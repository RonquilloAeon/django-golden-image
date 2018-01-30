#!/bin/bash
echo "Setting up '$1'"

if [ "$1" == "dev" ]; then
    cat > backend/settings/project_config.py <<'EOF'
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'gdb',
        'USER': 'djangodev',
        'PASSWORD': 'golden',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

DEBUG = True

EMAIL = dict()
EMAIL['EMAIL_BACKEND'] = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL['EMAIL_USE_TLS'] = True
EMAIL['EMAIL_HOST'] = os.environ.get('EMAIL_HOST')
EMAIL['EMAIL_PORT'] = 587
EMAIL['EMAIL_HOST_PASSWORD'] = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL['EMAIL_HOST_USER'] = os.environ.get('EMAIL_HOST_USER')
EMAIL['DEFAULT_FROM_EMAIL'] = os.environ.get('DEFAULT_FROM_EMAIL')

HASH_SALT = 'sei39su3sind8ien4hqn'

# Simpler hasher to speed up testing
# For DEV/TESTING only
PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)
EOF
elif [ "$1" == "production" ]; then
    cat > backend/settings/project_config.py <<'EOF'
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}

DEBUG = os.environ.get('DEBUG', False)

EMAIL = dict()
EMAIL['EMAIL_BACKEND'] = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL['EMAIL_USE_TLS'] = True
EMAIL['EMAIL_HOST'] = os.environ.get('EMAIL_HOST')
EMAIL['EMAIL_PORT'] = 587
EMAIL['EMAIL_HOST_PASSWORD'] = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL['EMAIL_HOST_USER'] = os.environ.get('EMAIL_HOST_USER')
EMAIL['DEFAULT_FROM_EMAIL'] = os.environ.get('DEFAULT_FROM_EMAIL')

# SECURITY WARNING: CHANGE FOR PRODUCTION
HASH_SALT = '94nethn49thpbs3e93nhu6'
EOF
else
    echo "No environment specified [dev|production]"
fi