#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked-list contains a cycle.
 * @list: Singly-linked-list.
 * Return: 0 If no cycle found, or 1 if there is a cycle found.
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL || list->next == NULL)
		return (0);

	slow = list->next;
	fast = list->next->next;

	while (slow && fast && fast->next)
	{
		if (slow == fast)
			return (1);

		slow = slow->next;
		fast = fast->next->next;
	}

	return (0);
}
