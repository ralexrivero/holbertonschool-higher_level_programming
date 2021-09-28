#include <Python.h>
#include <bytesobject.h>
#include <floatobject.h>
#include <listobject.h>
#include <math.h>
#include <object.h>


/**
 * print_python_bytes - printPython bytes objects info
 * @p: pointer to PyObject
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t i, lim;
	PyBytesObject *b;
	PyVarObject *o;

	b = (PyBytesObject *)p;
	o = (PyVarObject *)p;
	puts("[.] bytes object info");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		puts("  [ERROR] Invalid Bytes Object");
		fflush(stdout);
		return;
	}
	printf("  size: %ld\n", o->ob_size);
	printf("  trying string: ");
	for (i = 0; i < o->ob_size && b->ob_sval[i] != '\0'; i++)
		putchar(b->ob_sval[i] > 0 ? b->ob_sval[i] : '?');
	putchar('\n');
	lim = o->ob_size + 1 > 10 ? 10 : o->ob_size + 1;
	printf("  first %ld bytes: ", lim);
	for (i = 0; i < lim; i++)
	{
		printf("%02hx", (unsigned char)b->ob_sval[i]);
		if (i < lim - 1)
			putchar(' ');
	}
	putchar('\n');
	fflush(stdout);
}
/**
 * print_python_float - print Python float objects info
 * @p: pointer to a PyFloatObject
 * 
 */
void print_python_float(PyObject *p)
{
	char *repr;
	PyFloatObject *f;

	f = (PyFloatObject *)p;
	puts("[.] float object info");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		puts("  [ERROR] Invalid Float Object");
		fflush(stdout);
		return;
	}
	repr = PyOS_double_to_string(f->ob_fval, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", repr);
	PyMem_Free(repr);
	fflush(stdout);
}
/**
 * print_python_list - print Python list objects info
 * @p: pointer to PyListObject (cast as PyObject)
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t i;
	PyListObject *l;
	PyVarObject *o;

	l = (PyListObject *)p;
	o = (PyVarObject *)p;
	puts("[*] Python list info");
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		puts("  [ERROR] Invalid List Object");
		fflush(stdout);
		return;
	}
	printf("[*] Size of the Python List = %ld\n", o->ob_size);
	printf("[*] Allocated = %ld\n", l->allocated);
	for (i = 0; i < o->ob_size; i++)
	{
		printf("Element %ld: %s\n", i, l->ob_item[i]->ob_type->tp_name);
		if (strcmp(l->ob_item[i]->ob_type->tp_name, "bytes") == 0)
			print_python_bytes(l->ob_item[i]);
		else if (strcmp(l->ob_item[i]->ob_type->tp_name, "float") == 0)
			print_python_float(l->ob_item[i]);
	}
	fflush(stdout);
}
