# The sys module.
#
#  The “sys.path” list is initialized from the PYTHONPATH environment variable. Is it possible to change it from within
# Python? If so, does it affect where Python looks for module files? Run some interactive tests to find it out.

#Answer: Yes, we can. Firstiful Python looks in initial file __init__.py
#Then we can proclaim where Python must look for modules via directive
#In this sample i've created module imported_module.py in subdirectory module_test
#and from there imported variable imported_var


from module_test.imported_module import imported_var

print(imported_var)


