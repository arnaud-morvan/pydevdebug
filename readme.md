PydevDebugPlugin
================

Configuration
-------------

Add *pydevd* to your python path.
To do so, in QGIS **Settings** menu, **Options** sub-menu, **System** tab, **Environment** fieldset,
activate **Use custom variables** and add a new line:

- set *Apply* to **Append**;
- set *Variable* to **PYTHONPATH**;
- set *Value* to **path to your pysrc folder prefixed by a semicolon**.

Exemple:

Append | PYTHONPATH | :/home/xxx/.eclipse/org.eclipse.platform_3.8_155965261/plugins/org.python.pydev_3.0.0.201311051910/pysrc/

Usage
-----

- Run *Eclipse*, go in the *debug* perspective, and click on *start the PyDev server*;
- Run *QGIS* and click on **Start pydevd debugging** in the *Plugins* toolbar;
- Place a break point in a source file;
- Execute the code which contains the break point.
