#include "lists.h"
/**
 * insert_node - insert a node at a given position
 * @head: head of the list
 * @number: number to insert
 * Return: listint_t*
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *new, *previous = NULL;

	if (head == NULL)
		return (NULL);
	current = *head;
	while (current != NULL)
	{
		if (current->n > number)
		{
			new = malloc(sizeof(listint_t));
			if (new == NULL)
				return (NULL);
			if (previous != NULL)
				previous->next = new;
			new->next = current;
			if (current == *head)
				*head = new;
			new->n = number;
			return (new);
		}
		previous = current;
		current = current->next;
	}
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	if (*head == NULL)
		*head = new;
	else
		previous->next = new;
	new->next = NULL;
	new->n = number;
	return (new);
}