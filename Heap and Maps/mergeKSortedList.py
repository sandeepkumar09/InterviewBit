# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):
    	head = A[0]
    	current1 = head
    	if current1 != None:
    		next1 = current1.next;
    	for i in range(1,len(A)-1):
    		current2 = A[i]
    		while(current1 != None and current2 != None):
    			if current1 == None:
    				if current1 = head:
    					head = current2
    					previous = head
    				else:
    					previous.next = current2
    					previous = current2
    					current1 = head
    					break
    			elif current2 == None:
    				previous.next = current1
    				current1 = head
    				break
    			if current1 > current2:
    				if current1 == head:
    					head = current2
    					previous = head
    				else:
    					previous.next = current2
    					previous = current2
    				current2 = current2.next
    			else:
    				current1 = current1.next
    				previous = current1
    	return head