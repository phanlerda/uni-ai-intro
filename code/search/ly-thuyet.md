
---

# 📚 TỔNG HỢP LÝ THUYẾT GIẢI THUẬT TÌM KIẾM TRONG AI

---

## I. 🔎 PHÂN LOẠI GIẢI THUẬT

| Phân loại             | Đặc điểm chính                      | Dùng khi nào                           |
| --------------------- | ----------------------------------- | -------------------------------------- |
| **Uninformed Search** | Không có kiến thức thêm về bài toán | Không biết thông tin mục tiêu          |
| **Informed Search**   | Có dùng heuristic (hàm ước lượng)   | Biết hướng đến goal, cần tìm nhanh hơn |
| **Local Search**      | Không theo dõi đường đi, chỉ tối ưu | Không có goal rõ ràng, cần tối ưu hóa  |

---

## II. ⚙️ UNINFORMED SEARCH

### 1. **Breadth-First Search (BFS)**

* Mở rộng node **nông nhất trước**.
* Dùng **FIFO queue**.
* Tối ưu nếu chi phí các bước bằng nhau.
* **Không hiệu quả với không gian lớn** (tốn bộ nhớ).

### 2. **Depth-First Search (DFS)**

* Mở rộng node **sâu nhất trước**.
* Dùng **stack** (LIFO).
* Không tối ưu, có thể đi lạc vô hạn.
* Ít tốn bộ nhớ hơn BFS.

### 3. **Depth-Limited Search (DLS)**

* Giống DFS nhưng giới hạn độ sâu.
* Tránh được vấn đề "đi lạc vô tận".

### 4. **Uniform-Cost Search (UCS)**

* Mở rộng node có **tổng chi phí thấp nhất**.
* Dùng **priority queue** theo `g(n)` – chi phí từ start đến node hiện tại.
* **Tối ưu**, miễn chi phí luôn dương.

---

## III. 🧠 INFORMED (HEURISTIC) SEARCH

### 📌 Khái niệm quan trọng:

* **Heuristic `h(n)`**: ước lượng chi phí từ node `n` đến goal.
* Phải **admissible**: không bao giờ > chi phí thực.
* Nếu **consistent**: đảm bảo optimal hơn.

---

### 5. **Greedy Best-First Search**

* Chọn node có `h(n)` thấp nhất (ước lượng đến goal).
* Nhanh nhưng **không tối ưu**.
* Dùng priority queue theo `h(n)`.

### 6. **A\* Search**

* Kết hợp chi phí thực và ước lượng:

  `f(n) = g(n) + h(n)`

  * `g(n)` = chi phí từ start → `n`.
  * `h(n)` = ước lượng từ `n` → goal.
* **Tối ưu và hiệu quả** nếu `h(n)` tốt.
* Dùng rất nhiều trong:

  * Game pathfinding
  * Xe tự lái, robot navigation
  * Bài toán ràng buộc

---

## IV. 🔁 LOCAL SEARCH & OPTIMIZATION

### Không cần lưu vết đường đi – chỉ quan tâm trạng thái hiện tại.

### 7. **Hill-Climbing**

* Luôn chọn hàng xóm tốt nhất.
* Dễ bị **kẹt ở local optimum**.
* Nhanh, ít tốn RAM.

### 8. **Simulated Annealing (SA)**

* Cho phép **chấp nhận nghiệm xấu** với xác suất:

  `P = exp(−ΔE / T)`

  * `ΔE`: độ xấu đi
  * `T`: nhiệt độ (giảm dần)
* Tránh kẹt local optimum → tìm global optimum.

### 9. **Local Beam Search**

* Duy trì `k` trạng thái tốt nhất cùng lúc.
* Mỗi bước tạo các successor → chọn `k` tốt nhất tiếp theo.
* Khả năng song song cao.

### 10. **Genetic Algorithm (GA)**

* Mỗi trạng thái là **một cá thể (gene)**.
* Tiến hóa qua:

  * **Fitness function**
  * **Crossover**
  * **Mutation**
* Mạnh với bài toán:

  * Tối ưu tổ hợp (8-queen, TSP)
  * Bài toán không tuyến tính

---

## V. 🎯 TÓM TẮT SO SÁNH

| Tên thuật toán      | Dùng Heuristic | Tối ưu | Bộ nhớ thấp | Cần dùng khi                           |
| ------------------- | -------------- | ------ | ----------- | -------------------------------------- |
| BFS                 | ❌              | ✅      | ❌           | Tìm đường ngắn nhất, chi phí bằng nhau |
| DFS                 | ❌              | ❌      | ✅           | Không cần optimal, không gian lớn      |
| UCS                 | ❌              | ✅      | ❌           | Chi phí biến đổi, không có `h(n)`      |
| Greedy BFS          | ✅              | ❌      | ❌           | Nhanh, nhưng không đảm bảo tốt nhất    |
| A\*                 | ✅              | ✅      | ❌           | Tốt nhất nếu có `h(n)` tốt             |
| Hill-Climbing       | ✅              | ❌      | ✅           | Tối ưu local nhanh                     |
| Simulated Annealing | ✅              | ✅      | ✅           | Tránh local optimum                    |
| Genetic Algorithm   | ✅              | ✅      | ✅           | Không gian lớn, không tuyến tính       |

---
