# -*- coding: utf-8 -*-
"""
Compares Theme Manager against file system and reports on
1) Themes (layer files) in TM database that are not in the TM filesystem
2) Themes (layer files) in TM filesystem that are not in the TM database
"""
from __future__ import absolute_import, division, print_function, unicode_literals

import csv
import os

import csv23


tm_filesystem = r"X:\GIS\ThemeMgr"
tm_database = r"data\TM_20171206.csv"

unique_themes = set([])
with csv23.open(tm_database, "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # ignore the header
    for row in csv_reader:
        row = csv23.fix(row)
        theme = row[3]
        unique_themes.add(theme)

print("Missing Themes:")
for theme in sorted(unique_themes):
    if theme and not os.path.exists(theme):
        print("  " + theme)

print("Extra Themes:")
for root, dirs, files in os.walk(tm_filesystem):
    if ".git" in dirs:
        dirs.remove(".git")
    for name in files:
        base, ext = os.path.splitext(name)
        if ext.lower() != ".xml":
            filepath = os.path.join(root, name)
            if filepath not in unique_themes:
                print("  " + filepath)
