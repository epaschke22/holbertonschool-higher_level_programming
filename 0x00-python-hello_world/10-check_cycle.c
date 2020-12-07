#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if there is a cycle in a single linked list
 * @listin_t: the list to check in
 * Return: 0 if there is no cycle, 1 if there is
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr1, *ptr2;

	ptr1 = list;
	ptr2 = list->next;

	while (ptr2 != NULL)
	{
		if (ptr1 == ptr2)
			return (1);
		ptr2 = ptr2->next;
		if (ptr1 == ptr2)
			return (1);
		if (ptr2 == NULL)
			break;
		ptr2 = ptr2->next;
		ptr1 = ptr1->next;
	}
	return (0);
}
