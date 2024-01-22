#include <Python.h>
#include <stdio.h>
/**
*print_python_bytes - prints python bytes
*@p: - pyobject type
*Return: - returns nothing
*/
void print_python_bytes(PyObject *p)
{
	char *str;
	long int size, i, max_bytes;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = PyBytes_Size(p);
	str = PyBytes_AsString(p);
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);
	max_bytes = size + 1 > 10 ? 10 : size + 1;
	printf("  first %ld bytes: ", max_bytes);
	for (i = 0; i < max_bytes; i++)
		printf("%02hhx%s", str[i], i + 1 < max_bytes ? " " : "");
	printf("\n");
}
/**
*print_python_float - prints python floats
*@p: - pyobject type param
*Return: - returns nothing
*/
void print_python_float(PyObject *p)
{
	double value;

	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	value = PyFloat_AsDouble(p);
	printf("  value: %g\n", value);
}
/**
*print_python_list - prints python list
*@p: - pyobject param
*Return: - returns nothing
*/
void print_python_list(PyObject *p)
{
	long int size, alloc, i;
	PyObject *item;

	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	size = PyList_GET_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);
	for (i = 0; i < size; i++)
	{
		item = PyList_GET_ITEM(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
		else if (PyFloat_Check(item))
			print_python_float(item);
	}
}
