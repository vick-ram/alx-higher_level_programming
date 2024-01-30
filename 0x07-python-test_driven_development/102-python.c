#include <Python.h>
/**
*print_python_string - prints python object
*@p: - python object param
*Return: - returns nothing
*/
void print_python_string(PyObject *p)
{
	if (!PyUnicode_Check(p))
	{
		fprintf(stderr, "[.] string object info\n");
		fprintf(stderr, "  [ERROR] Invalid String Object\n");
		return;
	}
	Py_ssize_t length = PyUnicode_GET_LENGTH(p);
	const char *type = PyUnicode_IS_COMPACT_ASCII(p) ? "compact ascii" : "compact unicode object";
	const wchar_t *value = PyUnicode_AS_UNICODE(p);
	fprintf(stdout, "[.] string object info\n");
	fprintf(stdout, "  type: %s\n", type);
	fprintf(stdout, "  length: %zd\n", length);
	if (PyUnicode_IS_COMPACT_ASCII(p))
	{
		fprintf(stdout, "  value: %s\n", PyUnicode_AsUTF8(p));
	}
	else
	{
		fprintf(stdout, "  value: %ls\n", value);
	}
}

/**
*main - main entry point require to build library
*Return: - returns nothing
*/
int main(void)
{
	return 0;
}
