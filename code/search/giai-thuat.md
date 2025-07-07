
---

## ⚙️ 1. A\* Search

```python
import heapq

def a_star(start, goal, neighbors_fn, cost_fn, heuristic_fn):
    frontier = [(0 + heuristic_fn(start), 0, start, [])]  # (f, g, node, path)
    visited = {}

    while frontier:
        f, g, node, path = heapq.heappop(frontier)
        if node in visited and visited[node] <= g:
            continue
        visited[node] = g
        new_path = path + [node]

        if node == goal:
            return new_path

        for neighbor in neighbors_fn(node):
            cost = cost_fn(node, neighbor)
            h = heuristic_fn(neighbor)
            heapq.heappush(frontier, (g + cost + h, g + cost, neighbor, new_path))

    return None
```

---

## ⚖️ 2. Uniform-Cost Search (UCS)

```python
def uniform_cost_search(start, goal, neighbors_fn, cost_fn):
    frontier = [(0, start, [])]  # (g, node, path)
    visited = {}

    while frontier:
        g, node, path = heapq.heappop(frontier)
        if node in visited and visited[node] <= g:
            continue
        visited[node] = g
        new_path = path + [node]

        if node == goal:
            return new_path

        for neighbor in neighbors_fn(node):
            cost = cost_fn(node, neighbor)
            heapq.heappush(frontier, (g + cost, neighbor, new_path))

    return None
```

---

## 🧠 3. Greedy Best-First Search

```python
def greedy_bfs(start, goal, neighbors_fn, heuristic_fn):
    frontier = [(heuristic_fn(start), start, [])]
    visited = set()

    while frontier:
        h, node, path = heapq.heappop(frontier)
        if node in visited:
            continue
        visited.add(node)
        new_path = path + [node]

        if node == goal:
            return new_path

        for neighbor in neighbors_fn(node):
            heapq.heappush(frontier, (heuristic_fn(neighbor), neighbor, new_path))

    return None
```

---

## 🌐 4. Breadth-First Search (BFS)

```python
from collections import deque

def bfs(start, goal, neighbors_fn):
    frontier = deque([(start, [])])
    visited = set()

    while frontier:
        node, path = frontier.popleft()
        if node in visited:
            continue
        visited.add(node)
        new_path = path + [node]

        if node == goal:
            return new_path

        for neighbor in neighbors_fn(node):
            frontier.append((neighbor, new_path))

    return None
```

---

## 🔁 5. Depth-First Search (DFS)

```python
def dfs(start, goal, neighbors_fn):
    stack = [(start, [])]
    visited = set()

    while stack:
        node, path = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        new_path = path + [node]

        if node == goal:
            return new_path

        for neighbor in reversed(neighbors_fn(node)):
            stack.append((neighbor, new_path))

    return None
```

---

## ⛰️ 6. Hill-Climbing

```python
def hill_climbing(start, neighbors_fn, value_fn):
    current = start
    while True:
        neighbors = neighbors_fn(current)
        if not neighbors:
            return current
        next_node = max(neighbors, key=value_fn)
        if value_fn(next_node) <= value_fn(current):
            return current
        current = next_node
```

---

## 🌡️ 7. Simulated Annealing

```python
import math, random

def simulated_annealing(start, neighbors_fn, value_fn, schedule_fn, max_steps=1000):
    current = start
    for t in range(max_steps):
        T = schedule_fn(t)
        if T == 0:
            return current
        next_node = random.choice(neighbors_fn(current))
        delta = value_fn(next_node) - value_fn(current)
        if delta > 0 or random.random() < math.exp(delta / T):
            current = next_node
    return current
```

---

## 🧬 8. Genetic Algorithm (cho bài toán như 8-Queens)

```python
import random

def genetic_algorithm(population, fitness_fn, crossover_fn, mutate_fn, generations=1000, mutation_rate=0.1):
    for _ in range(generations):
        population = sorted(population, key=fitness_fn, reverse=True)
        if fitness_fn(population[0]) == 1.0:
            return population[0]
        next_gen = population[:2]
        while len(next_gen) < len(population):
            parents = random.choices(population[:10], k=2)
            child = crossover_fn(parents[0], parents[1])
            if random.random() < mutation_rate:
                child = mutate_fn(child)
            next_gen.append(child)
        population = next_gen
    return population[0]
```

---
