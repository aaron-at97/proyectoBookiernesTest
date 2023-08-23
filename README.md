# Deliverable 3

## Github
[Git Repository](https://github.com/aaron-at97/deliverable3WebProject)

## Heroku

[Heroku website - Deployment Devirable1](https://bookviewarp.herokuapp.com/)

## Summary
  - [Introduction](#introduction)
  - [Project idea](#project-idea)
  - [Requirements](#requirements)
  - [Key points of the functionality of the App](#Key-points-of-the-functionality-of-the-App)
  - [How to run the application](#How-to-run-the-application)
  - [Heroku deployment](#Heroku-deployment)
  - [Features](#Features)
  - [Api](#Api)
  - [Teachers](#teachers)
  - [Authors](#authors)


## Introduction
**Web Project** is a subject of the [Degree Computer Engineering](http://www.grauinformatica.udl.cat/en) studied in [University of Lleida](http://www.udl.es/ca/).
This is the repository of the project of this subject.

## Project idea
Our idea is to implement an application of a company that works as a publisher in which we will have different books online.
In which its different users can read the books online. 
We will have Editors who will be the members of the publishing house who will be able to accept books rejecting them. add covers to books and translate them.
Writers writers will be able to see if their books are accepted or on hold and upload their books to the publisher
Clients read the books, edit their profile, etc.


This objective is to facilitate the interaction when reading the books.

## Key points of the functionality of the App

+ The Client will be able to edit his user profile and will be able to read all the books published on the web.
+ The Writer can see the status of his books if it is published/pending publication or rejected.
+ The Writer the user uploading a book for publishers to see.
+ The Editor may accept the books / reject them.
+ The Editor may publish books and delete books.
+ The Editor may translate them into other languages and upload them to the web, etc
+ API translate: this api translate text

## Checklist of implemented funcionalities:
### First Deliverable:
- [x] Models: created and revised for better functionality
- [x] Admin: activated and possible to midify the database
- [x] Login: login system with users and user administration with forms
- [x] Heroku deployment
- [x] Docker deployment
- [x] Multiserver planning

### Second Deliverable:
- [x] Models: revised for better functionality
- [x] Admin: activated and possible to modify the database
- [x] Login: login system with users and user administration with forms
- [x] Create/Update instances Client: Library / ReadBook / modify perfil form 
- [x] Create/View instances Writer: ListBooks State / Update book form with state 0 default
- [x] Create instances Editor: Asign Book form "Acept and reject" / Rejected Books form "Acept" / Acepted Books form "Recect"
- [x] Create instances Editor:  Delete books all states / publish books acepted
- [x] API translate: this api translate text

## Requirements
The document named **requirements.txt** should include the following dependencies:
```
    asgiref==3.5.0
    Django~=4.0.3
    sqlparse==0.4.
    django-heroku
    gunicorn
    whitenoise
    behave
    behave-django
    urllib3
    selenium
    splinter~=0.17.0
```
## How to run the application with docker

For docker, we recommend to clone the repository and check de Dockerfile and docker-compose.yml, we are able to create
a container for this one using *sudo docker compose run* and executing the different commands, so we are certain that it is
possible.

To run the application as a docker container orchestration we need to have the Dockerfile with the following content
```
FROM python:latest
ENV PYTHONUNBUFFERED=1
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app
```
We also need the file docker-compose.yml with the following content
```
version: "3.9"

services:
  web:
    build: .  
    container_name: BookView
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/app
    ports:
      - "8000:8000"
```
Finally, to run the application you have to execute the following commands:
```
docker-compose up
```

## Heroku deployment

There's already a deployment made with the app, you can find it in:

[Heroku website - Deployment Devirable1](https://bookviewarp.herokuapp.com/)

1- Copy all the document files in a new folder.

2- We make sure that Procfile file exist.
```
  web: gunicorn BookView.wsgi
```
3- We make sure that [requeriments.txt](#requirements) exist with all the following dependencies:
```
  Django
  gunicorn==20.1.0 
  django-heroku 
  whitenoise
```
4- Create a new repository:
```
  git init
  git add .
  git commit -m "heroku deployment"
```
5- Login in heroku:
```
  heroku login
```
6- Create new application in heroku:
```
  heroku create BookView
```
6.1- In case that the application is already created:
```
  heroku git:remote -a BookView
```
7- Push the new repository to the new heroku application:
```
  git push heroku master
```
8- Configure the django environment variables:
```
  heroku config:set DJANGO_SETTINGS_MODULE=BookView.settings_heroku
```
9- Migrate the DB:
```
  heroku run python manage.py migrate
```
10- Create superuser:
```
  heroku run python manage.py createsuperuser 
```

#### Access

The Web accces is with roles an diferents interfaces for Writer, Editor and Client

##### Writer

![writer interface](/writer.png)

* Principal test Writer
```
    Username: testw
    Password: phantom123
```
* Defaults Writer
```
    Username: escriptor
    Password: phantom123
    
    Username: escriptor1
    Password: phantom123
    
    Username: escriptor2
    Password: phantom123
  
    Username: escriptor3
    Password: phantom123
 ```   
 
## Editor
![Editor interface](/editor.png)
### User editor
```
    Username: editor
    Password: phantom123   
 ```   
## Client
![Client interface](/client.png)
### User client
```
    Username: client
    Password: masternum1
```
## Admin
For checking the admin and the only functionality data base of the admin:
```
    Username: admin
    Password: admin
```

#### Login implementation

In order to make a login that will work with our vision, we have used for better coding, better view callings
and better HTML in general. Also, it works perfectly with Django User system.


#### Multiserver planning

One of the requirements for the first deliverable was to create a plan in which we proposed a multiserver deployment of our app, in which
we needed to specify number, functionality and dependences in said network.

For the planning, we will create 3 tiers: the Web tier, the App tier and the Database tier.

First, you have the **Web tier**. This tier will be a server dedicated to reciving request from the users and sending the requested information. It will be the most Client based tier do to the direct connection with the possible users.

Secondly, you have the **Application tier**, this tier will process the Web tier sends it's ways, send request to the Database tier and send the response back to the Web tier. Here will have another server.

Finally, there's the **Database tier**, capable of holding all of the information for our Web App and recieving querys to answer. Yet another container in a server or several containers in different servers(possibly one for every type of model that we have in the app) will be created for said tier.

Additionally, there can be another separated group of containers that have the scripts necessary for the functionality of our App.

#### The application will consist of:
  -  A front end NGINX web server that will be in charge of receiving and making user requests and communicating directly with the Django application.
  -  Three GUNICORN servers, each running an instance of the django application.
  -  A MEMCACHE server for the database.
  -  A DATABASE server, which runs PostgresSQL.
  -  A REDIS server that stores user sessions.
Regarding the gunicorn servers, as they are scalable, if necessary the number of these can be increased in the future.

#### Connections and dependences amongst them The client makes an HTTP request and this is managed by the NGINX server, which transmits it to the gunicorn servers that are running the django application. REDIS is connected to the django framework and it stores user sessions. The django server accesses the DATABASE and once the queries are made, they are stored in the MEMCACHE for faster access in future requests.

#### Optional and obligatory servers
The states that are obligatory are:
  -  NGINX server.
  -  GUNICORN server.
  -  DATABASE server.

## Features
### Agile Behaviour Driven Development (BDD)
Now, we have the initial Django project and application that we'll start populating with functionality.

The purpose of this application is to help users keep track of the books in our library.

Consequently, and following a BDD approach, we first define the intended **features**:

* Edit profile
* Create book
* List of recent books
* View books
* accept book
* Reject book
* Publish book
* Delete book

The result is the following list of feature files with their corresponding content in the *features/* folder:
Feature: Acept Book
  
- *acept_book.feature* \
  **Feature**: Acept Book \
    **To keep** my previous 
    ** To keep my previous** record books up to date As a publisher I want to accept book. 
- *delete_book.feature* \
  **Feature**: Delete book \
    **To keep* my previous book records up to date, \
    **As a** editor, \
    **I want** to delete a record of books that I created, when we do not want that book to be available.
- *list_book.feature* \
  **Feature**: List Book HomePage \
    **To keep me** updated about the online library registered in my library \
    **I want to** list the first 4 books in the library on the home page, not register 
- *publish_book.feature* \
  **Feature**: Publish Bookt \
    **To keep my** old book records posted \
    **as a** editor \
    **I want to** edit a book record that I created was previously accepted.
- *register_book.feature* \
  **Feature**: Create book \
    **Create new book** in the library to accept or reject and have it reviewed by the editor
    **as a** writer \
    **I want to** register a book with about a library. 
- *update_book.feature* \
  **Feature**: Update Client
    **Update data** of client \
    **As a** client \
    **I want to** update a data with a about a user client. 
To facilitate the description of the feature scenarios, while connecting them to Python code that tests if the scenarios are satisfied by the application, we will use the Gherkin syntax and the Behave tool. 

To get Behave and integrate it with Django, install:

The document named **requirements.txt** should include the following dependencies:
```
    behave
    behave-django
    urllib3
    selenium
    splinter~=0.17.0
```

And add the 'behave_django' application at the end of the INSTALLED_APPS list in *myrecommendations/settings.py*:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'eBook',
    'behave_django',
]
```
Finally, for end-to-end test, it is necessary to have a browser to test from client side. With Splinter, different browsers can be configured for testing, for instance Chrome, the most common one. 

Assuming Chrome is already installed in your computer, the only requirement to use it for automated testing is the ChromeDriver, available for Windows, Linux and Mac from [https://sites.google.com/a/chromium.org/chromedriver/downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads)

Or **[Chocolatey](https://chocolatey.org/docs/installation)** on Windows:

```shell script
choco install chromedriver
```
## Environment ##

After installing all the required tools for BDD, we also need to configure the testing environment. In this case, the Django application myrestaurant.

We do so in a file in the *features/* folder called *environment.py*:

```python
from splinter.browser import Browser

def before_all(context):
    context.browser = Browser('chrome', headless=True)

def after_all(context):
    context.browser.quit()
    context.browser = None
```

This file defines the Django settings to load and test, the context to be passed to each testing step, and then what to:

* **Before all tests**: setting Google Chrome as the browser used to act as the user.
* **After all tests**: closing the browser used for testing.


## Api

To be able to use the api we have used the LibreTranslate Api: \
[Git LibreTranslate](https://github.com/aaron-at97/ProjecteWeb) \
[GitHub LibreTranslate Python](https://github.com/aaron-at97/ProjecteWeb) 

```python
     """
     Connect to LibreTranslate API url - https://translate.argosopentech.com/translate
     Args:
       q (str): The text to translate
       source (str): The source language code (ISO 639)
       target (str): The target language code (ISO 639)

       Returns: The translated text
     """
   params = {"q": q, "source": source, "target": idioma}
   url_params = parse.urlencode(params)
   req = request.Request(url, data=url_params.encode())
   
```
To use this application, what we do is treat a text file, take the text and pass it to said api to translate 
it into the language selected in the popUp that will appear in the template. \
At the moment, being a slow API, we only give the option of translating a text file with the following text: 

- *ej.txt*
```
Ejemplo de traducción de la página de un libro
```

In the future the objective is to loop the different files and translate them 1 by 1 per page, to check it is only necessary to change the file **ej.txt**
to **1.txt**

We also have two ways to open them depending on the format of the txt **iso-8859-1** or **utf8**

```python
class TraducirLibro(TemplateView):
    template_name = 'books/editor/solicitud_traduccion2.html'

    def get_context_data(self, **kwargs):
        context = super(TraducirLibro, self).get_context_data(**kwargs)
        data = self.read_file(self.kwargs['libropk'], self.kwargs['pagnum'])
        context['data'] = data

        return context

    def read_file(self, libro, idioma):
        data = ""
        try:
            with open(os.path.join(BASE_DIR, 'staticfiles') + "/img/Libros/" + libro + "/" + "ej.txt", "r",
                      encoding='utf8') as file:
                # Strip lines
                data = file.read()
                data = self.translate(data, "es", idioma, "https://translate.argosopentech.com/translate", libro)
        except Exception as e:
            with open(os.path.join(BASE_DIR, 'staticfiles') + "/img/Libros/" + libro + "/" + "ej.txt", "r",
                      encoding='iso-8859-1') as file:
                # Strip lines
                data = file.read()
                data = self.translate(data, "es", idioma, "https://translate.argosopentech.com/translate", libro)

        return data

    def translate(self, q, source, idioma, url, libro):
        """Connect to LibreTranslate API
        Args:
            q (str): The text to translate
            source (str): The source language code (ISO 639)
            target (str): The target language code (ISO 639)

        Returns: The translated text
        """
        params = {"q": q, "source": source, "target": idioma}

        url_params = parse.urlencode(params)

        req = request.Request(url, data=url_params.encode())

        try:
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE
            response = request.urlopen(req, context=ctx)
        except Exception as e:
            print("No puedo abrir la web")
            print(e, sys.stderr)
            return None

        try:
            response_str = response.read().decode()
        except Exception as e:
            print(e, sys.stderr)
            return None

        data = ""
        data = str(json.loads(response_str))
        print(data)
        nueva = ""
        ant = ""
        data = data[20:len(data)-2]

        for c in data:
            if c == '\\':
                nueva = nueva + " \n "
            elif ant == '\\':
                pass
            else:
                nueva = nueva + c
            ant = c
        try:
            with open(os.path.join(BASE_DIR, 'staticfiles') + "/img/Libros/" + libro + "/" + idioma + "/1.txt", 'w',
                      encoding='utf8') as file_write:
                # write json data into file
                file_write.write(nueva)
                file_write.close()

        except Exception as e:
            with open(os.path.join(BASE_DIR, 'staticfiles') + "/img/Libros/" + libro + "/" + idioma + "/1.txt", 'w',
                      encoding='iso-8859-1') as file_write:
                # Strip lines
                # write json data into file
                file_write.write(nueva)
                file_write.close()

        return data
  ```
## Teachers
The teachers who have guided this project are:
- [Alvaro Ortega](https://github.com/alortegama)
- [Roberto Garcia](https://github.com/rogargon)

## Authors
This project have been developed by:
- [Aarón Arenas Tomás](https://github.com/aaron-at97)
- [Pau Taló López](https://github.com/PauTalo)
- [Ramon Escoda Semís](https://github.com/rescoda7)

