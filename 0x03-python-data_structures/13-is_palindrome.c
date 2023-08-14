#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: a pointer that points to the first node
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}
	listint_t *slow = *head, *fast = *head;
	listint_t *prev = NULL, *tmp;
	
	while (fast && fast->next)
	{
		fast = fast->next->next;
		tmp = slow->next;
		slow->next = prev;
		prev = slow;
		slow = tmp;
	}
	listint_t *left = prev;
	listint_t *right = (fast == NULL) ? slow : slow->next;
	
	while (left && right)
	{
		if (left->n != right->n)
		{
			return (0);
		}
		left = left->next;
		right = right->next;
	}
	return (1);
}
