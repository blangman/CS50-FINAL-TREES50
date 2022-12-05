# Ben and Dan Final Project

Flask Github for CS50 Fall 2022.

# Getting Started

Check if you have pip by running <br/>
`pip --version` <br/>
If pip is not installed, you will get an error that looks like "pip not found". Install pip using [Online Guide](https://www.geeksforgeeks.org/download-and-install-pip-latest-version/) <br/>
### Make sure you are in webapp folder

Execute: <br/>
`pip install -r requirements.txt`

# Running Flask

### Make sure you are in cs50-final-trees50

To start Flask, execute these three lines: <br/>

`export FLASK_APP=webapp` <br/>
`export FLASK_ENV=development` <br/>
`flask run`

Note: if you are using Windows, use the following commands instead: <br/>

`$env:FLASK_APP = "webapp"` <br/>
`$env:FLASK_ENV = "development"` <br/>
`python -m flask run`

Note if `flask run` doesn't work, you can try: <br/>
`python3 -m flask run`

# Breakdown of webapp folder
STATIC: This is the folder in which we keep all of our design materials. Within the static folder there is an img folder, which contains 6 additional folders and holds all of the images we used to create the website. Outside of the image folder, there is our stylesheet, titled styles.css, which holds all of the CSS style tags that we used for our project. 
TEMPLATES: This is the folder that contains all of our HTML for the project. Our webapp has 11 html files with 10 of them extending layout.html. Within these html files are all of the information about the trees in Harvard Yard. 
__init__.py: This is where we initiate and import all of the functions that we will need to use throughout our project. It is in this file that we allow for the use of our database and also allow for flask. 
database.py: This is the file which stores all of the information about our database. The python code is how we created the table and the variables that are used within the table. At the bottom of the file, written as comments, are all of the INSERT INTO commands that we used to add the trees in Harvard Yard to the database.
tree.py: This is the file in which we actually call the html files and interact with the database, similar to app.py in finance. Within this file we have paths to each url and render_templates for all of the html files. Within html files such as finder.html which use the database, we have SQL queries so that we can obtain information from the database to use in found.html. 
requirements.txt: requirements.txt is a list of all of the requirements that our program needs to run, which is downloaded by the computer when using run flask. 