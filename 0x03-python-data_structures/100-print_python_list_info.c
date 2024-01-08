#include <object.h>
#include <listobject.h>
#include <python.h>
/**
*print_python_list_info - function to print python basic info
*@p: - python object param
*Return: - returns nothing
*/
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, allocated, i;
	PyObject *item;

	if (!PyList_Check(p))
	{
		PyErr_SerString(PyExc_TypeError, "Input must be a list.");
		return;
	}

	size = PyList_size(p);
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
