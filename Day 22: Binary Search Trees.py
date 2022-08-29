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

    def getHeight(self,root):
        #Write your code here
        routes = ['root']
        i = 0
        while i < len(routes):
            if eval(routes[i] + '.right'):
                routes.append(routes[i] + '.right')    
            if eval(routes[i] + '.left'):
                routes.append(routes[i] + '.left')
            i += 1
        return max(route.count('left') + route.count('right') for route in routes)
        

T=int(input())
