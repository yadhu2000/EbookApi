# A small ebook management REST API with Django and SQLite.
***
This is an API for ebook management developed using rest framewrok using Django and SQLite. This api also checks authentication before delivering the request.

##Table of contents
1. [General Info](#general-info)
2. [Softwares Used](#softwares-used)
3. [Environmental Setup](#environmental-setup)
4. [Creating Project](#creating-project)
5. [URL Patterns Used](#url-patterns-used)

### General Info
***
The REST API that support CRUD operations on one or many ebooks. The API is also able to
return ebook lists that sorted or filtered ebooks by any of the fields.
The REST API supports multiple users and uses token authentication to authenticate and authorize the
user.

## Softwares Used
***
A list of softwares used in the project:
*[Visual Studio Code](https://code.visualstudio.com/): Version 1.73.2
*[SQLiteStudio](https://sqlitestudio.pl/): Version 3.4.0
*[Postman](https://www.postman.com/): Version 10.3.5

## Environmental Setup
***
Install python and add it to PATH.
Install Visual Studio Code.
Install SQLite Studio.

## Creating Project
***
### setting up the server
***
We have to install some modules first.
```
$ pip install django
$ pip install djangorestframework
$ pip install django-cors-headers
$ django-admin startprojectDangoApi
```
Files in the project:
>__init__.py (Empty file indicates the given folder is a python project)
>asgi.py (Entry point to the asgi compatible webservers)
>wsgi.py (Entry point to the wsgi compatible webservers)
>Urls.py (Has all the url declaations needed for this project)
>setting.py (Has all the configurations needed for the project)
>manage.py (Is the command line utility which helps to interact with the django project)

```
$ python manage.py runserver
```
>Copy and paste the URL in the browser and press enter.
>"The install worked successfully! Congratulations" message will be displayed.

### Creating app
***
```
$ python manage.py startapp EbookApp
```
>Register app in the installed apps section inside settings.py.
>Add 'Corsheaders.middleware.CorsMiddleware' in MIDDLEWARE section inside settings.py.
>Add CORS_ORIGIN_ALLOW_ALL =True inside settins.py.
>Create models for Ebooks inside models.py.
>Connect the database by adding db fileto SQLite studio.

```
$ python manage.py make igrations EbookApp
$ python.py migrate EbookApp
```
>Tables will be created.
>Write SQL query for selecting and instering records to and from the database.

### CRUD OPerations
***
>Create serializers.py file inside EmployeeApp.
>Import required modules.
>Create serializer Class for Ebooks.
>Import required modules for views in views.py in EbookApp.

Code for CRUD OPerations:
```
def get(self, request,id=0, format=None):
            Ebook = Ebooks.objects.all()
	Ebooks_serializer = EbooksSerializer(Ebook,many=True)
        return JsonResponse(Ebooks_serializer.data,safe=False)
def post(self, request,id=0, format=None):
            Ebooks_data = JSONParser().parse(request)
            Ebooks_serializer = EbooksSerializer(data=Ebooks_data)
            if Ebooks_serializer.is_valid():
                Ebooks_serializer.save()
                return JsonResponse("Added Successfuly", safe=False)
            return JsonResponse("Failed to Add", safe=False)
def put(self, request,_id=0, format=None):
            Ebooks_data = JSONParser().parse(request)
            Ebook = Ebooks.objects.get(ID=_id)
            Ebooks_serializer = EbooksSerializer(Ebook, data=Ebooks_data)
            if Ebooks_serializer.is_valid():
                Ebooks_serializer.save()
                return JsonResponse("Update Successfull", safe=False)
            return JsonResponse("Failed to update")
def delete(self, request,_id=0, format=None):
            Ebook = Ebooks.objects.get(ID=_id)
            Ebook.delete()
            return JsonResponse("deleted Successfully", safe=False)
```

>Create a new file urls.py in EbookApp and import required modules.
>Set url Patterns.
>Include these URLs in the main URL file.

```
$ python manage.py runserver
```

### Testing API in Postman
***
>Copy and paste the server URL.
>Test GET,POST,PUT,DELETE method by sending request.

### Authentication
***
>Import Authentication modules to serializers.py, urls.py, views.py.
>Add serializer class for user in serializers.py.
>Add the Authentication Scheme and permission policy inside settings.py.
>Create an Authentication class in views.py.
>Add url patterns in urls.py in EbookApp.
>Add 'rest_framework.authtoken' in INSTALLED_APPS inside setting.py.
Code for automatically generate token for every user inside models.py:
```
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
```
>Create a class or Custom token authentication by token.
>Add the url for custom authentication in urls.py.
```
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```
#### Cheching Token Authentication
***
>In Postman select POST method.
>In form date add key as 'username' and 'password', Add previously created username and password to it.
>Copy URL for custom authentication and send.
>A token will be generated with user_id and email.
>copy that token.
>Change permission_classes=[permission.IsAuthenticated]
```
	 authentication_classes = [authentication.TokenAuthentication]
         permission_classes = [permissions.IsAuthenticated]
```
>Try to GET the users by entering the URL for users and send.
 
 Output will be generated as:

	{
	   "detail" : "Authentication credentials were not provided."
	 }

>Inside Postman inthe headers section, We set an authorization token and the value will be given by pasting the previously copied token.
>After that when we send the request for GET, POST, PUT, DELETE operations, The respective operation will be performed succesfully.

## URL Patterns Used
***
```
http://127.0.0.1:8000/users
http://127.0.0.1:8000/token/auth
http://127.0.0.1:8000/auth/eBooks
http://127.0.0.1:8000/auth/ebooks/([0-9]+)


