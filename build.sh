#!/bin/bash

# Activate virtual environment (if using one locally)
# This step would be skipped for Vercel deployments
# source myenv/bin/activate  # Replace 'myenv' with your virtualenv name

echo "Start Build"

echo "Started Venv"
# apt install python3.10-venv

python3 --version

python3 -m venv my_env
source my_env/bin/activate

python3 --version


wget https://www.sqlite.org/src/tarball/sqlite.tar.gz
tar xvfz sqlite.tar.gz
cd sqlite*/

# Configure, compile, and install SQLite
./configure
make
make install

cd ../

python3 -c "import sqlite3"



# Install dependencies (Vercel will handle this during deployment)
echo "Started my_env"

pip3 install -r requirements.txt

python3 manage.py runserver 3000
# Collect static files
# python manage.py collectstatic --noinput

# Migrate database (optional, may not be needed for Vercel if using migrations on deploy)
# python manage.py migrate


echo "Build completed successfully!"
