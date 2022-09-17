class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def printList(node):
  while (node != None):
    print(node.data, end=' ');
    node = node.next;
    
def insertEnd(head, data):
  new_node = Node(data)
  if head is None:
    head = new_node
    return head;
    
  last = head
  while (last.next):
    last = last.next
    
  last.next =  new_node
  return head;

def getLen(head):
    temp = head
    p = 0
 
    while(temp != None):
        p += 1
        temp = temp.next
 
    return p
def findMiddle(head):
  if head != None:
    a =getLen(head)
    temp = head
    midIdx = a // 2
    while midIdx != 0:
      temp = temp.next
      midIdx -= 1
    return temp.data
  else:
    return -1
def findNLast(head,n):
  length=getLen(head)
  temp = head
  if(length!=0):
    if(length>n):
      for i in range(0, length - n):
        temp = temp.next
      return temp.data
    else:
      return length
  else:
    return -1
def main():
    t = int(input().strip())
    for i in range(t):
      head = None
      n = int(input().strip())
      if n!=0:
        string = input().strip().split()
        for j in string:
          head = insertEnd(head,int(j.strip()))
      k = int(input())
      print(findMiddle(head))
      print(findNLast(head,k))
        
if __name__ == "__main__":
  main();