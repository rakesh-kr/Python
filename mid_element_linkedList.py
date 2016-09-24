import sys

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def insert_begining(self,data):
        node=Node(data)
        node.next=self.head
        self.head=node

    def display(self):
        p=self.head
        while p is not None:
            print str(p.data) + " -> ",
            p=p.next
        print "NULL"

    def middle_element(self):
        p=self.head
        q=self.head
        while p.next is not None and q.next is not None and q.next.next is not None:
            p=p.next
            q=q.next.next
        self.display()
        print "Middle element is %s" %(p.data)
            



def main():
    newList=LinkedList()
    while(True):
        print "1:Insert 2:Find middle element 3:Display 4:Exit"
        n=int(raw_input("Enter:").rstrip())
        if n==1:
            data=raw_input("Enter node data:").rstrip()
            newList.insert_begining(data)
        elif n==2:
            newList.middle_element()
        elif n==3:
            newList.display()
        else:
            sys.exit("Exiting...!")
        




if __name__=="__main__":
    main()
