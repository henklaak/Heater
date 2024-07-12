#!/bin/bash

source .venv/bin/activate
pyside6-uic gui/GUI3.ui -o gui/ui_GUI3.py
pyside6-uic gui/Settings.ui -o gui/ui_Settings.py
