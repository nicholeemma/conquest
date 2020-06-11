# **Raise Request through Conquest API**

#### An App allows user to create a request and attach a picture to that request.



### Basic ideas

Users fill in request related information, with submit button clicked, the request will be stored as an item in the database, meanwhile, the information will be transformed in JSON format and post to Conquest "create_request" API. If the post is successful, requestID will be returned. The requestID and picture address will be transformed in JSON format and post to Conquest"add_document" API. After that a picture is linked to the request in success. The users can see the what did they input in the below "request information table".

### Demo

Web app demo for create a request https://youtu.be/Y4eUWJ544Oo

Check the result from the mobile App https://youtu.be/9yKiXP4yq5w

### Tech-Stack

- Python Django
- HTML, materialize CSS
- Conquest API https://conquestsolutions.github.io/swagger/?api-version=2.0.10#/DocumentService/AddDocument

### How to use

1. Under the path \conquest\conquestapp, open console, run " python manage.py runserver 8100" (Before this, you might need to pip install python and django)
2. Open the "http://localhost:8100/" in the browser

### What can be improved in the future

1. Form validation (For now, I used a content length limit as one rule of form. In the future, the form can validate whether the picture link is accessible and workable)
2. Picture upload(If the current web application can be deployed and accessed through a HTTPS link, I can upload the picture from desktop. The picture will be firstly stored in the database and can be accessed through HTTPS link, then I can use this link as "address" to attach a picture in a request. I have realized partial development.)
3. UI



Jiayue(Nicole) Yang 6/11/2020

If you have any question, contact me through "hpyangjiayue@gmail.com"