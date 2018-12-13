//https://www.xvideos.com/video22665059/abigaile_johnson_2_-_sexygirlstripping.com/**
/*
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
int Solution::lPalin(ListNode* A) {
	ListNode *current, *previous, *lastNode, *nextNode, *previousToLast;
	current = A;
	nextNode = A->next;
	lastNode = A;
	if(A == NULL && A->next == NULL)
		return 0
	while(lastNode->next){
		lastNode = lastNode->next;
	}
	while(current != lastNode){
		while(nextNode != lastNode){
			previousToLast = nextNode;
			nextNode = nextNode->next;			
		}
		if(current->val != lastNode->val)
			return 0
		current = current->next;
		lastNode = previousToLast;
	}
	return 1
}