#include <stdlib.h>
#include <stdio.h>
#include <Python.h>

void print_python_list_info(PyObject *p)
{
	int i;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", item->allocated);
	for (i = 0; i < Py_Size(p); i++)
		printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
}
