#!/usr/bin/env python

import glob
import os
import sys

from setuptools import setup, find_packages

extra_deps = []

if os.name == "nt":
    extra_deps = [
        "pycrypto"  # used to check the activation keys
    ]

setup(
    name="paperwork",
    # if you change the version, don't forget to
    # * update the download_url in this file
    # * update the ChangeLog file
    # * update AUTHORS
    # * change it also in
    #   paperwork/frontend/aboutdialog/aboutdialog.glade
    # * change it also in
    #   paperwork/frontend/mainwindow/__init__.py:__version__
    # * update the dependency version on paperwork-backend
    # * update the public key in
    #   paperwork/frontend/activation/__init__.py:check_activation_key()
    #   if required
    version="1.2",
    description=(
        "Using scanner and OCR to grep dead trees the easy way (Linux only)"
    ),
    long_description="""Paperwork is a tool to make papers searchable.

The basic idea behind Paperwork is "scan & forget" : You should be able to
just scan a new document and forget about it until the day you need it
again.
Let the machine do most of the work.

Main features are:
- Scan
- Automatic orientation detection
- OCR
- Indexing
- Document labels
- Automatic guessing of the labels to apply on new documents
- Search
- Keyword suggestions
- Quick edit of scans
- PDF support
    """,
    keywords="scanner ocr gui",
    url="https://github.com/jflesch/paperwork",
    download_url=("https://github.com/jflesch/paperwork"
                  "/archive/1.2.tar.gz"),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: X11 Applications :: GTK",
        "Environment :: X11 Applications :: Gnome",
        "Intended Audience :: End Users/Desktop",
        ("License :: OSI Approved ::"
         " GNU General Public License v3 or later (GPLv3+)"),
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Topic :: Multimedia :: Graphics :: Capture :: Scanners",
        "Topic :: Multimedia :: Graphics :: Graphics Conversion",
        "Topic :: Scientific/Engineering :: Image Recognition",
        "Topic :: Text Processing :: Filters",
        "Topic :: Text Processing :: Indexing",
    ],
    license="GPLv3+",
    author="Jerome Flesch",
    author_email="jflesch@openpaper.work",
    packages=find_packages(),
    data_files=[
        # css file
        (
            'share/paperwork',
            [
                'paperwork/frontend/application.css',
            ]
        ),

        # glade files
        (
            'share/paperwork/aboutdialog',
            [
                'paperwork/frontend/aboutdialog/aboutdialog.glade',
            ]
        ),
        (
            'share/paperwork/activation',
            [
                'paperwork/frontend/activation/activationdialog.glade',
            ]
        ),
        (
            'share/paperwork/diag',
            [
                'paperwork/frontend/diag/diagdialog.glade',
            ]
        ),
        (
            'share/paperwork/searchdialog',
            [
                'paperwork/frontend/searchdialog/searchdialog.glade',
            ]
        ),
        (
            'share/paperwork/settingswindow',
            [
                'paperwork/frontend/settingswindow/settingswindow.glade',
            ]
        ),
        (
            'share/paperwork/import',
            [
                'paperwork/frontend/import/importaction.glade',
                'paperwork/frontend/import/importfileselector.glade',
            ]
        ),
        (
            'share/paperwork/labeleditor',
            [
                'paperwork/frontend/labeleditor/labeleditor.glade',
            ]
        ),
        (
            'share/paperwork/mainwindow',
            [
                'paperwork/frontend/mainwindow/appmenu.xml',
            ]
        ),
        (
            'share/paperwork/mainwindow',
            [
                'paperwork/frontend/mainwindow/export.glade',
                'paperwork/frontend/mainwindow/mainwindow.glade',
            ]
        ),
        (
            'share/paperwork/multiscan',
            [
                'paperwork/frontend/multiscan/multiscan.glade',
            ]
        ),

        # translations
        ('share/locale/fr/LC_MESSAGES',
         ['locale/fr/LC_MESSAGES/paperwork.mo']),
        ('share/locale/de/LC_MESSAGES',
         ['locale/de/LC_MESSAGES/paperwork.mo']),

        # documentation
        ('share/paperwork/doc',
         glob.glob('doc/*.pdf')),

        # pics
        ('share/paperwork',
         ['data/bad.png']),
        ('share/applications',
         ['data/paperwork.desktop']),

        ('share/icons/hicolor/scalable/apps',
         ['data/paperwork.svg', 'data/paperwork_halo.svg']),
        ('share/icons/hicolor/16x16/apps',
         ['data/16/paperwork.png']),
        ('share/icons/hicolor/22x22/apps',
         ['data/22/paperwork.png']),
        ('share/icons/hicolor/24x24/apps',
         ['data/24/paperwork.png']),
        ('share/icons/hicolor/32x32/apps',
         ['data/32/paperwork.png']),
        ('share/icons/hicolor/36x36/apps',
         ['data/36/paperwork.png']),
        ('share/icons/hicolor/42x42/apps',
         ['data/42/paperwork.png']),
        ('share/icons/hicolor/48x48/apps',
         ['data/48/paperwork.png']),
        ('share/icons/hicolor/64x64/apps',
         ['data/64/paperwork.png']),
        ('share/icons/hicolor/72x72/apps',
         ['data/72/paperwork.png']),
        ('share/icons/hicolor/96x96/apps',
         ['data/96/paperwork.png']),
        ('share/icons/hicolor/128x128/apps',
         ['data/128/paperwork.png']),
        ('share/icons/hicolor/160x160/apps',
         ['data/160/paperwork.png']),
        ('share/icons/hicolor/192x192/apps',
         ['data/192/paperwork.png']),
        ('share/icons/hicolor/256x256/apps',
         ['data/256/paperwork.png']),
        ('share/icons/hicolor/512x512/apps',
         ['data/512/paperwork.png']),
        ('share/paperwork',
         ['data/paperwork_100.png']),
        ('share/paperwork',
         ['data/magic_colors.png']),
        ('share/paperwork',
         ['data/waiting.png']),
    ],
    entry_points={
        'gui_scripts': [
            'paperwork = paperwork.paperwork:main',
        ]
    },
    install_requires=[
        "python-Levenshtein",
        "Pillow",
        "pycountry",
        "pyinsane2",
        "pyocr >= 0.3.0",
        "pypillowfight",
        "termcolor",  # used by paperwork-chkdeps
        "paperwork-backend >= 1.2",
        # paperwork-chkdeps take care of all the dependencies that can't be
        # handled here. For instance:
        # - Dependencies using gobject introspection
        # - Dependencies based on language (OCR data files, dictionnaries, etc)
        # - Dependencies on data files (icons, etc)
    ] + extra_deps
)

print("============================================================")
print("============================================================")
print("||                       IMPORTANT                        ||")
print("|| Please run 'paperwork-shell chkdeps paperwork_backend' ||")
print("||        and 'paperwork-shell chkdeps paperwork'         ||")
print("||        to find any missing dependency                  ||")
print("============================================================")
print("============================================================")
