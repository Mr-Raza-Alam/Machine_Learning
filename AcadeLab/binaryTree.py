 # Binary Tree 
class Node:
    def __init__(self,x):
        self.item = x
        self.left = None
        self.right = None

class BT:
    def __init__(self):
        self.idx = -1  # To keep track of current index

    def build_BT(self,num):
        self.idx += 1 
        if self.idx == len(num) or num[self.idx] == -1:
            return None
        else:
            newNode = Node(num[self.idx])
            newNode.left = self.build_BT(num)
            newNode.right = self.build_BT(num)
            return newNode

    def preorder(self,root):
        if root is None:
            return
        print(root.item,end=" ")
        self.preorder(root.left)
        self.preorder(root.right)
    
    def inorder(self,root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.item,end=" ")
        self.inorder(root.right)

    def height_BT(self,root):
        if root is None:
            return 0
        lh = self.height_BT(root.left)
        rh = self.height_BT(root.right)
        return max(lh, rh) + 1
    
# initialize 
# lst = [1,2,4,-1,-1,5,-1,-1,3,-1,6,-1,-1]
lst = [5,6,2,-1,5,-1,7,-1,-1,-1,7,9,-1,8,-1,-1,1,-1,-1]
print("The avialable data is : ",lst)
bt = BT()
root = bt.build_BT(lst)
bt.inorder(root)
print("\nThe height of the tree = ",bt.height_BT(root))








