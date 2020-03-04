#!/bin/bash
echo source .venv/Scripts/activate
python -m venv .venv
git config --global user.name "youaresoroman"
git config --global user.email "qfaipkookw@groupoffice.ch"
python -m pip install --upgrade pip
pip -V
pip install beautifulsoup4
pip install requests