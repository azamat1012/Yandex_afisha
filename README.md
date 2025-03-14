# Yandex afisha

This script is used for adding favorite locations and see them on the map. 

[demo version of a user_interface](https://aza004mat.pythonanywhere.com/)

[demo version of an admin panel ](https://aza004mat.pythonanywhere.com/admin)

----

## <h2 style="text-align:center">Environment</h2> 
-----
### Requirements


Python3 must already be installed in your environments. You may create an virtual environement as well to not trash your memory space. 

 - To run your bot correctly you should install next requirements to your env:


1. Django==5.1.7
2. django-admin-sortable2==2.2.4
3. django-tinymce==4.1.0
4. pillow==11.1.0
5. python-environ==0.4.54



or just but the next line of code in your bash terminal:

```bash
  pip install -r requirements.txt
```

- In your created .env file you should add your keys

```bash
    SECRET_KEY="PUT_YOUR_SECRET_KEY"
    DEBUG=True
```
-----
## Complete migrations

```bash
    python manage.py migrate
```
-------
## Run 

```bash
    python manage.py runserver
```


Now your website will be running on the local host via address:
http://127.0.0.1:8000

-----
##  <h2 style="text-align:center">Notes</h2> 
---

If you'd like to go to the admin panel then follow next steps:

1. Create super user for permission:

```bash
    python manage.py createsuperuser
```

Then come up with passkeys

2. Re-run the server

```bash
    python manage.py runserver
```

3. Go to the admin panel, it's located on:

http://127.0.0.1:8000/admin


There you're able to add a new info now and see the changes on the main page

----
## <h2 style="text-align:center">Project Goals</h2> 
---

The code is written to simplify the user interface when they would like to see their fav places!
