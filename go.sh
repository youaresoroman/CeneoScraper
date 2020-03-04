#!/bin/bash
python -m venv .venv
source .venv/Scripts/activate
python -m pip install --upgrade pip
pip -V
git config --global user.name "youaresoroman"
git config --global user.email "qfaipkookw@groupoffice.ch"