def solve(node):
    count = 0
    while node:
        count +=1
        node=node.next
    return count
class Solution:
    def swapNodes(head, k):
        for i in range(k-1):
            head = head.next
        return head
    print(swapNodes((1,2,3,4,5),2))