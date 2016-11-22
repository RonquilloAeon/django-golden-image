# Django Starter Project
Use this project to jump-start your Django projects

## Getting Started
1. Clone repo
2. Set up a virtual environment with Python 3.5
3. Run `./scripts/setup.sh dev`
4. Create a Postgres DB using credentials from `backend/settings/project_config.py
5. Run `pip install -r requirements.txt`
6. Run `./manage.py migrate`
7. Run `./manage.py createsuperuser`
8. Run `./scripts/install_redis.sh`
9. Run `./scripts/start.sh`
10. Run `./manage.py runserver` in another terminal