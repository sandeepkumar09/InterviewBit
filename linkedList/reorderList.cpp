/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
ListNode* Solution::reorderList(ListNode* A) {
	if(A ==NULL || A->next == NULL)
		return A;
	ListNode *current, *previous, *next, *headB;
	int length = 0, midLength = 1;
	current = A;
	previous = NULL;
	while(current){
		current = current->next;
		length += 1;
	}
	current = A;
	midLength = 1;
	while(midLength <= (length / 2)){
		previous = current;
		current = current->next;
		midLength += 1;
	}
	previous->next = NULL;
	while(current){
		next = current->next;
		current->next = previous;
		previous = current;
		current = next;
	}
	ListNode *headB = previous
	ListNode *currentA = A;
	ListNode *currentB = headB;
	ListNode *previousA;
	ListNode *previousB;
	while(currentA){
		nextA = currentA->next;
		nextB = currentB->next;
		currentA->next = currentB;
		currentA = nextA;
		currentB = nextB;
	}


}
