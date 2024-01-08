#include <object.h>
#include <listobject.h>
#include <Python.h>
/**
*print_python_list_info - function to print python basic info
*@p: - python object param
*Return: - returns nothing
*/
void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	int i;
	PyListObject *item = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", item->allocated);

	for (i = 0; i < size; i++)
	{
		printf("Element %i: %s\n", i, Py_TYPE(item->ob_item[i])->tp_name);
	}
}
