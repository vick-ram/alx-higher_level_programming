#include "lists.h"
/**
*is_palindrome - checks if linked list is palindrome
*@head: first list element
*Return: - returns 0 if not and 1 if is
*/
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head;
	listint_t *prev = NULL, *temp, *mid = NULL;
	int is_palindrome = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		temp = slow->next;
		slow->next = prev;
		prev = slow;
		slow = temp;
	}
	mid = (fast == NULL) ? prev : slow;
	while (prev != NULL && mid != NULL)
	{
		if (prev->n != mid->n)
		{
			is_palindrome = 0;
			break;
		}
		prev = prev->next;
		mid = mid->next;
	}
	return (is_palindrome);
}
