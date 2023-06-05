#include "lists.h"

/**
* check_cycle - checks if a linked list contains a cycle
* list: linked list to check
*
* Returns: True if the list has a cycle, False if it doesn't*/
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	/* If the list is empty, it doesn't have a cycle*/
	if (!list)
		return (0);

	/* Use slow and fast pointers to traverse the list*/
	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	/* If slow and fast pointers meet, there is a cycle*/
		if (slow == fast)
			return (1);
	}

	/*NO cycle found*/
	return (0);
}
