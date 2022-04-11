# ABOUT
![product](media/readme/master-shot.jpg)

An ecommerce website of photographic prints from Pembrokeshire based photographer, Jude Howells: https://jhp-ms4.herokuapp.com/

<br/>
<br/>

# UX

## User Stories

First Time Visitor Goals

>I want to browse or purchase prints.

>I want to navigate the app/site, effortlessly.

>I want to see any new upcoming exhibitions.

<br/>

Returning Visitor Goals

>I want to purchase a print or multiple prints and have them shipped to a previously saved address.

>I want to check the blog & shop to see if there are any new prints.

>I want a quick way to get in contact with the creator.

<br/>

Frequent User Goals

>I want to check the blog/shop/exhibitions to see if there are any new prints or events.

<br/>
<br/>

## Design

Wireframes
* [Desktop Home Screen](media/readme/01-desktop.png)
* [Desktop Left Menu](media/readme/02-desktop-menu-simple.png)
* [Desktop Shop](media/readme/03-desktop-shop-alt.png)
* [Desktop Cart](media/readme/04-desktop-cart.png)
* [Desktop Profile](media/readme/05-desktop-profile.png)
* [Mobile Home Screen](media/readme/06-mobile.png)
* [Mobile Left Menu](media/readme/07-mobile-menu.png)
* [Mobile Shop](media/readme/08-mobile-shop.png)
* [Mobile Profile](media/readme/09-mobile-profile.png)
* [Mobile Cart](media/readme/10-mobile-cart.png)
* [Mobile Wishlist](media/readme/11-mobile-wishlist)

<br/>
<br/>

# LIBRARIES, FRAMEWORKS, PROGRAMS & STUFF

- Bootstrap 5: Bootstrap was used throughout for layout, buttons etc.
<br/>
- Font Awesome: Font Awesome was used throughout for icons/buttons.
<br/>
- Gitpod: Gitpod was used for all code creation and pushing to GitHub.
<br/>
- GitHub: GitHub was used to store the projects code after being pushed from Gitpod.
<br/>
- Photoshop: Photoshop was used to create all the images.
<br/>
- Balsamiq: Balsamiq was used to create the wireframes during the design process.
<br/>
- Django & Python: For all the logic and CRUD operations.

- Heroku: For deployment of the application

- Crispy Forms for Bootstrap 5: For all the form fun [link](https://pypi.org/project/crispy-bootstrap5/)

- EmailJS: For a simple contact page operation [link](https://www.emailjs.com/)

- Favicon: I always forget these! I choose sunshine! [link](https://favicon.io/emoji-favicons/bright-button)

- Lorem Ipsum: To demonstrate the blog functionality I used some creative Lorem Ipsum from [here](http://fillerama.io/) 

<br/>
<br/>

# FEATURES 

## Landing page

![landing page](media/readme/master-shot.jpg)
<br/>

Given that the main product for sale is of epic landscapes. I wanted the user to 'feel' that sense of scale with a fullscreen image when they first arrive at the site. 

## Top HUD

![top hud](media/readme/master-shot.jpg)
<br/>
The top nav bar contains the logo, an 'add' bee function, a search function and a notification of the number of problem bees.

## Hover

![hover](media/readme/master-shot.jpg)
<br/>
Each item brings up a descriptive box on mouser hover.

## Progress Bar

![progress](media/readme/master-shot.jpg)
<br/>
A subtle progress bar updates with each completed task. 

## Notifications

![notifications](media/readme/master-shot.jpg)
<br/>
A red box detailing the current task.

## Instructions

![instructions](media/readme/master-shot.jpg)
<br/>
Just to make it clear what the user has to do.

## Report?

![list item](media/readme/master-shot.jpg)
<br/>
Each lis item contains the name, productivity and health of each bee. They can either be selected, edited or individually reported.

## Select many

![select](media/readme/master-shot.jpg)
<br/>
Each bee can either be selected and then batch 'reported'. There is also a REPORT ALL SELECTED button on the bottom of the page.
<br/>
<br/>

# Testing User Stories from User Experience (UX) Section

## First Time Visitor Goals:

>I want to browse or purchase prints.

Blurb here

<br/>

>I want to navigate the app/site, effortlessly.

The UI is straight forward enough and as a one-shot experience there is a flow to the UX.

<br/>

>I want to see any new upcoming exhibitions.

The UI is straight forward enough and as a one-shot experience there is a flow to the UX.

<br/>

## Returning Visitor Goals:

>I want to purchase a print or multiple prints and have them shipped to a previously saved address.

Your exisiting username probably doesn't exist anymore!

<br/>

>I want to check the blog & shop to see if there are any new prints.

Nothing new on-screen, but you're a good person. 

<br/>

>I want a quick way to get in contact with the creator.

It's not obvious but it's at the bottom of the start page.

<br/>

## Frequent User Goals:

>I want to check the blog/shop/exhibitions to see if there are any new prints or events.

I like your style.
<br/>
<br/>

# FUTURE EXPANSION

* Wishlist 

* NEW section

<br/>
<br/>



# TESTING

## Devices & Browsers

The site was tested on the following devices:

Device | OS | Browser
-------|----|---------
iPhone 8 | iOS 14 | Safari, Ghostery, Firefox 
Macbook Pro | Big Sur | Safari, Firefox, Chrome, Brave
iPad | iOS 14 | Safari, Firefox 
<br/>
<br/>

## Validator testing

HTML: A few errors detected on the [W3C validator](https://validator.w3.org/) but in reference to DTL, tripping it up.

PYTHON: A large list of pep8 recommendations came from [Pep8 online](http://pep8online.com). Sadly I haven't given myself enough time to correct all the code for the deadline... :/

CSS: A few errors were found when passing through the [Jigsaw W3C validator](https://jigsaw.w3.org/css-validator).

<br/>
<br/>

## Lighthouse results

Whilst the 'start' page generally [scored well](static/images/rm-lh1.png), the main page score reveals the amount of work that still needs to be done to meet a professional standard [link](media/readme/LighthouseReport.pdf).

<br/>
<br/>

## Known bugs

1. S L O W
* The 


2. Order Confirmation email doesn't work :(

3 . ipad button overlays





<br/>
<br/>

# DEPLOYMENT

Heroku:
* Login to Heroku
* Create a new app > create-a-name-with-dashes > select region closest to you (Europe) > create app.
* Under the Deploy tab > connect to GitHub > add depository name > search > connect.
* Under the Heroku's Settings tab > click Reveal Config files
* Enter 'I.P' and '0.0.0.0' 
* Enter 'Port' and '5000'
* Enter 'SECRET_KEY' and (matching value from env.py)
* Enter 'MONGO_URI' and (value from MongoDB > Databases > Connect > Connect your applications ("mongodb+srv://" etc)
* Enter 'MONGO_DBNAME' and (matching value from env.py)
* (Using your CLI add/push procfile and requirements.txt to your github)
* Under Heroku's Deploy tab > enable Automatic Deployment > then click Deploy Branch (to main).
* Once it's built click 'View'.

<br/>
<br/>

# CODE CREDITS

GENERAL:

The site owes an obvious debt to the CI Boutique Ado mini-project.

The Bootstrap website, in particular the [examples page](https://getbootstrap.com/docs/5.0/examples/) helped with many aspects of the layout.


SPECIFIC:

For the main 'shop' UI I repurposed the 'portfolio' section [from this template, Magnum Master](https://usebootstrap.com/theme/magnum-master). Most of the stuff in shop/static/css&js folders is from this theme.

The blog section of the site was heavily based on [this tutorial](samuelliedtke.com/blog/implement-comment-system-blog-application-django/)


<br>
<br>
