#include "lists.h"
/**
 *  * is_palindrome - checks if a singly linked list is a palindrome.
 *   * @head: pointer to firts node
 *    * Return: 0 if it is not a palindrome,
 *    1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
    int arr[3000], i = 0;
    listint_t *aux = *head;

    while (aux)
    {
        arr[i] = aux->n;
        aux = aux->next;
        i++;
    }
    aux = *head;
    i -= 1;
    while (aux)
    {
        if (arr[i] != aux->n)
        {
            return (0);
        }
        aux = aux->next;
        i--;
    }
    return (1);
}
