# Priority Queue
class PriorityQueue:
    def __init__(self):
        self.heap = []
    def parent(self,i):
        return (i-1)//2
    def leftChild(self,i):
        return (2*i)+1
    def rightChild(self,i):
        return (2*i)+2
    
    def insert(self, val):
        self.heap.append(val)
        # apply heapify_up to maintain min-heap property
        self._heapify_up(0)
    
    def _heapify_up(self,idx):
        while idx>0 and self.heap[self.parent(idx)] > self.heap[idx]:
            # swapp 
            self.heap[self.parent(idx)],self.heap[idx] = self.heap[idx],self.heap[self.parent(idx)] 
            idx = self.parent(idx)
    
    def extract_min(self):
        if not self.heap:
            return None 
        elif len(self.heap) == 1:
            return self.heap.pop()
        else:
            root = self.heap[0]
            self.heap[0] = self.heap.pop()
            #apply heapify_down to maintain min-heap property
            self._heapify_down(0)
        return root
    
    def _heapify_down(self,index):
        smallest = index
        left = self.leftChild(index)
        right = self.rightChild(index)

        if left<len(self.heap) and self.heap[left] < self.heap[index]:
            smallest = left 
        if right<len(self.heap) and self.heap[right] < self.heap[index]:
            smallest = right
        
        if smallest != index :
            self.heap[smallest],self.heap[index] = self.heap[index],self.heap[smallest] 
        self._heapify_down(smallest)
        
    def peek(self):
        if not self.heap:
            return None
        return self.heap[0]
    
    def isEmpty(self):
        return len(self.heap) == 0
    



