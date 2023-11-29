#include "lists.h"

/**
 * insert_node - a function that inserts a number into a
 *                  sorted singly linked list.
 * @head: a pointer to linked list.
 * @number : an integer .
 * Return: the address of new node or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *before_node, *after_node = NULL;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (!*head)
	{
		*head = new_node;
		return (*head);
	}

	if ((*head)->n >= number)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		before_node = *head;
		after_node = *head;
		after_node = after_node->next;
		while (number >= after_node->n && after_node->next != NULL)
		{
			before_node = before_node->next;
			after_node = after_node->next;
		}
		if (number <= after_node->n)
		{
			after_node = before_node->next;
			new_node->next = after_node;
			before_node->next = new_node;
		}
		else
			after_node->next = new_node;
	}
	return (*head);
}
