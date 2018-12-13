/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
ListNode* Solution::reverseList(ListNode* A, int B) {
	ListNode *current, *previous, *nextNode;
	int length;
	previous = NUL
	current = A;
	length = 1;
	while(current){
		current = current->next;
		length += 1;
		if(length == B-1)
			newHead = current;
	}
	current = A;
	current = 1;
	while(currLenght <= length){
		while(tempLength <= B){
			nextNode = current->next;
			current->next = previous;
			previous = current;
			current = nextNode;
		}
		while(previous->next){
			previous = previous->next;
		}
		previous->next = current;

	}
	return newHead;
}
