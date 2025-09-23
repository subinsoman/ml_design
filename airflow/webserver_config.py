"""
Airflow webserver configuration to disable authentication
This configuration file disables login and makes everyone an admin automatically.
"""
import os
from flask_appbuilder.security.manager import AUTH_DB

# The SQLAlchemy connection string
SQLALCHEMY_DATABASE_URI = os.environ.get('AIRFLOW__DATABASE__SQL_ALCHEMY_CONN')

# Flask-WTF flag for CSRF
WTF_CSRF_ENABLED = True

# ----------------------------------------------------
# AUTHENTICATION CONFIG
# ----------------------------------------------------
# The authentication type
AUTH_TYPE = AUTH_DB

# Will allow user self registration
AUTH_USER_REGISTRATION = False

# The default user self registration role
AUTH_USER_REGISTRATION_ROLE = "Public"

# ----------------------------------------------------
# DISABLE AUTHENTICATION - EVERYONE IS ADMIN
# ----------------------------------------------------
# This is the critical setting that disables authentication
# and automatically makes everyone an admin
# WARNING: Only use this in development/testing environments
AUTH_ROLE_PUBLIC = 'Admin'
