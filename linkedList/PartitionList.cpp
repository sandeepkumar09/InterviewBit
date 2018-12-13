/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
ListNode* Solution::partition(ListNode* A, int B) {
	ListNode *current, *previous, *nextNode;
	previous = NULL;
	currentPoint = A;
	nextNode = A
	while(current){
		if(current->val <= B){
			if(previous == NULL)
				previous = A;
			else
				previous = previous->next;
			temp = previous->val;
			previous->val = current->val;
			current->val = temp;
		}
	}
	return A;
}
