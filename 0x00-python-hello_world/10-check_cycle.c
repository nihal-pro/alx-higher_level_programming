#include "lists.h"
/**
 * check_cycle - a function that checks if a singly linked list
 *               has a cycle in it
 * @list: a pointer to linked list
 * Return:0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *check = list, *check_next = list;

	if (!list)
		return (0);
	while (check_next && check_next->next)
	{
		check = check->next, check_next = check_next->next->next;
		if (check == check_next)
			return (1);
	}
	return (0);
}
