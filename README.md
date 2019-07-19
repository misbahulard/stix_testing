# stix-testing
This app is for test the STIX object such as "access time, analytics, or counter"

## Description
`access.py` used to find out the time needed to access data \
`analytics.py` used to find out the top 10 actors and targets \
`counter.py` used to calculate actors and targets \
`query` are additional queries for further analysis and making additional collections such as "analytics"

## Config
set the database uri in each python file

## Create python virtual environment
```
virtualenv venv
```

## Install dependencies
```
pip install -r requirements.txt
```

## Run app
```
python access.py
python analytics.py
python counter.py
"query" run each query in mongo console
```