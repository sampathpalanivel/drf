To create venv

- python3 -m venv drf-env
- source drf-env/bin/activate

Install package form requirements.txt

- pip3 install -r requirements.txt

Automatically create requirements.txt

- pip3 freeze > requirements.txt

To run this app:

- chmod +x run.sh (mark it executable by run this cmd on your terminal)
  Note: This cmd is required only first time on your environment

- ./run.sh

Manually run app in Local:

- python3 manage.py runserver
