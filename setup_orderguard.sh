# Create a new directory for the project
mkdir OrderGuardCommandHub

cd OrderGuardCommandHub

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install Django
pip install Django

# Create a new Django project
django-admin startproject OrderGuard

cd OrderGuard

# Create a new Django app for each module (ERP, Project Management, HR, etc.)
django-admin startapp ERP
django-admin startapp ProjectManagement
django-admin startapp HR
django-admin startapp RealTimeCommunication
django-admin startapp Geospatial

# Install additional packages
pip install django-allauth django-channels django-rest-framework django-rbac qgis-server-api

# Initialize Git repository
git init

git add .

git commit -m 'Initial project setup'

# Add your GitHub repository as a remote
git remote add origin [Your GitHub Repository URL]

git push -u origin master