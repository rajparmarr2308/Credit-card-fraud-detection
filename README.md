

!) CREATE VIRTUALENVIRONMENT WITH COMMAND

    virtualenv venv

#venv is name of name of virtualenvironment. we can give any name which we want.

!) Then Activate venv

    venv\Scripts\activate

!) Then Install requirements.txt with following COMMAND

    pip install -r requirements.txt


!)create superuser by following COMMAND in your root directory

    python manage,py createsiperuser

!) Then start your server by typing following COMMAND

    python manage.py runserver







NOTE:- If you are adding some model in models.py or changing something don't forget to make migrations 

    python manage.py makemigrations

and migrate it to database

    python manage.py migrate


