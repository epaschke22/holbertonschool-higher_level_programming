#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * list_len - returns the number of elements in linked
 * @h: list to prtinf from
 * Return: number of elements
 */
size_t list_len(const listint_t *h)
{
	int count = 0;

	while (h != NULL)
	{
		count++;
		h = h->next;
	}
	return (count);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: input list
 * Return: 1 if palindrome, else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *fronthead = *head, *backhead;
	size_t i, len1 = 0, len2 = 0;

	if (head == NULL)
		return 0;
	if (*head == NULL)
		return (1);
    if (fronthead->next == NULL)
        return (1);
    len2 = list_len(fronthead) - 1;

    while (len2 >= len1)
    {
        fronthead = *head;
        for (i = 0; i < len1; i++)
            fronthead = fronthead->next;
        backhead = *head;
        for (i = 0; i < len2; i++)
            backhead = backhead->next;
        if (fronthead->n != backhead->n)
            return (0);
        len1++;
        len2--;
    }
    return (1);
}
