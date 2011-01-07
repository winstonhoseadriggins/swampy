#!/usr/bin/python

import inspect
import Lumpy
lumpy = Lumpy.Lumpy()
lumpy.make_reference()

stack = inspect.stack()
for tup in stack:
    frame, filename, lineno, func, lines, index = tup
    arg_names, args, kwds, locals = inspect.getargvalues(frame)

lumpy.object_diagram()
