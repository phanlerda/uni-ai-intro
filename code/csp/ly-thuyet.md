Dưới đây là các đoạn **code Python cốt lõi** để giải bài toán CSP với 3 phương pháp chính:

---

# ✅ 1. AC-3 Algorithm (Arc Consistency)

```python
from collections import deque

def ac3(csp):
    queue = deque([(xi, xj) for xi in csp['neighbors'] for xj in csp['neighbors'][xi]])
    
    while queue:
        xi, xj = queue.popleft()
        if revise(csp, xi, xj):
            if not csp['domains'][xi]:
                return False
            for xk in csp['neighbors'][xi]:
                if xk != xj:
                    queue.append((xk, xi))
    return True

def revise(csp, xi, xj):
    revised = False
    for x in set(csp['domains'][xi]):
        if not any(csp['constraints'](xi, x, xj, y) for y in csp['domains'][xj]):
            csp['domains'][xi].remove(x)
            revised = True
    return revised
```

---

# ✅ 2. Backtracking Search (với MRV + LCV + Forward Checking)

```python
def backtracking_search(csp):
    return backtrack({}, csp)

def backtrack(assignment, csp):
    if len(assignment) == len(csp['variables']):
        return assignment

    var = select_unassigned_variable(assignment, csp)
    for value in order_domain_values(var, assignment, csp):
        if is_consistent(var, value, assignment, csp):
            assignment[var] = value
            removals = forward_check(var, value, csp)
            result = backtrack(assignment, csp)
            if result:
                return result
            del assignment[var]
            restore(csp, removals)
    return None

def select_unassigned_variable(assignment, csp):
    unassigned = [v for v in csp['variables'] if v not in assignment]
    return min(unassigned, key=lambda var: len(csp['domains'][var]))  # MRV

def order_domain_values(var, assignment, csp):
    return sorted(csp['domains'][var], key=lambda val: count_conflicts(var, val, assignment, csp))  # LCV

def is_consistent(var, val, assignment, csp):
    for neighbor in csp['neighbors'][var]:
        if neighbor in assignment:
            if not csp['constraints'](var, val, neighbor, assignment[neighbor]):
                return False
    return True

def forward_check(var, val, csp):
    removals = []
    for neighbor in csp['neighbors'][var]:
        if val in csp['domains'][neighbor]:
            csp['domains'][neighbor].remove(val)
            removals.append((neighbor, val))
    return removals

def restore(csp, removals):
    for var, val in removals:
        csp['domains'][var].append(val)

def count_conflicts(var, val, assignment, csp):
    count = 0
    for neighbor in csp['neighbors'][var]:
        if val in csp['domains'][neighbor]:
            count += 1
    return count
```

---

# ✅ 3. Min-Conflicts (Local Search)

```python
import random

def min_conflicts(csp, max_steps=1000):
    assignment = {v: random.choice(csp['domains'][v]) for v in csp['variables']}

    for _ in range(max_steps):
        conflicted = [v for v in csp['variables'] if not is_consistent(v, assignment[v], assignment, csp)]
        if not conflicted:
            return assignment
        var = random.choice(conflicted)
        value = min(csp['domains'][var], key=lambda val: count_conflicts(var, val, assignment, csp))
        assignment[var] = value
    return None
```

---

# 📦 Ví dụ đơn giản: Map Coloring (Úc)

```python
variables = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
domains = {v: ['red', 'green', 'blue'] for v in variables}
neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['SA', 'Q', 'V'],
    'V': ['SA', 'NSW'],
    'T': []
}

def constraint(a, va, b, vb):
    return va != vb

csp = {
    'variables': variables,
    'domains': {v: list(domains[v]) for v in variables},
    'neighbors': neighbors,
    'constraints': constraint
}
```

---

## 📌 Gợi ý sử dụng:

```python
# AC-3 (lọc trước)
ac3(csp)

# Backtracking
solution_bt = backtracking_search(csp)
print("Backtracking:", solution_bt)

# Min-Conflicts
solution_mc = min_conflicts(csp)
print("Min-Conflicts:", solution_mc)
```

---

Bạn muốn tôi triển khai một bài toán cụ thể như **Sudoku**, **8-Queens**, hoặc **Job-Shop Scheduling** bằng CSP không? Tôi có thể dựng full code theo yêu cầu.
