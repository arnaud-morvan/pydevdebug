PydevDebugPlugin
================

Configuration
-------------

Add pydevd to your python path :

In QGIS **Settings** menu, **Options** sub-menu, **System** tab, **Environment** fieldset,
activate **Use custom variables** and add a line with:

- *Apply* set to **Append**;
- *Variable* set to **PYTHONPATH**;
- *Value* set to your *pysrc* path prefixed by a semicolon.

Exemple:

Append | PYTHONPATH | :/home/amorvan/.eclipse/org.eclipse.platform_3.8_155965261/plugins/org.python.pydev_3.0.0.201311051910/pysrc/

Usage
-----

- Run *Eclipse* and click on *start the PyDev server* in the debug perspective;
- Run *QGIS* and click on **Start pydevd debugging**;
- Place a break point in a source file;
- Execute the code which contains the break point.

