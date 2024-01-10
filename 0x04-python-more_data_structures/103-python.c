#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *element;

	printf("[*] Python list info\n");
	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		element = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);
		if (strcmp(Py_TYPE(element)->tp_name, "bytes") == 0)
		{
			printf("[.] bytes object info\n");
			printf("  size: %ld\n", PyBytes_Size(element));
			printf("  trying string: %s\n", PyBytes_AsString(element));
			printf("  first 10 bytes: ");
			for (Py_ssize_t j = 0; j < PyBytes_Size(element) && j < 10; j++)
			{
				printf("%02x ", (unsigned char)PyBytes_AsString(element)[j]);
			}
			printf("\n");
		}
	}
}
void print_python_bytes(PyObject *p)
{
	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("  size: %ld\n", PyBytes_Size(p));
	printf("  trying string: %s\n", PyBytes_AsString(p));
	rintf("  first 10 bytes: ");
	for (Py_ssize_t i = 0; i < PyBytes_Size(p) && i < 10; i++)
	{
		printf("%02x ", (unsigned char)PyBytes_AsString(p)[i]);
	}
	printf("\n");
}
