#!/bin/bash
python3 --version
python3 -m venv myenv
source myenv/bin/activate
which python3
pip3 install -r requirements.txt
sudo apt update
sudo apt install apt
sudo apt install curl wget
wget http://ftp.us.debian.org/debian/pool/main/a/apt/apt_2.2.4_amd64.deb
sudo dpkg -i apt_2.2.4_amd64.deb
sudo apt --fix-broken install
apt-get --version

sudo apt-get install libsqlite3-dev
wget https://www.python.org/ftp/python/3.10.12/Python-3.10.12.tgz
tar xzf Python-3.10.12.tgz
cd Python-3.10.12
./configure --enable-loadable-sqlite-extensions
make
sudo make install

python3 manage.py runserver