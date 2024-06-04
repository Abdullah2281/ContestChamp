#!/bin/bash

# Activate virtual environment (if using one locally)
# This step would be skipped for Vercel deployments
# source myenv/bin/activate  # Replace 'myenv' with your virtualenv name

echo "Start Build"

echo "Started Venv"
# apt install python3.10-venv

which python
which pip

python3 -m venv my_env
source my_env/bin/activate

python3 --version

apt-get install libsqlite3-dev

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
