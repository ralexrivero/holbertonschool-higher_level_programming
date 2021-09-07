#include "lists.h"
/**
 * check_cycle - check if a list has a cycle
 * @list: list to check 
 * Return: 0 if there is no cycle, 1 if there is a cycle 
 */
int check_cycle(listint_t *list)
{
        listint_t *slow = list;
        listint_t *fast = list;

        while (slow && fast && fast->next)
        {
                slow = slow->next;
                fast = fast->next->next;
                if (slow == fast)
                        return (1);
                else
                        return (0);
        }
        return (0);
}