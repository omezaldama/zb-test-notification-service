# Notification Service

This is a project done with Python 3.10.4

## Run locally

Download the repo
```
git clone https://github.com/omezaldama/zb-test-notification-service.git
cd zb-test-notification-service
```
Create a virtual environment and activate it.

On Windows:
```
virtualenv venv
. venv/Scripts/activate
```

On Linux:
```
mkvirtualenv zb-notif
workon zb-notif
```

Install dependencies.
```
pip install -r requirements.txt
```

Run the server.
```
uvicorn main:app --port=8001
```
If you want to watch for changes, use the reload flag.
```
uvicorn main:app --reload --port=8001
```
This will run the app on port 8001. Here we use port 8001 so it does not collide with the port used by the api by default.
```
http://localhost:8001
```
Swagger documentation will be located in.
```
http://localhost:8001/docs
```


## Project structure

File main.py is the entrypoint of the app.

Endpoint routes are defined in the folder /api.

Pydantic models are defined in folder /pd_models. Database models are defined in folder /db_models.

Folder /notifiers contains functions to send emails using Sendgrid Python library.

File settings.py contains settings for the app.

File requirements.txt contains the pip dependencies needed to run this app.


## Built with

* [Python 3.10.4](https://www.python.org/) - Main programming language
* [FastAPI 0.79.0](https://fastapi.tiangolo.com/) - Backend framework
* [Sendgrid 6.9.7](https://docs.sendgrid.com/for-developers/sending-email/quickstart-python) - Python API for sending emails via Sendgrid
