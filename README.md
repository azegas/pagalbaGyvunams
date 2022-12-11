# pagalbaGyvunams DEV branch

## How to launch this app

### Installing system dependencies

- Make sure you have **Python** installed on your system, check that by
  opening command line(cmd) and typing in `python --version`. If the output is
  similar to **Python 3.8.10** - you are good to go. If it says **python is
  not found** -  download and install it [Here](https://www.python.org/downloads/).
- Make sure [git](https://www.python.org/downloads/) is installed in on your system.
- Open `cmd` in the location your want this project to be cloned(downloaded).
- Copy this: `git clone https://github.com/arvydasg/pagalbaGyvunams.git`
  and put in your terminal, press enter.
- You now have cloned the whole repository of the project, it exists
  on your computer in the location you wanted.
- Make sure **pip** is installed. [Here is how to install
  it](https://www.geeksforgeeks.org/how-to-install-pip-on-windows/) if
  you haven't already.
  
### Installing python dependencies

- Every Django python project has dependencies(or packages which
  allow the project to run). Usually those packages are listed in
  "requirements.txt" file.
- If you have cloned and ran many projects in the past, chances are your computer
  is full of those "dependencies" from each and every project. A good practice is
  to have a separate "folder" for each project where you store the
  needed dependencies for that particular project.
- Lets create such folder. It will be our "virtual environment" for
  this particular "pagalbagyvunams" project.
- Open terminal in the directory of the project that you have cloned
  and do `python -m venv venv` and it will create a folder "**venv**".
- write `pip list` to list all the packages you have on your WHOLE
  system.
- now let's activate our "virtual environment" by typing
  `.\venv\scripts\activate` in command line
- a little word **(venv)** should appear at the left of your command line. It
  indicates, that we are "inside" this "virtual environment" now. Try
  typing `pip list` again and now you will see ONLY the packages that
  are installed in this virtual environment.
- let's install packages that are needed to run this project.
- Do that by typing `pip install -r requirements.txt` (make sure you
  are in the same folder that has requirements.txt in it).
  
### Handling secret variables

- What is secret - has to remain secret
- Take `.env_example` file and rename it to `.env`
- Now take the [secret
  key](https://stackoverflow.com/questions/7382149/whats-the-purpose-of-django-setting-secret-key)
  value from `settings.py` and place it in `.env` appropriate field
- now instead of the secret key being exposed to the public when you
  push yourf project to github, it will remain in your system, .env
  file which is [gitignored](https://git-scm.com/docs/gitignore) and
  is not pushed to git.
- Now our secret values are secret. As you can see in .env file we can
  also define our allowed hosts, debug value and possibly other
  variables in the future.

### Running the project

- After successful dependencies installation, make sure you are
  located in the same folder where **manage.py** file is.
- Then write `python manage.py migrate` and press enter.
- Now write `python manage.py runserver` and press ented.
- Go to your browser and open http://127.0.0.1:8000/ 
- You should now see the project running in your local environment.
