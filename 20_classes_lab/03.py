"""
Following code assumes a class named Widget that depends on
other widgets
Widget ctor takes a name, and function 
add_dependency(depends)
marks widget as depends on all widgets in "depends" list

When building a widget, you need to first build all the widgets it
depends on.

Implement widget so the following code works
"""

class Widget(object):

    def __init__(self, name):
        self._name = name
        self._dependencies = []
        self._is_built = False

    def add_dependency(self, *widgets):
        self._dependencies.extend(widgets)

    def build(self):
        if (self._is_built): return

        for dep in self._dependencies:
            dep.build()
        print self._name
        
        self._is_built = True

luke    = Widget("Luke")
hansolo = Widget("Han Solo")
leia    = Widget("Leia")
yoda    = Widget("Yoda")
padme   = Widget("Padme Amidala")
anakin  = Widget("Anakin Skywalker")
obi     = Widget("Obi-Wan")
darth   = Widget("Darth Vader")
_all    = Widget("All")


luke.add_dependency(hansolo, leia, yoda)
leia.add_dependency(padme, anakin)
obi.add_dependency(yoda)
darth.add_dependency(anakin)

_all.add_dependency(luke, hansolo, leia, yoda, padme, anakin, obi, darth)
_all.build()
