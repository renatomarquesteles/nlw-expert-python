git init

pip3 install virtualenv

https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/

Creates the virtualenv
py -m venv .venv

Allows scripts to run on windows
Set-ExecutionPolicy RemoteSigned

Runs the virtualenv script
.venv\Scripts\activate
or
Ctrl+Shift+P > Python: Select Interpreter

(.venv)
pip3 install pylint

pylint --generate-rcfile > .pylintrc
