# -*- coding: utf-8 -*-
"""
/***************************************************************************
 PydevDebugPlugin
                                 A QGIS plugin
 Start pydevd debugging by calling settrace
                             -------------------
        begin                : 2014-09-16
        copyright            : (C) 2014 by Arnaud Morvan
        email                : arnaud.morvan@camptocamp.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load PydevDebugPlugin class from file PydevDebugPlugin.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .pydevdebug_plugin import PydevDebugPlugin
    return PydevDebugPlugin(iface)
