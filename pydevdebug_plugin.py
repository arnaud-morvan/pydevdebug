# -*- coding: utf-8 -*-
"""
/***************************************************************************
 PydevDebugPlugin
                                 A QGIS plugin
 Start pydevd debugging by calling settrace
                              -------------------
        begin                : 2014-09-16
        git sha              : $Format:%H$
        copyright            : (C) 2014 by Arnaud Morvan
        email                : arnaud.morvan@camptocamp.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import sys
import os.path
from PyQt4.QtCore import QSettings, QTranslator, qVersion, QCoreApplication
from PyQt4.QtGui import QAction, QIcon
# Initialize Qt resources from file resources.py
import resources_rc


try:
    import pydevd
except:
    pydevd = None


class PydevDebugPlugin:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'PydevDebug_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&PydevDebug')

    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('PydevDebugPlugin', message)

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        if pydevd is not None:
            action = QAction(QIcon(':/plugins/PydevDebug/icon.png'),
                             self.tr(u'Start pydevd debugging'),
                             self.iface.mainWindow())
            action.triggered.connect(self.startDebug)
            self.iface.addPluginToMenu(self.menu, action)
            self.iface.addToolBarIcon(action)

        action = QAction(QIcon(':/plugins/PydevDebug/icon.png'),
                         self.tr(u'Print settings'),
                         self.iface.mainWindow())
        action.triggered.connect(self.printSettings)
        self.iface.addPluginToMenu(self.menu, action)
        self.iface.addToolBarIcon(action)

        self.actions.append(action)

    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&PydevDebug'),
                action)
            self.iface.removeToolBarIcon(action)

    def startDebug(self):
        pydevd.settrace(suspend=False)

    def printSettings(self):
        for key in QSettings().allKeys():
            print key, QSettings().value(key)
