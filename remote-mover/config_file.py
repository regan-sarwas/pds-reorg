# -*- coding: utf-8 -*-
"""
A collection of configuration properties.

WARNING: This file, while intended to be edited by the user, is part of the
source code of this application.  If edited incorrectly the application may
crash or misbehave in unexpected ways.

ALWAYS TEST AFTER MAKING CHANGES TO THIS FILE.
"""

from __future__ import absolute_import, division, print_function, unicode_literals

# Path to the moves database.
# https://github.com/AKROGIS/MapFixer for the definition of the moves database.
# Production:
# MOVES_DB = r"\\inpakrovmdist\GISData\GIS\ThemeMgr\DataMoves.csv"
# Testing:
MOVES_DB = "test/moves.csv"

# Remote server X drive path: UNC path or symbolic link to location where moves are to occur.
# Production:
# MOUNT_POINT = r"E:\XDrive\RemoteServers"
# Testing:
MOUNT_POINT = "test/servers"
