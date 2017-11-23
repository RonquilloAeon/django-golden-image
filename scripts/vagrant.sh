#!/bin/bash

echo "Installing packages..."

# Python 3.5 setup
sudo apt-get install --reinstall software-properties-common -y > /dev/null
echo | sudo add-apt-repository ppa:fkrull/deadsnakes > /dev/null
sudo apt-get update > /dev/null
sudo apt-get install python3.5 -y > /dev/null

# Install packages
sudo apt-get install python3-pip python3.5-dev libffi-dev libpq-dev \
python-virtualenv libjpeg8 libjpeg62-dev libfreetype6 libfreetype6-dev build-essential -y > /dev/null

sudo apt-get install postgresql postgresql-contrib -y > /dev/null
sudo apt-get build-dep python-imaging -y > /dev/null

# Set up virtual environment and env variables
mkdir virtualenvs
sudo pip3 install virtualenv virtualenvwrapper > /dev/null
printf "# Virtualenv settings\n" >> ~ubuntu/.bash_profile
printf "export WORKON_HOME=~ubuntu/virtualenvs\n" >> ~ubuntu/.bash_profile
printf "export PROJECT_HOME=/vagrant\n" >> ~ubuntu/.bash_profile
printf "export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3\n" >> ~ubuntu/.bash_profile
printf "source /usr/local/bin/virtualenvwrapper.sh\n" >> ~ubuntu/.bash_profile

# Aliases
printf "\n# Useful Aliases:\n" >> ~ubuntu/.bash_profile
printf "alias runserver='python manage.py runserver 0.0.0.0:8000'\n" >> ~ubuntu/.bash_profile
printf "alias test='python manage.py test'\n" >> ~ubuntu/.bash_profile
printf "alias coveragetest='coverage run --source='apps' manage.py test'\n" >> ~ubuntu/.bash_profile
source ~ubuntu/.bash_profile > /dev/null

# Create virtualenv
mkvirtualenv --python=python3.5 backend > /dev/null

# Set up db
sudo -u postgres bash -c "psql -c \"CREATE USER djangodev WITH PASSWORD 'golden';\""
sudo -u postgres bash -c "psql -c \"CREATE DATABASE gdb  WITH OWNER djangodev;\""
sudo -u postgres bash -c "psql -c \"ALTER USER djangodev WITH SUPERUSER;\""

# Set up project deps
cd /vagrant
setvirtualenvproject
pip install -r requirements.txt > /dev/null
./scripts/setup.sh dev > /dev/null
./manage.py migrate

# Set virtualenvs owner
sudo chown -R ubuntu:ubuntu ~ubuntu/virtualenvs