#include "lists.h"
/**
* reverse - helper function to reverse a list
*@head: - first node
*Return: - returns a list
*/
listint_t *reverse(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *curr = head, *next;

	while (curr != NULL)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}
	return (prev);
}
/**
*is_palindrome - checks if linked list is palindrome
*@head: first list element
*Return: - returns 0 if not and 1 if is
*/
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head;
	listint_t *first, *second;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;
	}
	if (fast != NULL)
	{
		slow = slow->next;
	}
	second = reverse(slow);
	first = *head;
	while (second != NULL)
	{
		if (first->n != second->n)
			return (0);
		first = first->next;
		second = second->next;
	}
	return (1);
}
