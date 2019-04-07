# -*- coding: utf-8 -*-
"""
/***************************************************************************
 QCopycanvas
                                 A QGIS plugin
 This tool can be used to copy the map canvas and place it in the clipboard.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2019-04-07
        copyright            : (C) 2019 by Marios S. Kyriakou, KIOS Research and Innovation Center of Excellence (KIOS CoE)
        email                : mariosmsk@gmail.com
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
    """Load QCopycanvas class from file QCopycanvas.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .QLocklayers import QLocklayers
    return QLocklayers(iface)
