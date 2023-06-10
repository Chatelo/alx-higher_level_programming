#include <stddef.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to head of list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
    int len = 0, i = 0, j;
    int arr[100000];
    listint_t *current;

    if (head == NULL || *head == NULL)
        return (1);

    current = *head;
    while (current != NULL)
    {
        arr[len] = current->n;
        len++;
        current = current->next;
    }

    j = len - 1;
    while (i < j)
    {
        if (arr[i] != arr[j])
            return (0);
        i++;
        j--;
    }

    return (1);
}
