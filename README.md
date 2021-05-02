Dataset Link :- https://www.kaggle.com/mlg-ulb/creditcardfraud

1)  First  Create virtualenvironment with following COMMAND:-

        virtualenv venv

 NOTE:- venv is name of name of virtualenvironment. we can give any name which we want.

2) Then Activate venv:-

        venv\Scripts\activate

3) Then Install requirements.txt with following COMMAND:-

        pip install -r requirements.txt


4)  create superuser by following COMMAND in your root directory:-

        python manage.py createsuperuser

5)  Then start your server by typing following COMMAND:-

        python manage.py runserver







    NOTE:- If you are adding some model in models.py or changing something don't forget to make migrations 

        python manage.py makemigrations

    and migrate it to database

        python manage.py migrate


