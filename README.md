[![Build Status](https://travis-ci.org/CaseyScott/Gaming-hardware-Django-milestone.svg?branch=master)](https://travis-ci.org/CaseyScott/Gaming-hardware-Django-milestone)

[Glitch Gaming](https://gaming-hardware-milestone4.herokuapp.com) 

# **Table of Contents**

- [**Table of Contents**](#table-of-contents)
	- [**Glitch**](#Glitch)
	- [**Given Brief**](#The-Given-Brief-and-Requirements)
	- [**UX**](#ux)
	  - [**User Stories**](#user-stories)
      - [**Users**](#users)
	  - [**Wireframes**](#wireframes)
	- [**Existing features**](#existing-features)
		- [Create account and log in](#Create-account-and-log-in)
		- [Home page](#home-page)
		- [Departments](#department)
		- [detail-view page](#detail-view-page)
		- [Navigation bar and footer](#navigation-barand-footer)
	- [**Features left to implement**](#features-left-to-implement)
    - [**Database**](#database)
	- [**Technologies used**](#technologies-used)
	- [**Testing**](#testing)
	- [**Deployment**](#deployment)
	  - [**How to run the project locally?**](#how-to-run-the-project-locally)
	  - [**Remote Deployment**](#remote-deployment)


# **Glitch**


## **The Given Brief and Requirements**
Full stack frameworks with Django milestone project.
Glitch is an e-commerce website for selling high end gaming computer hardware.

Project purpose:
This project, is a full-stack site based around business logic used to control a centrally-owned dataset. It has an authentication mechanism and provide paid access to the site's data and/or other activities based on the dataset, such as the purchase of a product/service.


## **UX**
Glitch is an online high end gaming componet store for purchasing computer parts deicated to PC gaming.
The site is simple to use with Most categories covered. People spending at this level of componentry know exactly the parts they need so it really just comes down to price. Having the best prices avaliable is what will bring customers coming back. There are also 6 pre-built options with the latest hardware at competitive prices.

## **User Stories**
- As a user I want an online gaming store that has the best prices avaliable.
- As a user I want to be able to contact the site to request a price comparison or beter.
- As a user spending a lot from overseas stores costs to much with tax and duties, I want a NZ store that can compete with those prices.
- As a user I want a simple, easy to use site.
- As a user I want to know my credit card and email are safe. 
- As a user I want to be able to create an account to sign in and out as a return customer.
- As a user I want to be able to freely go from products to cart and continue shopping.
- As a user I want a mobile friendly site.
- As a user I want to update or delete from my cart.

### Users
- Users of this site can browse all content without registiering but if a user wants to purchase they must be regisitered and signed in to complete this action.

## Existing Features
### Create account and log in
- Users can regisiter their details and sign in giving them the ability to make purchases.
### UserProfile
- User is able to change there password from there profile page.
- User can sign in and out
- A user that is logged in has access to the user drop down in the nav bar that only shows to a signed in user.
### Home page
- Home page shows categories avaliable in a drop down from the navbar or with carousel images that link to that category.
- Pre-built machines for those that just want to pay and play.
### Departments
- All avaliable components are in departments in their own categories.
### Navigation bar and footer
- Navbar is on every page making it easy for the user to move around the site from category to category, use the search bar or return home at any time.
### Cart
- Cart displays all products in the users cart
- Total price and allows the user to edit or remove items
### Checkout
- Users must log in to access the checkout page
- Total price and order forms displayed before confirmation of payment
- Stripe 4242 4242 4242 4242 credit card number for testing

## Features left to implement
- Categories are hard coded at this stage. This list in real world situation would be a dynamic list so the administrator could change the list and add more categories as the company expands.
- home page to have more information on products instore 
- User feedback about where the completed purchase has been sent to with package tracking.
- return policy for damaged goods.
- User comments on components instore.
- Component compatibility feedback as the user adds items to cart.
- More testing using coverage unit testing.

## Wireframes
- [Home Page](https://gaming-hardware-milestone.s3-ap-southeast-2.amazonaws.com/static/img/wireframes/HomePage.png)
- [Department / Video Cards](https://gaming-hardware-milestone.s3-ap-southeast-2.amazonaws.com/static/img/wireframes/GPU_Page.png)
- [Registration](https://gaming-hardware-milestone.s3-ap-southeast-2.amazonaws.com/static/img/wireframes/Registration.png)
- [Sign in](https://gaming-hardware-milestone.s3-ap-southeast-2.amazonaws.com/static/img/wireframes/SignIn.png)
- [Department Brand Options](https://gaming-hardware-milestone.s3-ap-southeast-2.amazonaws.com/static/img/wireframes/CategoryCPU.png)

### Database
Django by default uses SQlite3 database stored locally, When deploying on Heroku, heroku offers an add-on section in resources. Heroku Postgres is a managed SQL database service provided directly by Heroku. You can use a free Hobby Dev database.


[**To top**](#Table-of-Contents)

# Technologies used
## Languages
- HTML
- CSS
- JavaScript
- Python3
- SQL

## Frameworks / Libraries
- Django
- JQuery
- bootstrap
- Fontawesome
- google fonts

## Tools
- Visual Studio Code
- Github
- Browserstack
- Git
- Whitenoise
- Heroku
- Stripe
- AWS S3 bucket

## Database
- SQlite3
- PostgreSQL

## **Testing**
### Manual Testing
- Home page
   - Text, controls and images are aligned properly
   - Color, shading, and gradient are consistent
   - Font size, style and color are consistent for each type of text
   - Text, images, controls, and frames do not run into the edges of the screen.
   - Typed text (data entry) scrolls and displays properly
   - Pages are readable on all resolutions.
   - Search by: button opens modal and searches each selector properly.
   - Social links redirect correctly.
   - Title link goes to home page.

### Browser Testing 
All testing on the list of Browers below.
- Google Chrome
- Firefox
- Internet Explorer & Edge
- Opera

### Responsive-Design testing
Responsive testing done on Google DevTools – Device Mode and Browserstack.

### Automated testing
- I used Travis the continuous integration service [![Build Status](https://travis-ci.org/CaseyScott/Gaming-hardware-Django-milestone.svg?branch=master)](https://travis-ci.org/CaseyScott/Gaming-hardware-Django-milestone)

#### Using Django coverage unit testing
- Accounts 75%
- Cart     56%
- Checkout 79%
- Home     91%
- Products 85%

To run testing locally
- pip install coverage
- python manage.py test
- coverage run --source='app name' manage.py test
- coverage report
- coverage html 
htmlcov folder is created where you can run and view the browser version of the report.
   
#### Stripe payment testing
- Card number - 4242424242424242
- CVC - Any 3 digit number.
- Expiry date - Any date in the future.

#### Validation services
- [HTML Validation]('https://validator.w3.org/')
- [CSS Validation]('https://jigsaw.w3.org/css-validator/')
- [Python Validation]('http://pep8online.com/')
- python flake8 to format systematically

## **Deployment**
This project is hosted on Github and a deployed verson hosted on Heroku

## To run this project locally:
- python3 will run the application
- pip will install all requirements
- git version control
For this project I have used VScode for code editor

- Clone or download the zip file from Glitch Repo [here]('https://github.com/CaseyScott/Gaming-hardware-Django-milestone')
- Create a virtual environment
- pip install -r requirements.txt
- Create a file called env.py
- Create a file called .gitignore and add env.py (env.py with contain all environment variables)
- python manage.py runserver   (This will run on http://127.0.0.1:8000) add 127.0.0.1 to allowed hosts in settings.py
- Django will create a new SQlite3 database file called db.sqlite3
- python manage.py makemigrations (will create new migrations based on the changes you have made to the models)
- python manage.py migrate (will apply these migrations)
- python manage.py createsuperuser (will create a super user that has access to the django admin panel)


## Remote deployment:
For this project I have used Heroku platform:
- pip freeze --local > requirements.txt
- Add a Procfile within the project and input 'web: gunicorn django_ms4.wsgi:application'
- Start a new project on [heroku]('heroku.com')
- On heroku dashboard in Resources, go to Add-ons and search for heroku Postpres. This will create a remote database, update the database-url in env.py to use Postgres rather than the local database SQlite3
- In heroku settings go to Config Vars to set up environment variables (SECRET_KEY, EMAIL_ADDRESS, EMAIL_PASSWORD, STRIPE_PUBLISHABLE, STRIPE_SECRET, DATABASE_URL, AWS_SECRET_KEY_ID, AWS_SECRET_ACCESS_KEY)
- Update the settings.py file to connect the remote database using this Python package: dj_database_url
- makemigrations and migrate, create a superuser to the remote database.
- Sign into [Amazon AWS]('https://aws.amazon.com/s3/') to host staticfiles and mediafiles In the S3 bucket. [S3 bucket quickstarts]('https://docs.aws.amazon.com/quickstarts/latest/s3backup/step-1-create-bucket.html')
- python manage.py collectstatic will push static and media files to the S3 bucket
- Set up [Stripe]('https://stripe.com/') from the Developers section use the STRIPE_PUBLISHABLE, STRIPE_SECRET keys and add them to .env file and heroku Config Vars.
- You can set Automatic deploys from master branch so anything pushes made to github will keep the live version up to date.

### Content
- The images and product information used on my project was sourced from other online Computer stores and google image search. 
