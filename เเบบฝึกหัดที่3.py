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

def is_max_heap(arr):
    n = len(arr)
    for i in range(n // 2):  # ตรวจสอบเฉพาะโหนดภายใน
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[i] < arr[left]:
            return False
        if right < n and arr[i] < arr[right]:
            return False
    return True

# ค่าที่จะเพิ่มลงใน Max Heap
elements = [5, 3, 8, 1, 2, 7, 6, 4]

# สร้าง Max Heap
max_heap = MaxHeap()
for element in elements:
    max_heap.push(element)

# แสดงค่า Max Heap ที่ได้
print("Max Heap:", max_heap.get_heap())

# ลบค่าสูงสุด 3 ครั้ง
for i in range(3):
    removed = max_heap.pop()
    print(f"หลังจากลบ {removed}:", max_heap.get_heap())

# ตรวจสอบว่าเป็น Max Heap หรือไม่
print("เป็น Max Heap หรือไม่:", is_max_heap(max_heap.get_heap()))
