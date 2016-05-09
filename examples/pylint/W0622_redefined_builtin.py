"""pylint: Attempting to redefine built-in %r, or function override a build-in.

"""

from __future__ import print_function
import builtins

def new_print(var):
    builtins.print("New print statement!")

print = new_print # Overrides print function.