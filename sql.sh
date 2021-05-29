#!/bin/bash

printf "checkout master(SQL) ...\n"
git checkout master


printf "creating virtual env ATTACK ...\n"
python3 -m venv ATTACK


printf "activating ATTACK env ...\n"
. ATTACK/bin/activate

printf "installing Flask ...\n"
pip3 install FLASK

export FLASK_APP=iq
flask initdb

printf "launching HMS ...\n"
flask run



