def deleteNode(node):
  if(node==None or node.next==None):
    return
  temp=node
  while (node.next !=None):
    temp=node
    node=node.next
    temp.data=node.data
  temp.next=None

