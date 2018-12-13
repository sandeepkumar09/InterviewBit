/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
ListNode* Solution::deleteDuplicates(ListNode* A) {
	if(!A || !A->next)
        return A;
	ListNode *current, *previous, *nextNode, *head ,*maydist;
	int value , flag = 1, headFlag = 1;
	current = A->next;
	value = A->val;
	maydist = A;
	while(current){
		if(current->val == value){
			current = current->next;
			flag = 0;
		}
		else if((current->val != value) && flag == 1 ){
			if(headFlag == 1){
				head = maydist;
				previous = maydist;
				headFlag = 0;
			}
			else{
				previous->next = maydist;
				previous = previous->next;
			}
			maydist = current;
			value = current->val;
			current = current->next;
			flag = 1;
		}
		else{
			maydist = current;
			value = current->val;
			current = current->next;
			flag = 1;
		}
	}
	return head;
}	
