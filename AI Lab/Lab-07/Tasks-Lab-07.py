# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
class Node:
    def __init__(self, val,data,alpha,beta):

        self.left = None
        self.right = None
        self.data = data
        self.val = val
        self.alpha =alpha
        self.beta = beta

    def insert(self, data,val):
# Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data,val)
                else:
                    self.left.insert(data,val)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data,val)
                else:
                    self.right.insert(data,val)
        else:
            self.data = data
            self.val=val

# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.val," ",self.data,"alpha: ",self.alpha,"beta: ",self.beta),
        if self.right:
            self.right.PrintTree()

            
# Inorder traversal
# Left -> Root -> Right
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.val)
            res.append(root.data)
            
            res = res + self.inorderTraversal(root.right)
        return res        

# Preorder traversal
# Root -> Left ->Right
    def PreorderTraversal(self, root):
        res = []
        if root:
            res.append(root.val)
            res.append(root.data)
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return res   

# Postorder traversal
# Left ->Right -> Root
    def PostorderTraversal(self, root):
        res = []
        if root:
            res = self.PostorderTraversal(root.left)
            res = res + self.PostorderTraversal(root.right)
            res.append(root.val)
            res.append(root.data)
        return res

# findval method to compare the value with nodes
    def findval(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval)+" is not Found"
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return str(lkpval)+" is not Found"
            return self.right.findval(lkpval)
        else:
            return str(self.data) + " is found"


    def minDepth(self,root):
    
        if root is None:
            return 0
     
    # Base Case : Leaf node.This acoounts for height = 1
        if root.left is None and root.right is None:
            return 1
     
    # If left subtree is Null, recur for right subtree
        if root.left is None:
            return root.minDepth(root.right)+1
     
        # If right subtree is Null , recur for left subtree
        if root.right is None:
            return root.minDepth(root.left) +1
     
        return min(root.minDepth(root.left), root.minDepth(root.right))+1
    
    TargetDepth=0

    def Max(self,node,currDepth):
        if(node.left is None and node.right is None):
            return node.data
        if (currDepth == TargetDepth):
            return node.data
        node.data=np.NINF
    
        node.data=max(node.data,node.Min(node.left,currDepth+1),node.Min(node.right,currDepth+1))
        return node.data
        
    
            
    def Min(self,node,currDepth):
        if(node.left is None and node.right is None):
            return node.data
        if (currDepth == TargetDepth):
            return node.data
        node.data=np.Inf
        node.data=min(node.data,node.Max(node.left,currDepth+1),node.Max(node.right,currDepth+1))
        return node.data

    def MaxAlphaBeta(self,node,currDepth):
        if(node.left is None and node.right is None):
            return node.data
        if (currDepth == TargetDepth):
            return node.data
        node.data=np.NINF
    
        node.data=max(node.data,node.MinAlphaBeta(node.left,currDepth+1),node.MinAlphaBeta(node.right,currDepth+1))
        if node.data >= node.beta:
            return node.data
        if node.data>=node.alpha:
            node.alpha=node.data
        return node.data
        
    
            
    def MinAlphaBeta(self,node,currDepth):
        if(node.left is None and node.right is None):
            return node.data
        if (currDepth == TargetDepth):
            return node.data
        node.data=np.Inf
        node.data=min(node.data,node.MaxAlphaBeta(node.left,currDepth+1),node.MaxAlphaBeta(node.right,currDepth+1))
        if node.data <= node.alpha:
            return node.data
        if node.data<=node.beta:
            node.beta=node.data
        return node.data


root = Node('A', np.NINF,np.NINF,np.Inf); 
root.left = Node('B', np.Inf,np.NINF,np.Inf); 
root.right = Node('C', np.Inf,np.NINF,np.Inf);  
root.left.left = Node('D', np.NINF,np.NINF,np.Inf); 
root.left.right = Node('E', np.NINF,np.NINF,np.Inf); 
root.right.left = Node('F', np.NINF,np.NINF,np.Inf);
root.right.right = Node('G', np.NINF,np.NINF,np.Inf);
root.left.left.left = Node('H',-1,np.NINF,np.Inf);
root.left.left.right = Node('I',4,np.NINF,np.Inf);
root.left.right.left = Node('J',2,np.NINF,np.Inf);
root.left.right.right = Node('K',6,np.NINF,np.Inf);
root.right.left.left = Node('L',-3,np.NINF,np.Inf);
root.right.left.right = Node('M',-5,np.NINF,np.Inf);
root.right.right.left = Node('N',0,np.NINF,np.Inf);
root.right.right.right = Node('O',7,np.NINF,np.Inf);
TargetDepth = root.minDepth(root)
print("Depth:",TargetDepth)
#value = root.Max(root, 0)
#print(value)
value = root.MaxAlphaBeta(root, 0)
#print("Value: ",value)
root.PrintTree()