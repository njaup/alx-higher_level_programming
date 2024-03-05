#include <Python.h>
#include <stdio.h>

/**
 * print_python_string - Create a function that prints Python strings.
 * @p: A PyObject string object.
 */
void print_python_string(PyObject *p)
{
	if (!PyUnicode_Check(p))
	{
		printf("[ERROR] Invalid Python string\n");
		return;
	}
	
	Py_ssize_t length;
	const char *utf8_str = PyUnicode_AsUTF8AndSize(p, &length);
	if (!utf8_str)
	{
		printf("[ERROR] Failed to convert Python string to UTF-8\n");
		return;
	}
	
	printf("String data: %s\n", utf8_str);
	printf("Length: %zd\n", length);
}
