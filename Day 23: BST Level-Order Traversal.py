import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        #Write your code here
        qu=[root]
        while len(qu)!=0:
            curr=qu[0]
            qu=qu[1:]
            print(str(curr.data)+' ',end="")
            if curr.left!=None:
                qu.append(curr.left)
            if curr.right!=None:
                qu.append(curr.right)

T=int(input())
