

---

## 🕹️ **Mô tả bài toán Wumpus World 4x4**

### ✅ Luật chơi cơ bản:

* Agent bắt đầu ở \[1,1], hướng phải.
* Có **1 con Wumpus**, vài hố (*pit*) và 1 cục vàng.
* Agent cảm nhận qua: `Stench`, `Breeze`, `Glitter`, `Bump`, `Scream`.

---

### 🧩 **Bố trí môi trường (ẩn - agent không biết)**:

| Vị trí | Nội dung |
| ------ | -------- |
| \[1,3] | Pit      |
| \[2,2] | Wumpus   |
| \[2,3] | Gold     |
| \[3,1] | Pit      |

---

## 👀 **Các tri giác agent nhận được theo bước**

Agent di chuyển theo:
`[1,1] → [2,1] → [2,2] → [2,3]`

| Vị trí | Tri giác (Percept)                      |
| ------ | --------------------------------------- |
| \[1,1] | `[None, None, None, None, None]`        |
| \[2,1] | `[None, Breeze, None, None, None]`      |
| \[2,2] | `[Stench, None, None, None, None]`      |
| \[2,3] | `[Stench, Breeze, Glitter, None, None]` |

---

## 🧠 **Xây dựng cơ sở tri thức (KB)**

Biến logic (trạng thái vị trí):

* `Pxy`: có hố ở \[x,y]
* `Wxy`: có Wumpus ở \[x,y]
* `Bxy`: có Breeze ở \[x,y]
* `Sxy`: có Stench ở \[x,y]

---

## 🧮 **Diễn dịch tri giác thành các mệnh đề logic**

### Tại \[1,1]:

* Không Breeze, không Stench → loại các pit và wumpus gần:

```text
¬P1,2 ∧ ¬P2,1
¬W1,2 ∧ ¬W2,1
```

### Tại \[2,1]:

* Có Breeze → 1 trong các ô gần là Pit:

```text
B2,1 ⇔ (P1,1 ∨ P3,1 ∨ P2,2)
=> P3,1 ∨ P2,2 (vì P1,1 = false từ trước)
```

### Tại \[2,2]:

* Có Stench → Wumpus kề cận:

```text
S2,2 ⇔ (W1,2 ∨ W2,1 ∨ W2,3 ∨ W3,2)
=> W2,1 ∨ W2,3 ∨ W3,2 (vì W1,2 đã bị loại)
```

### Tại \[2,3]:

* Có Stench + Breeze + Glitter → Có vàng + pit gần + wumpus gần:

```text
Glitter ở đây → có Gold tại [2,3]
B2,3 ⇔ (P1,3 ∨ P2,2 ∨ P3,3)
S2,3 ⇔ (W1,3 ∨ W2,2 ∨ W2,4 ∨ W3,3)
```

---

## 🔍 **Suy luận theo Resolution / Modus Ponens**

### Mục tiêu: Có an toàn không nếu đi đến \[1,3]?

Ta biết:

* B2,3 ⇔ (P1,3 ∨ P2,2 ∨ P3,3)
* Đã biết B2,3 = true
* Nếu ta kiểm tra ¬P2,2 và ¬P3,3 (qua các bước tiếp theo), thì P1,3 phải là pit.

→ Agent có thể dùng suy luận:

```text
Nếu ¬P2,2 ∧ ¬P3,3 ⇒ P1,3
→ Không nên đi vào [1,3]
```

---

## ✅ **Kết luận hành động từ KB**

Tại \[2,3]:

* Có Glitter → Agent nên Grab
* Không nên đi \[1,3] vì có nguy cơ Pit.
* Wumpus rất có thể ở \[2,2] → nếu có tên, có thể bắn.

---

## 🧠 **Hành vi agent sau khi suy luận**

1. Di chuyển từ \[1,1] → \[2,1] → \[2,2] → \[2,3]
2. Phân tích:

   * Grab vàng.
   * Tránh \[1,3] và \[3,3] (nguy cơ Pit)
   * Tránh Wumpus nếu chưa có tên hoặc chưa xác định vị trí chắc chắn.
3. Quay về \[2,1] → \[1,1] và Climb ra khỏi hang.

---

## 📌 Tổng kết suy luận

| Vị trí | Phân tích logic                   |
| ------ | --------------------------------- |
| \[1,1] | An toàn tuyệt đối                 |
| \[2,1] | Có breeze → gần đó có pit         |
| \[2,2] | Có stench → gần đó có Wumpus      |
| \[2,3] | Có Glitter → có vàng ở đây        |
| \[1,3] | Có khả năng Pit (từ các suy diễn) |

---

