# dogAPI
A basic REST API developed in Python using Flask.

## Files
* `Pipfile` - dependency list for pipenv
* `Pipfile.lock` - confirm requirements are the correct version
* `dogAPI.py` - simple restful API
* `dogs.json` - JSON formatted local datastore
* `README.md` - A quick explanation

## Installation
**Prereqs:**
* Python 3.7
* Pipenv

#### Clone repository:
    git clone https://github.com/vmannello/dogAPI
#### Install dependencies:
    pipenv install
#### Run server:
    pipenv run python dogAPI.py

## Routes
Request Type|Path|Action|Parameters|Example
------------|----|------|----------|-------
**POST**| /dogs | Add a new dog | name, owner, notes | `curl http://127.0.0.1:5000/dogs -d "name=Fido" -d "owner=Joe Smith" -d "notes=Very nice." -X POST`
**GET**| /dogs | List all dogs | -- | `curl http://127.0.0.1:5000/dogs`
**GET**| /dogs/:id | Get details for specific dog | -- | `curl http://127.0.0.1:5000/dogs/dog_1`
**PUT**| /dogs/:id | Update details for specific dog | name, owner, notes | `curl http://127.0.0.1:5000/dogs/dog_1 -d "owner=Mark Twain" -X PUT`
**DELETE**| /dogs/:id | Remove a dog | -- | `curl http://127.0.0.1:5000/dogs/dog_1 -X DELETE`
