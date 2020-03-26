class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insert(self,Newnode):
        if self.head is None:
            self.head=Newnode
        else:
            lastnode=self.head
            while True:
                if lastnode.next is None:
                    break
                else:
                    lastnode=lastnode.next
            lastnode.next=Newnode
    def printllist(self):
        if self.head is None:
            print('linked list is empty')
            return
        currentnode=self.head
        while True:
            if currentnode is None:
                break
            print(currentnode.data)
            currentnode=currentnode.next
                                  
if __name__ == '__main__':
    firstnode=Node("jack")
    llist=LinkedList()
    llist.insert(firstnode)
    secondnode=Node("rose")
    llist.insert(secondnode)
    thirdnode=Node("lily")
    llist.insert(thirdnode)
    llist.printllist()



