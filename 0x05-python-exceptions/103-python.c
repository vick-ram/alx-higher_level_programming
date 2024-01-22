#include <Python.h>
#include <stdio.h>
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);
/**
*print_python_list - prints python list
*@p: - pyobject type
*Return: - returns nothing
*/
void print_python_list(PyObject *p)
{
	PyObject *item;
	Py_ssize_t size = PyList_Size(p), i;
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;

	if (!PyList_Check(p))
	{
		fprintf(stderr, "[*] Python list info\n
		[ERROR] Invalid List Object\n");
		return;
	}
	printf("[*] Python list info\n[*] Size of the Python
		List = %zd\n[*] Allocated = %zd\n", size, allocated);
	for (i = 0; i < size; ++i)
	{
		item = PyList_GetItem(p, i);
		printf("Element %zd: ", i);
		if (PyBytes_Check(item))
		{
			printf("bytes\n");
			print_python_bytes(item);
		}
		else if (PyFloat_Check(item))
		{
			printf("float\n");
			print_python_float(item);
		}
		else if (PyLong_Check(item) && PyLong_CheckExact(item))
			printf("int\n");
		else if (PyTuple_Check(item))
			printf("tuple\n");
		else if (PyList_Check(item))
		{
			printf("list\n");
			print_python_list(item);
		}
		else if (PyUnicode_Check(item))
			printf("str\n");
	}
}
/**
*print_python_bytes - prints python bytes
*@p: - pyobject type
*Return: - returns nothing
*/
void print_python_bytes(PyObject *p)
{
	char *str;

	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "[.] bytes object info\n  [ERROR] Invalid Bytes Object\n");
		return;
	}
	Py_ssize_t size = PyBytes_Size(p);
	str = PyBytes_AsString(p);
	printf("[.] bytes object info\n  size: %zd\n  trying string: %s\n  first %d bytes: ", size, str, (int)fmin(size, 10));
	for (Py_ssize_t i = 0; i < fmin(size, 10); ++i)
	{
		printf("%02x ", (unsigned char)str[i]);
	}
	printf("\n");
}
/**
*print_python_float - prints python float
*@p: - pyobject type
*Return: -returns nothing
*/
void print_python_float(PyObject *p)
{
	double value;

	if (!PyFloat_Check(p))
	{
		fprintf(stderr, "[.] float object info\n  [ERROR] Invalid Float Object\n");
	return;
	}
	value = PyFloat_AsDouble(p);
	printf("[.] float object info\n  value: %f\n", value);
}
