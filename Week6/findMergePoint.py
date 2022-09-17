def findMergePoint(head1,head2):
      nodes = set()
  while head1:
    nodes.add(head1)
    head1 = head1.next
  while head2:
    if head2 in nodes:
      return head2
    head2 = head2.next
  return None