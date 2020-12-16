#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: input list
 * Return: 1 if palindrome, else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmpthead = *head;
	size_t i, count = 0, len1 = 0, len2 = 0;

	if (head == NULL)
		return 0;
	if (*head == NULL || tmpthead->next == NULL)
		return (1);
	while (tmpthead != NULL)
	{
		len2++;
		tmpthead = tmpthead->next;
	}
	len2--;
    for (len1 = 0; len1 <= len2; len1++)
	{
		if (head[len1]->n != head[len2]->n)
			return (0);
		len2--;
	}
    return (1);
}
