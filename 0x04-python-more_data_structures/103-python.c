#include <Python.h>
#include <stdio.h>
/**
* print_python_list - prints a python list
* @p: - pyobject type param
* Return: - returns nothing
*/
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i, j;
	PyObject *element;
	char *c;

	printf("[*] Python list info\n");
	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		element = PySequence_GetItem(p, i);
		printf("Element %ld: %s\n", i, ((PyObject *)element)->ob_type->tp_name);
		if (strcmp(((PyObject *)element)->ob_type->tp_name, "bytes") == 0)
		{
			printf("[.] bytes object info\n");
			printf("  size: %ld\n", PyBytes_Size(element));
			printf("  trying string: %s\n", PyBytes_AsString(element));
			printf("  first 10 bytes: ");
			c = PyBytes_AsString(element);
			for (j = 0; j < PyBytes_Size(element) && j < 10; j++)
			{
				printf("%02x ", (unsigned char)c[j]);
			}
			printf("\n");
		}
	}
}
/**
* print_python_bytes - prints python bytes
* @p: - pyobject type param
* Return: - returns nothing
*/
void print_python_bytes(PyObject *p)
{
	char *c;
	Py_ssize_t i;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("  size: %ld\n", PyBytes_Size(p));
	printf("  trying string: %s\n", PyBytes_AsString(p));
	printf("  first 10 bytes: ");
	c = PyBytes_AsString(p);
	for (i = 0; i < PyBytes_Size(p) && i < 10; i++)
	{
		printf("%02x ", (unsigned char)c[i]);
	}
	printf("\n");
}
