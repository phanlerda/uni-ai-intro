
---

# 📚 KIẾN THỨC TRỌNG TÂM – AI2503: TRI THỨC & SUY DIỄN

---

## I. 🧠 **KIẾN TRÚC AGENT DỰA TRÊN TRI THỨC**

**Agent dựa trên tri thức (Knowledge-Based Agent)**:

* Mỗi vòng lặp:

  1. `TELL(KB, percept)` – cập nhật KB bằng tri giác.
  2. `ASK(KB, action)` – hỏi KB nên làm gì.
  3. `TELL(KB, action)` – cập nhật lại KB với hành động vừa chọn.

**Ứng dụng mẫu**: Wumpus World – môi trường mô phỏng AI điều hướng dựa vào tri giác và luật logic.

---

## II. 🔗 **LOGIC MỆNH ĐỀ (Propositional Logic)**

* **Ký hiệu**: P, Q, R, ...
* **Cú pháp**:

  * Phủ định `¬`, hội `∧`, tuyển `∨`, kéo theo `⇒`, tương đương `⇔`
* **Ngữ nghĩa**:

  * Dùng bảng chân trị để xác định đúng/sai.
  * Entailment: `α |= β` ⇔ mọi mô hình mà α đúng → β cũng đúng.

### 📌 **Suy diễn (Inference)**:

* **Soundness**: nếu `KB ⊢ α` thì chắc chắn `KB |= α`
* **Completeness**: nếu `KB |= α` thì ta có thể chứng minh `α` từ `KB`

### 🎯 Các phương pháp:

1. **Truth Table** – đầy đủ nhưng chậm (2^n mô hình).
2. **Resolution (giải bằng phản chứng)**:

   * Đưa về **CNF**
   * Chứng minh `KB |= α` bằng cách kiểm tra `KB ∧ ¬α` **vô nghiệm**.

---

## III. 🧩 **SUY DIỄN HORN CLAUSE (Horn Clause Inference)**

* **Horn clause**: tối đa 1 mệnh đề dương. Dễ viết dưới dạng kéo theo.
* Cho phép **suy diễn tuyến tính**:

  * **Forward Chaining**: từ facts → goal
  * **Backward Chaining**: từ goal → facts

### ⚙️ Algorithm cơ bản:

* Duyệt rule: nếu đủ điều kiện vế trái thì suy ra vế phải.
* Kết thúc khi tìm được goal hoặc không còn gì để suy.

---

## IV. 🤖 **SUY DIỄN TỰ ĐỘNG & LẬP KẾ HOẠCH (DPLL, Planning)**

### DPLL (Davis–Putnam–Logemann–Loveland)

* Thuật toán SAT solver hiện đại (cho logic mệnh đề).
* Dựa trên:

  * **Pure Symbol**: ký hiệu chỉ xuất hiện với 1 chiều.
  * **Unit Clause**: clause chỉ có 1 literal → bắt buộc phải đúng.

---

## V. 🌐 **LOGIC VỊ TỪ BẬC NHẤT (First-Order Logic – FOL)**

* **Bổ sung**: biến, hàm, lượng từ `∀`, `∃`
* **Cấu trúc cơ bản**:

  * **Term**: biểu diễn đối tượng (`John`, `Father(John)`)
  * **Atomic Sentence**: quan hệ (`Brother(x,y)`)
  * **Quantifier**: `∀x`, `∃x`

### ✍️ Ví dụ:

* `∀x Human(x) ⇒ Mortal(x)` – tất cả người đều phải chết
* `∃x Loves(x, Socrates)` – có ai đó yêu Socrates

---

## VI. 🔍 SUY DIỄN TRONG FOL

### 1. **Universal / Existential Instantiation**

* `∀x P(x)` → `P(John)`
* `∃x P(x)` → `P(c)` (c là constant mới)

### 2. **Unification**

* Tìm phép thay thế biến để hai biểu thức giống nhau.
* `Unify(Knows(John,x), Knows(y,Mary))` → `{x=Mary, y=John}`

### 3. **Generalized Modus Ponens**

* Cho: `P1(x) ∧ ... ∧ Pn(x) ⇒ Q(x)`
  Nếu `P1, ..., Pn` đúng thì kết luận `Q`.

---

## VII. ⚔️ SUY DIỄN THEO DẠNG LẬP LUẬN

| Phương pháp           | Áp dụng cho       | Ưu điểm                        |
| --------------------- | ----------------- | ------------------------------ |
| **Resolution**        | PL, FOL (với CNF) | Tổng quát, phổ biến            |
| **Forward Chaining**  | Horn KB           | Hiệu quả với nhiều facts       |
| **Backward Chaining** | Horn KB           | Tập trung vào goal, ít mở rộng |
| **DPLL**              | SAT solver        | Giải bài toán boolean logic    |

---

## VIII. 🏆 TỔNG KẾT HỌC NHANH

| Nội dung               | Ghi nhớ cốt lõi                                  |
| ---------------------- | ------------------------------------------------ |
| Logic mệnh đề          | Biết CNF, Resolution, bảng chân trị              |
| Horn Clause            | Suy diễn nhanh, dùng Modus Ponens                |
| FOL                    | Sử dụng ∀, ∃, Unify, substitution                |
| Forward/Backward Chain | 2 hướng để đạt goal từ KB                        |
| DPLL                   | SAT solver hiện đại, dùng pure & unit heuristics |
| Wumpus World           | Mô hình áp dụng lý thuyết logic vào agent AI     |

---
