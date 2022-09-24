#!/bin/bash
# First checks whether user has python3 installed
if [[ -x "$(command -v python3)" ]]
then
    pyv="$(python3 -V)"
    if [[ $pyv == "Python 3"* ]]
    then
    # installs virtual environment, then required packages, then runs the application
        git clone https://github.com/Coder-Nicki/times_tables_challenge/
        python3 -m venv .venv
        pip install -r src/requirements.txt
        python3 src/main.py
    fi 
else
    echo "You don't have python3, go get it! You can find it at https://www.python.org/downloads/" >&2
fi
