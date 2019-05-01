# HyraxMapUI
## Introduction

It integrate a MAP UI to perform Hyrax Server Request to fetch data based on their GeoSpatial information.
I will automatical create a request for the server to fetch data based on the coordinates bounds selected in map.

## Run the App

clone the respository
```
$ git clone https://github.com/ShubhamShaswat/HyraxMapUI.git
```

#make virtual environmnet
```
$ mkvirtualenv --python=/usr/bin/python3.4 HyraxMapUI-virtualenv
```

Install Django using pip

```
$ pip install django
```


Go to the directory
```
$ cd HyraxMapUI
```

```
$ python manage.py migrate
```

```
$ python manage.py createsuperuser
```


```
$ python manage.py runserver
```
