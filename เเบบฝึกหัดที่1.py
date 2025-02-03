import heapq

class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def push(self, value):
        heapq.heappush(self.heap, -value)  # ใช้ค่าลบเพื่อจำลอง Max Heap
    
    def pop(self):
        return -heapq.heappop(self.heap)
    
    def peek(self):
        return -self.heap[0] if self.heap else None
    
    def get_heap(self):
        return sorted([-x for x in self.heap], reverse=True)  # แสดงค่าตามลำดับ Max Heap

# ค่าที่จะเพิ่มลงใน Max Heap
elements = [5, 3, 8, 1, 2, 7, 6, 4]

# สร้าง Max Heap
max_heap = MaxHeap()
for element in elements:
    max_heap.push(element)

# แสดงค่า Max Heap ที่ได้
print("Max Heap:", max_heap.get_heap())
