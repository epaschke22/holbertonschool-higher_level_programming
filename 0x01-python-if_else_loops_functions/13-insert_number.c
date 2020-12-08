#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * listint_len - returns the number of elements in linked
 * @h: list to prtinf from
 * Return: number of elements
 */
size_t listint_len(const listint_t *h)
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
 * add_nodeint - adds node to beginning a list
 * @head: pointer to head of list
 * @n: element to put in new node
 * Return: adress to element
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = n;
	new->next = *head;
	*head = new;
	return (*head);
}

/**
 * findidx - finds the index based on the passed value
 * @head: the linked list to look through
 * @num: the value to find the index
 * Return: always 0
 */
int findidx(listint_t *head, int num)
{
	int idx = 0;

	while (head != NULL)
	{
		if (num < head->n)
			break;
		head = head->next;
		idx++;
	}
	return (idx);

}

/**
 * insert_nodeint - returns the nth node of a list
 * @head: list to look through
 * @number: the value to add to the new node
 * Return: listint node added
 */
listint_t *insert_nodeint(listint_t **head, int number)
{
	listint_t *temp, *new, *tmphead;
	unsigned int len, count = 0;

	if (head == NULL)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->number = number;
	tmphead = *head;
	len = listint_len(tmphead);
	idx = findidx(tmphead, number);
	if (idx == 0)
		return (add_nodeint(head, number));
	if (idx == len)
		return (add_nodeint_end(head, number));
	while (tmphead != NULL)
	{
		if (count == idx - 1)
		{
			temp = tmphead->next;
			tmphead->next = new;
			new->next = temp;
			return (new);
		}
		count++;
		tmphead = tmphead->next;
	}
	free(new);
	return (NULL);
}
