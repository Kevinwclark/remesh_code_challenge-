# Remesh Clone

A simplified version of Remesh. The basics of Remesh are such that there are conversations. In each conversation, users send messages. Another group of users respond to those messages by submitting thoughts.

## Prerequisites

What things you need to install the software.
Go to [Python](https://www.python.org/) for instructions to install - test if it installed with the command below. You should see a version like 3.9.0. If not, please recheck the Python instructions. 
```
python --version 
```
Go to [Pipenv](https://pipenv.pypa.io/en/latest/install/#id2) for instructions to install. Test with command below. You should see something similar to 'pipenv, version 2020.11.15'

"Pipenv is a dependency manager for Python projects. If you’re familiar with Node.js’s npm or Ruby’s bundler, it is similar in spirit to those tools. While pip can install Python packages, Pipenv is recommended as it’s a higher-level tool that simplifies dependency management for common use cases. -quoted from [here](https://pipenv.pypa.io/en/latest/install/#id2)"

```
pipenv --version 
```
With everything installed we can move forward. 

## Getting Started

Go to the GitHub [Remesh Repo](https://github.com/Kevinwclark/remesh_code_challenge-) and clone the repo. Open a terminal or command line and cd to the directory you would like to place this project. Enter the below command. Keep in mind, between the <> in the command below is the link copied from GitHub.

```
git clone <name of repository>
```
Now we should have the software local on our machine. Type the command below to show the contents of the directory. You should see 'remesh_code_challenge-'
```
ls
```
Now that we have it lets move into the directory with:
```
cd remesh_code_challenge-
```

## Getting The Project Running

Lets create a virtual evnvironment and manage all dependencies. In our terminal, and in the project just created run:

```
pipenv install
```
To activate this project's virtualenv, run: 

```
pipenv shell
```
Now is the time to open the code in your editor. In the directory 'remesh_clone' create a .env file. The file structure should look similar to the structure below. 

 
    ├── ...
    ├── remesh_clone                  
    │   ├── __init__.py             
    │   ├── .env              
    │   ├── asgi.py            
    │   ├── settings.py            
    │   └── # etc.
    └── ...

In this file you will need to place the SECRET_KEY sent with the email for this submission.  
It will look like the example below. Make sure there are no spaces and no quotes. Also, the key below will not work.
```
SECRET_KEY=us=5@%y)#=ko(rxq4$vrkumlt!!0lskdflaksdjfl;askdjftb+ccpr(8
```

Next, we need to run a command to set up our database:
```
python manage.py migrate
```
Run this command if you would like to create a superuser to access the admin panel. The admin panel will allow you to create data easily. Follow the prompts. This command is optional. Remember the username and password to later access the admin
```
python manage.py createsuperuser
```
We made it this far! Let's spin up our server!
```
python manage.py runserver
```
You should see something like this:
```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
February 13, 2021 - 06:30:38
Django version 3.1.6, using settings 'remesh_clone.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Go to your browswer and enter this link:
```
http://127.0.0.1:8000/
```
If you created a superuser, you can access the admin panel with this:
```
http://127.0.0.1:8000/admin
```


## Running the tests

Have you project virtual environment running. CONTROL-C if the server is running. Then enter the following command. 
```
./manage.py test
```
What you should see:
```
----------------------------------------------------------------------
Ran 5 tests in 0.060s

OK
Destroying test database for alias 'default'...
```


## Author

* **Kevin Clark** - [GitHub](https://github.com/Kevinwclark)


## Acknowledgments

* Thank you to Remesh for allowing me to submit my project. 
* Hat tip to Kenzie Academy and Instructors.


