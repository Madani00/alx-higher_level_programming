#include "lists.h"

/**
 * check_cycle - function checks if a singly linked list has a cycle in it.
 * @list: pointer to the beginning of the node
 * Return: 0 if no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *sslow = NULL, *ffast =  NULL;

	if (list == NULL || list->next == NULL)
		return (0);
	sslow = list->next;
	ffast = list->next->next;

	while (sslow && ffast && ffast->next)
	{
		if (sslow == ffast)
			return (1);
		sslow = sslow->next;
		ffast = ffast->next->next;
	}

	return (0);
}
