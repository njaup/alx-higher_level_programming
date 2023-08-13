#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: check linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr2 = list;
	listint_t *ptr1 = list;

	while (ptr1 != NULL && ptr1->next != NULL)
	{
		ptr2 = ptr2->next;
		ptr1 = ptr1->next->next;

		if (ptr2 == ptr1)
		{
			return (1);
		}
	}
	return (0);
}
