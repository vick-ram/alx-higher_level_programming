#include <Python.h>

void print_python_list(PyObject *p) {
    Py_ssize_t i, size;
    PyListObject *list;
    PyObject *item;

    if (!PyList_Check(p)) {
        printf("[*] Python list info\n  [ERROR] Invalid List Object\n");
        return;
    }

    list = (PyListObject *)p;
    size = PyList_Size(p);

    printf("[*] Python list info\n[*] Size of the Python List = %ld\n[*] Allocated = %ld\n", size, list->allocated);

    for (i = 0; i < size; i++) {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

void print_python_bytes(PyObject *p) {
    Py_ssize_t size, i;
    char *str;

    if (!PyBytes_Check(p)) {
        printf("[.] bytes object info\n  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    str = PyBytes_AsString(p);

    printf("[.] bytes object info\n  size: %ld\n  trying string: %s\n", size, str);
    printf("  first %ld bytes: ", (size < 10) ? size : 10);
    for (i = 0; i < size && i < 10; i++) {
        printf("%02hhx%c", str[i], (i + 1 < size && i + 1 < 10) ? ' ' : '\n');
    }
}

void print_python_float(PyObject *p) {
    if (!PyFloat_Check(p)) {
        printf("[.] float object info\n  [ERROR] Invalid Float Object\n");
        return;
    }

    printf("[.] float object info\n  value: %f\n", PyFloat_AS_DOUBLE(p));
}
