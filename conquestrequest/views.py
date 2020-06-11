
from django.shortcuts import render,redirect, get_object_or_404
from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from .models import Item
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.urls import reverse
from .forms import ItemForm
from django.utils.datastructures import MultiValueDictKeyError
import json
import requests
import time


def index(request):
    content={}
    error_message=""
    # give all the requests
    items = Item.objects.all()
    if request.method == "POST": 
        if "ItemAdd" in request.POST: 
            # validate the input form
            form = ItemForm(request.POST) 
            # ,request.FILES
            if form.is_valid():
                name = form.cleaned_data["name"] 
                description = form.cleaned_data["description"] 
                filelink = form.cleaned_data["filelink"]

                # The following code can be used to upload a picture from desktop after the web is deployed 
                # myfile = request.FILES['myfile']
                # fs = FileSystemStorage()
                # filename = fs.save(myfile.name, myfile)
                # uploaded_file_url = fs.url(filename)
                # a_item = Item(picture=uploaded_file_url, name=name, description=description)
                # get_file_url = "../conquestapp"+uploaded_file_url
                # print(get_file_url)
                # pic = {"file": ("pic", open("../conquestapp/Capture.PNG","rb"),"image/png")}
                # print(pic)
                # ,"Content-Type":"multipart/form-data"

                # create a request based on the input information
                url = 'https://developer-demo.australiaeast.cloudapp.azure.com/api/requests/create_request'
                headers = {"Authorization":"Bearer A4Fo2/hpXIWeLnS6dg0Nqo9mVGo=","Accept":"application/json","Content-Type":"multipart/form-data"}
                playloadRequest = {"ChangeSet": {
                            "Changes": [       
                            "OrganisationUnitID",
                            "RequestDetail",
                            "RequestorName"
                            ],
                            "LastEdit": "2020-06-10T03:03:52.757Z",
                            "Original": {
                            "OrganisationUnitID": 0,
                            "RequestDetail": "string",
                            "RequestorName": "string"
                            },
                            "RequestID": 0,
                            "Updated": {
                            "OrganisationUnitID": 0,
                            "RequestDetail": description,
                            "RequestorName": name
                            }
                        }
                        }
                       
                r = requests.post(url, data=json.dumps(playloadRequest),headers=headers)
                print("here is a response")
                # get request ID from the response
                requestID = str(r.text)
                print(requestID)
                # add this request to database, so that records can be shown in the webpage
                a_item = Item(picture=filelink, name=name, description=description,requestID=requestID)
                a_item.save() 
                # add a picture and link to the request
                # since it will take some to response correctly, I made it keep posting until it get a successful response
                flag = False
                while (flag==False):
                    playloadDoc =  {
                        "Address": filelink,
                        "CreateTime": "2020-06-10T13:44:29.090Z",
                        "ContentType": "image/jpeg",
                        "DocumentDescription": "string",
                        "ObjectKey": {
                            "int32Value": requestID,
                            "objectType": "ObjectType_Request",
                            
                            "timestampValue": "2020-06-10T03:27:39.696Z"
                        }
                        }
                    urlAddDoc = "https://developer-demo.australiaeast.cloudapp.azure.com/api/documents/add_document"
                    r2 = requests.post(urlAddDoc, data=json.dumps(playloadDoc),headers=headers)
                    if r2.status_code == 200:
                        flag = True
                print(str(r2.text))
                return redirect(reverse("index"))
            # if there is something wrong with the input error message will show up
            else:
                content["show"]=form.errors
                error_message = content["show"]
                return render(request,"index.html",{"items":items,"show":error_message})

    return render(request,"index.html",{"items":items})