# 🧠 HEAPS — INTERVIEW FLASHCARDS

## 1️⃣ K Smallest / K Largest Elements

**Pattern**: Fixed-size heap  
**Heap**:

- K smallest → **max heap** of size `k`
    
- K largest → **min heap** of size `k`
    

**Invariant**:  
Heap always contains the best `k` candidates so far.

**Why heap?**  
Keeps only relevant elements → `O(n log k)`

**Common bug**:  
Using full heap instead of size-k heap.

```
 🧠 Interview Explanation
 “I maintain a max-heap of size k.
 The heap stores the k smallest elements seen so far.
 If a new element is smaller than the largest in the heap, I replace it.
 This gives O(n log k) time and O(k) space.”
```

---

## 2️⃣ Kth Smallest / Largest Element

**Pattern**: Same as above, but return root

**Key Insight**:  
Root of heap = answer once all elements processed.

---

## 3️⃣ Sort a K-Sorted Array

**Pattern**: Sliding heap window  
**Heap**: Min heap of size `k+1`

**Invariant**:  
Smallest element must lie within next `k+1` range.

**Time**: `O(n log k)`

```
🧠 Interview Explanation
“Since the array is k-sorted, the smallest element must lie within the first k+1 elements.
I maintain a min-heap of size k+1 and repeatedly extract the minimum, giving an O(n log k) solution.”
```
---

## 4️⃣ Top K Frequent Elements

**Pattern**: Frequency + heap  
**Heap**: Min heap of size `k` (freq, value)

**Why min heap?**  
Pop lowest frequency when size exceeds `k`.

**Alternative**: Bucket sort (when range is small).

```
“I maintain a min-heap of size k containing the k largest elements seen so far.
The smallest element in the heap is the kth largest overall.”
```

---

## 5️⃣ Merge K Sorted Lists

**Pattern**: Multi-pointer merge  
**Heap entry**: `(value, list_index, element_index)`

**Invariant**:  
Heap always holds one element per list.

**Stop when**: Any list is exhausted.

---

## 6️⃣ Minimum Cost to Connect Ropes

**Pattern**: Greedy merge  
**Heap**: Min heap

**Rule**:  
Always merge **two smallest** ropes.

**Why?**  
Large ropes get reused → minimize repeated cost.

---

## 7️⃣ Find Median from Data Stream

**Pattern**: Two heaps

- `small` → max heap
    
- `large` → min heap
    

**Invariant**:

```
|small| >= |large|
max(small) <= min(large)
```

**Median**:

- Odd → root of `small`
    
- Even → avg of roots
    

---

## 8️⃣ Sliding Window Median

**Pattern**: Two heaps + lazy deletion  
**Extra DS**: `delayed` hashmap

**Key Operations**:

- `add(num)`
    
- `remove(num)`
    
- `prune(heap)`
    
- `rebalance()`
    

**Why prune?**  
Heap can’t delete arbitrary elements.

**Invariant**:

`small_size == large_size or +1`

---

## 9️⃣ Reorganize String

**Pattern**: Max heap + greedy pairing  
**Heap**: `(-freq, char)`

**Rule**:

- Always place **two most frequent chars**
    
- Reinsert after decrement
    

**Impossible if**:  
Remaining char freq > 1 at the end.

---

## 🔟 Task Scheduler

**Pattern**: Greedy scheduling + cycles  
**Heap**: Max heap of frequencies

**Cycle size**: `n + 1`

**Per cycle**:

- Execute up to `n+1` distinct tasks
    
- Delay reinsertion
    
- Add idle **only if tasks remain**
    

**Key Line**:

```
if heap:
    time += cycle
```

**Math shortcut**:

`max(len(tasks), (max_freq - 1)*(n + 1) + count_max)`

---

## 1️⃣1️⃣ Smallest Range Covering K Sorted Lists

**Pattern**: Sliding window across lists  
**Heap**: Min heap  
**Track**: `current_max`

**Invariant**:  
Heap always has **one element per list**

**Move**:  
Only advance pointer of **minimum element**

**Stop when**:  
Any list runs out

---

# 🎯 HOW TO RECOGNIZE HEAP PROBLEMS

Ask yourself:

- “Do I need top-K?”
    
- “Do I need min/max repeatedly?”
    
- “Am I merging sorted streams?”
    
- “Is greedy choice always the best next step?”
    

If yes → **heap**.

---

# 🧠 HEAP PATTERN MAP

|Problem Type|Heap Pattern|
|---|---|
|Top K|Fixed-size heap|
|Median|Two heaps|
|Scheduling|Heap + cycles|
|Sliding window|Heap + lazy deletion|
|Multi-list|Heap + pointers|
|Greedy merge|Min heap|

---

# 🏁 FINAL STATUS

You now:

- recognize heap patterns instantly
    
- maintain correct invariants
    
- avoid common pitfalls
    
- explain decisions clearly
    

👉 **Heap mastery achieved** 🏆