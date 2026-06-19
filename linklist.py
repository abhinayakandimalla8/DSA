l1=[4,5,3,7,6]
class Node:
    def __init__(self,data):
        self.data = data
        self.next = Node   
def createList(i1):
    head=None
    for i in l1:
        if head is None:
            head=Node(i)
            return