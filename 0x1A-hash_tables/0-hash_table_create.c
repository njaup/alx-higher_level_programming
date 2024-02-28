#include <stdio.h>
#include <stdlib.h>
#include "hash_tables.h"

#define INITIAL_CAPACITY 10

/**
 * hash_table_create - Creates a hash table.
 * @size: The size of the array.
 * Return: If an error occurs - NULL.
 *         Otherwise - a pointer to the new hash table.
 */
hash_table_t *hash_table_create(unsigned long int size)
{
	if (size == 0)
	{
		return (NULL);
	}

	hash_table_t *hash_table = malloc(sizeof(hash_table_t));

	if (hash_table == NULL)
	{
		return (NULL);
	}

	hash_table->size = size;
	hash_table->array = malloc(size * sizeof(void *));
	if (hash_table->array == NULL)
	{
		free(hash_table);
		return (NULL);
	}

	for (unsigned long int i = 0; i < size; ++i)
	{
		hash_table->array[i] = NULL;
	}

	return (hash_table);
}
/**
 * main - Executes the program
 * Return: 0.
 */
int main(void)
{
	hash_table_t *my_hash_table = hash_table_create(INITIAL_CAPACITY);

	if (my_hash_table == NULL)
	{
		printf("Failed to create hash table\n");
		return (1);
	}

	free(my_hash_table->array);
	free(my_hash_table);

	return (0);
}
