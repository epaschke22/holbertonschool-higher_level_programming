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
	listint_t *tmphead;
	size_t len1, len2 = 0;

	tmphead = *head;
	if (head == NULL)
		return 0;
	if (*head == NULL || tmphead->next == NULL)
		return (1);
	for (len2 = 0; tmphead != NULL; len2++)
		tmphead = tmphead->next;
	len2--;
	len2 *= 2;
	tmphead = *head;
    for (len1 = 0; len1 <= len2; len1 += 2)
	{
		if (tmphead[len1].n != tmphead[len2].n)
			return (0);
		len2 -= 2;
	}
    return (1);
}
