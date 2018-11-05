# Snake Stats

This is a web interface with a database for keeping stats on my snake feedings. The basic idea is to display a *pretty* list and show some graphs.

## Dependencies
### Python
* pipenv
* others; see Pipfile

### System
* python3
* mongodb

### Web
* jQuery

## How to run
Skip step 1 if not using pipenv
Skip step 4 if wanting to stub the API - stubApi set to True from config.py

1. Run "pipenv shell" - creates shell in virtualenv
2. Run "python main.py"
3. Open browser to "http://localhost:5000"
    * flask defaults to port 5000. check terminal output to confirm the correct port.
4. Ensure mongodb is running with configuration from "mongodb" in config.py
