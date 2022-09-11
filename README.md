# Documetrics

This is a Simple Student Identification System Developed for Microsoft Engage 2022 while Learning Django.

Thousands of people submit fake marksheets and degrees all across the country, and there is no means to check the authenticity of these documents. This project is an end-to-end credential verification system that helps academic/business organisations verify marksheets/degrees/certificates. This system uses the technology of face authentication to map students and teachers to unique IDs linked to their government-issued IDs and every student can use face recognition to access their results and certificates from anywhere. The documents uploaded on this website are uploaded from verified and authentic sources. To increase security technologies like geofencing and time duration monitor can also be added. Further to reduce the risk of forging we can upload these documents over blockchain for lifetime access. All the features in this project are registration, authentication using face recognition and documentation updating feature. This project uses a model dataset which includes the government-issued IDs and the details associated with them. The photos from this data are compared to the input images using python language’s face_recognition library and authentication of the person is done. Further the backend of the website is created using Django framework and HTML,CSS and JavaScript are used for the frontend of the website. 

## Project Video: 

https://drive.google.com/file/d/1Td3LYkmLwWm-ifSnFqJ9uz7W63p2Tbj8/view?usp=sharing

## Deployed to

http://documetrics.herokuapp.com

## Presentation:

https://drive.google.com/file/d/1TwxFs7BrP_lpg_TZ_jlAoCC35s1SqyZ3/view?usp=sharing


## How to Install and Run this project?

### Pre-Requisites:

Install Git Version Control [ https://git-scm.com/ ]

Install Python Latest Version [ https://www.python.org/downloads/ ]

Install Pip (Package Manager) [ https://pip.pypa.io/en/stable/installing/ ]

* Alternative to Pip is Homebrew *

### Installation

1. Create a Folder where you want to save the project

2. Create a Virtual Environment and Activate

Install Virtual Environment First
```
$  pip install virtualenv
```
Create Virtual Environment

For Windows
```
$  python -m venv venv
```
For Mac
```
$  python3 -m venv venv
```
For Linux
```
$  virtualenv .
```
Activate Virtual Environment

For Windows
```
$  source venv/scripts/activate
```
For Mac
```
$  source venv/bin/activate
```
For Linux
```
$  source bin/activate
```
3. Clone this project
```
$  git clone https://github.com/287palak/Documetrics
```
Then, Enter the project
```
$  cd project
```
4. Install Requirements from 'requirements.txt'
```
$  pip3 install -r requirements.txt
```
5. Add the hosts

Got to settings.py file
Then, On allowed hosts, Use [] as your host.
ALLOWED_HOSTS = []

6. Now Run Server

Command for PC:
```
$ python manage.py runserver
```
Command for Mac:
```
$ python3 manage.py runserver
```
Command for Linux:
```
$ python3 manage.py runserver
```
