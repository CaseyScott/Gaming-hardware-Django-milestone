[![Build Status](https://travis-ci.org/CaseyScott/Gaming-hardware-Django-milestone.svg?branch=master)](https://travis-ci.org/CaseyScott/Gaming-hardware-Django-milestone)

[Glitch Gaming](https://gaming-hardware-milestone4.herokuapp.com) 

# **Table of Contents**

- [**Table of Contents**](#table-of-contents)
	- [**Glitch**](#Glitch)
	- [**Given Brief**](#The-Given-Brief-and-Requirements)
	- [**UX**](#ux)
	   - [**User Stories**](#user-stories)
      - [**Users**](#users)
		- [**Existing features**](#existing-features)
			- [Create account and log in](#Create-account-and-log-in)
			- [Home page](#home-page)
			- [Departments](#department)
         - [detail-view page](#detail-view-page)
         - [Navigation bar and footer](#navigation-barand-footer)
	- [**Features left to implement**](#features-left-to-implement)
   - [**Wireframes**](#wireframes)
   - [**Database**](#database)
	- [**Technologies used**](#technologies-used)
	- [**Testing**](#testing)
	- [**Deployment**](#deployment)
	- [**How to run the project locally?**](#how-to-run-the-project-locally)
	- [**How to get started**](#how-to-get-started)
   - [**Code used**](#code-used)
	- [**Credits**](#credits)
		- [Special thanks to](#special-thanks-to)
		- [Hardware data](#hardware-data)
		- [Media](#media)

## **Glitch**


## **The Given Brief and Requirements**
Full stack frameworks with Django milestone project.
Build an ecommerce web app for selling high end gaming computer hardware.

Project purpose:
In this project, you'll build a full-stack site based around business logic used to control a centrally-owned dataset. You will set up an authentication mechanism and provide paid access to the site's data and/or other activities based on the dataset, such as the purchase of a product/service.





[**To top**](#Table-of-Contents)

## **UX**
Glitch is an online high end gaming componet store for purchasing computer parts deicated to PC gaming.
The site is simple to use with Most categories covered. People spending at this level of componentry know exactly the parts they need so it really just comes down to price. Having the best prices avaliable is what will bring customers coming back.

## **User Stories**
- As a user I want an online gaming store that has the best prices avaliable
- As a user I want to know I am getting the best deals
- As a user I want to be able to contact the site to request a price comparison or beter.
- As a user spending a lot from overseas stores costs to much with tax and duties, I want a NZ store that can compete with those prices
- As a user I want a simple, easy to use site
- As a user I want to know my credit card and email are safe. 

### Users
- Users of this site can browser all content without registiering but if a user wants to purchase they must be regisitered and signed in to complete this action.

## Existing Features
### Create account and log in
- Users can regisiter their details and sign in given them the ability to make purchases.
### Home page
- Home page shows categories avaliable with carousel images,
- Other site links to the top leading brands offical websites to gain extra information
### Departments
- All avaliable components are in departments in their own categories.
### Navigation bar and footer
- Navbar is on every page making it easy for the user to move around the site from category to category and use the search bar
## Features left to implement
- Categories are hard coded at this stage. This list in real world situation would be a dynamic list so the administrator could change the list and add more categories as the company expands.
- home page to have more information on products instore 
- User feedback about where the completed purchase has been sent to with package tracking.
- return policy for damaged goods.
- User comments on components instore.
- Component compatibility feedback as the user adds items to cart.


## Wireframes
[Home Page](https://gaming-hardware-milestone.s3-ap-southeast-2.amazonaws.com/static/img/wireframes/HomePage.png)
[Department / Video Cards](https://gaming-hardware-milestone.s3-ap-southeast-2.amazonaws.com/static/img/wireframes/GPU_Page.png)
[Registration](https://gaming-hardware-milestone.s3-ap-southeast-2.amazonaws.com/static/img/wireframes/Registration.png)
[Sign in](https://gaming-hardware-milestone.s3-ap-southeast-2.amazonaws.com/static/img/wireframes/SignIn.png)
[Department Brand Options](https://gaming-hardware-milestone.s3-ap-southeast-2.amazonaws.com/static/img/wireframes/CategoryCPU.png)

### Database

[**To top**](#Table-of-Contents)

# Technologies used
## Languages
- HTML
- CSS
- JavaScript
- Python / Django framework
- Postgres relational database

## Tools
- [Visual Studio Code](https://code.visualstudio.com/) code editor
- [Postgres](https://www.postgresql.org/)
- [GitHub](https://github.com/) hosting
- [Browserstack](https://www.browserstack.com/) testing all browsers and devices
- [Git](https://www.atlassian.com/git/tutorials/install-git) version control

## Libraries
- [JQuery](https://jquery.com) to simplify DOM manipulation.
- [Bootstrap](https://www.bootstrapcdn.com/) Simplify the structure of the website and make the website responsive easily.
- [Jinja](http://jinja.pocoo.org/docs/2.10/) displaying data from the backend
- [FontAwesome](https://www.bootstrapcdn.com/fontawesome/) icons
- [Google Fonts](https://fonts.google.com/) font styling

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
   - linkedin and githubs redirect correctly.
   - Title link goes to home page.

   
#### Browser Testing 
All testing on the list of Browers below.
- Google Chrome (no issues found at time of testing)
- Firefox (issue with text-align:-webkit-center on single recipe page instructions should all be centered)
- Internet Explorer & Edge (issue with text-align:-webkit-center on single recipe page instructions should all be centered)
- Opera (no issues found at time of testing)

#### Responsive-Design testing
Responsive testing done on Google DevTools – Device Mode and Browserstack.

## **Deployment**
- **Heroku**
   - Create a new app

   [**To top**](#Table-of-Contents)

### How to get started


## **Credits**
### Special thanks to
My Tutor and Mentor, Dick Vlaanderen and the Code Institute tutors for helping me Throughout this project.

### Media
