#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - checks linked list if it contains a cycle
 * @list: linked list
 *
 * Return: 1 if successful, 0 if it doesn't
 */

int check_cycle(listint_t *list)
{
	listint_t *stop = list;
	listint_t *run = list;

	if (!list)
		return (0);

	while (stop && run && run->next)
	{
		stop = stop->next;
		run = run->next->next;
		if (stop == run)
			return (1);
	}

	return (0);
}
