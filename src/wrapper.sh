#!/bin/bash
# First checks whether user has python3 installed (python3 should also include pip)
if [[ -x "$(command -v python3)" ]]
then
    pyv="$(python3 -V)"
    if [[ $pyv == "Python 3"* ]]
    then
    # installs virtual environment, then required packages, then runs the application
        python3 -m venv .venv
        source .venv/bin/activate
        pip install -r requirements.txt
        python3 main.py
    fi 
else
    echo "You don't have python3, go get it! You can find it at https://www.python.org/downloads/" >&2
fi
