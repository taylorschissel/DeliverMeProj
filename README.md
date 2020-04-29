# DeliverMe

## Table of Contents
1. Hosting
1. Installation
	1. Cloning
	1. Setup
1. Features
	1. Installing a Virtual Environment
	1. How to Run
	1. The DeliverMe Webpage
	1. How to Quit Running
1. Troubleshooting
1. Team Name and Contributors
1. Support

## Hosting
* This web app is hosted at isaacfc4.pythonanywhere.com
* Its hosting will be active until July 29, 2020
## Installation
*Cloning*
* Access the repository via the GitHub Link: https://github.com/taylorschissel/DeliverMeProj
* Go to the green box where it says "Clone or download" to find the repository link

*Setup*
* The operating system used to construct DeliverMe locally was Mac OS X
* In order to run the DeliverMe, the following programs must be installed:
	* Pycharm Professional 2020.1 or equivalent IDE
	* Python 3.8.2
  
## Features
*Installing the Project from Github*
* In a terminal, navigate to a convenient directory and type: mkdir DeliverMeProj
* Now navigate to that new directory and enter: sudo git clone https://github.com/taylorschissel/DeliverMeProj
*Installing a Virtual Environment*
* Install the virtual environment package using: $ sudo pip install virtualenv
* Create a virtual environment with Python: virtualenv venv -p python3.8
* To activate the virtual environment, use: source venv/bin/activate
* Once activated, install the following packages into the venv:
	* Django: pip install django
	* Django Admin: pip install django-admin
	* Social Auth: pip install social-auth-app-django
* Once finished, navigate to the DeliverMeProj directory containing manage.py,
* and run the commands "python3 manage.py makemigrations" & "python3 manage.py migrate"

*How to Run*
* Type the following line in the command line: python manage.py runserver
* The line "Starting developement server at ..." comes up, followed by an address
* Click on the address to be directed to the DeliverMe page

*The DeliverMe Webpage*
* Once redirected to the DeliverMe homepage, login by clicking on the "Google" box
* Choose an associated Google account to continue with
* You will then be redirected to a welcome page with multiple options:
	* To post a job, select "New Job" and enter:
		* Enter the item you'd like delivered
		* A brief description of the item (identifying features)
		* The pickup name and address
		* The dropoff name and address
	* To see available jobs, select "View Jobs"
		* Click on a delivery job to view the description and the pickup and dropoff information
		* To accept the job, click the blue box at the bottom of the screen that says "Accept this Job"
* To learn more about DeliverMe, select "About" from the header menu
* To log out, select "Logout" from the header menu
    
*How to Quit Running*
* Close the DeliverMe webpage tab
* Back in the command line, hit the command key and C and the same time

*Troubleshooting*
* If you seem to be having issues with install, try varying the use of terms such as pip/pip3 and python/python3

## Contributors
* Isaac Fluhr-Chapman
* Taylor Schissel
* Michael Sisk
* Emma Golden
* Ivan Isakov

## Support
* To reach out with questions, please contact Isaac's email: isaacfc4@bu.edu
