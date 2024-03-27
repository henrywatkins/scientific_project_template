"""A one line summary of the module or program, terminated by a period.

Leave one blank line.  The rest of this docstring should contain an
overall description of the module or program.  Optionally, it may also
contain a brief description of exported classes and functions and/or usage
examples.

  Typical usage example:

  foo = ClassFoo()
  bar = foo.FunctionBar()
"""
# Standard library imports
import datetime
import os

# Third party imports
import numpy as np

# Local application imports
#from local_module import local_class
#from local_package import local_function


class Foo:
    """
    A class for doing something

    """
    def foo(self):
        """
        This is a reST style docstring

        :param param1: this is a first param
        :param param2: this is a second param
        :returns: this is a description of what is returned
        :raises keyError: raises an exception
        """
        pass

    def bar(self):
        """Descriptrion of method"""
        pass

def func(x):
    """
    This is a reST style docstring.

    :param param1: this is a first param
    :param param2: this is a second param
    :returns: this is a description of what is returned
    :raises keyError: raises an exception
    """
    pass
