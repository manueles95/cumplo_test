# Cumplo Test





Django applications that connects to the Banxico api to show historiacal graph and information on different monetary series

To see an online demo [click here](http://159.65.108.240:8000/)




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
    $ pip install -r requirements.txt
    $ python manage.py makemigrations
    $ python manage.py migrate
    $ python manage.py loaddata series tiies
    $ python manage.py runserver 0.0.0.0:8000

    ```

# After Server is running

- Open your browser at **127.0.0.1:8000**



You should see a white window with a red nav bar, click on any of its options to start using the application

# Docker alternatives

This application is set up to use docker and docker-compose

## First
- Go to setting.py file and change the 'HOST':'localhost' in database configuration to 'HOST':'db'

If you don't want to set a database server and run the described python commands by hand you can simply  run

  ```sh
  $ docker-compose up --build

  ```

This will automatically create

- A conatiner running the sql server with the required user and database configurations
- A container serving our application

**Due to an unidentified bug when composing the db image, you may need to run the docker-compose command two or three times for the initial set up to take place**

After running that command you are set to go, simply open your browser at at **127.0.0.1:8000** and start using the application
