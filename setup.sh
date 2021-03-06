#bin/bash
clear
echo
echo "        Setting up first time installation just wait .....!"
echo
cd $HOME
pkg install python -y
pkg install python2 -y
pkg install git -y
pip inatall requests
pip install mechanize
pip install bs4
cd $HOME/getUser
python Fuck.py
