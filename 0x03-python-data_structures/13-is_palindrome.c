#include "lists.h"
/**
 * palindrome_h - recursively compares symetric entries in a linked list
 * @start: start of list, address manually iterated after comparison
 * @end: end of list, iterated through recursion
 *  Return: 1 if palindrome, 0 if not
 */
int palindrome_h(listint_t **start, listint_t *end)
{
int i = 1;

if (end->next != NULL)
i = palindrome_h(start, end->next);

if (i == 0)
return (0);

if ((*start)->n != end->n)
return (0);

*start = (*start)->next;

return (1);
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: linked list
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
listint_t *start;
listint_t *end;

if (head == NULL)
return (0);

if (*head == NULL)
return (1);

start = *head;
end = *head;

return (palindrome_h(&start, end));
}
