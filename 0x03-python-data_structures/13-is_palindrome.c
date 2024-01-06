#include "lists.h"
/**
*compare_and_reverse - a helper function to reverse
second half of a string and compare it with first
*@head: - first struct element
*@mid: - middle element
*Return: - returns reversed
*/
int compare_and_reverse(listint_t **head, listint_t *mid)
{
	listint_t *prev = NULL, *curr = mid, *next;
	int res = 1;
	listint_t *p1, *p2;

	while (curr != NULL)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}
	p1 = *head, p2 = prev;
	while (p1 != NULL && p2 != NULL)
	{
		if (p1->n != p2->n)
		{
			res = 0;
			break;
		}
		p1 = p1->next;
		p2 = p2->next;
	}
	curr = prev;
	while (curr != NULL)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}
	return (res);
}
/**
*is_palindrome - checks if linked list is palindrome
*@head: first list element
*Return: - returns 0 if not and 1 if is
*/
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head;
	listint_t *mid = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;
	}
	mid = (fast == NULL) ? slow : slow->next;
	return (compare_and_reverse(head, mid));
}
