# Cumplo Test





Django applications that connects to the Banxico api to show historiacal graph and information on different monetary series



## Rquirements

  - MySQL 5.7 or newer
  - Python 3.6
  - pip requirements are listed in the 'requirements.txt' file in the project


## Before running

This guide assumes that you already have an instance of mysql server running and have properly installed python 3.6  in you local computer

Before running the application you should follow these steps

- Do the following in your database in your local database
    - A database named 'cumplo_test'
    - A database user named 'user_cumplo' identified by pthe password 'secretpassword'
    - Grant all privileges to 'user_cumplo'


- Located at the application root folder run the following commands

    ```sh
    $ python manage.py makemigrations
    $ python manage.py migrate
    $ python manage.py loaddata series tiies
    $ python manage.py runserver 0.0.0.0:8000
    ```

# After Server is running

    Open your Browser at
    ```sh
    127.0.0.1:8000
    ```

    You should see a white window with a red nav bar, click on any of its options to start using the application
