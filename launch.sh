#!/bin/bash

printf "creating virtual env LOCAL ...\n"
python3 -m venv LOCAL


printf "activating LOCAL env ...\n"
. LOCAL/bin/activate

printf "installing Flask ...\n"
pip3 install FLASK

export FLASK_APP=iq

printf "launching HMS ...\n"
flask run












