ListNode* Solution::insertionSortList(ListNode* A) {
	ListNode *current, *previous, *nextNode;
	ListNode *sortedCurrent, *sortedHead, *temp;
	if( A == NULL || A->next == NULL)
		return A;
	current = A->next;
	sortedHead = A;
	while( current ){
		previous = current;
		current = current->next;
		sortedCurrent = sortedHead;
		while(sortedCurrent){
			// add a new head
			if(sortedCurrent->val > previous->val){
				temp = sortedCurrent->next;
				if (sortedCurrent == sortedHead)
					sortedHead = previous;
				sortedCurrent = previous;
				sortedCurrent->next = temp;	 
			}
			// add at tail
			else if(sortedCurrent->next = NULL)
				sortedCurrent->next = previous;
			else
				sortedCurrent = sortedCurrent->next;
		}
	}
	return sortedHead;
}