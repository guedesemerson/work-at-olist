# Description

In this sample application, you will create a web service application using Django to Olist challenge in Python, with standard best practices and respecting the rules.

# Python Django web application

This app contains an opinionated set of endpoints for web serving:

## Steps

### Execute web service
You can get started building this application locally, but you can either run the application in web using the heroku link host web (http://olistapichallenge.herokuapp.com).

### Building Locally

* Install [Python](https://www.python.org/downloads/)

Running Django applications: You can download the project dependencies with:

```bash
pip install -r requirements.txt
python manage.py migrate
```

To run your application locally:

```bash
python manage.py runserver
```

Your application will be running at `http://127.0.0.1:8000`.  You can access the `/book` and `/author` endpoints at the host.

### Import csv file

To import authors in database you need to execute this script following this format:

name<br>
author1<br>
author2<br>
author3<br>
author4<br>
author5<br>
author6<br>
...

bash:<br>
python manage.py import_authors file.csv



### Testing enpoints

bash:<br>
python manage.py test
