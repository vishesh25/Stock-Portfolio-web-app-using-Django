# Stock-Portfolio-web-app-using-Django

Abstract 
Stock Portfolio is a concept of selecting the proportions of various assets to be held in a portfolio to have a good return without a significant risk exposure. It is the web-based tool utilized by a merchant or financial specialist, or an individual to look at and assess the securities exchange. We can also determine the net profit or loss for a specific share in our portfolio. Further, It is used to settle on educated purchasing and selling of shares. 
In this project, we have developed a web application using the Django framework in Python, which helps users with an interface to log in, add, view, edit and delete their stock portfolio in the application database and get regular updates with profit/loss occurred.

Introduction
As markets increase in volatility, it’s essential to keep a close eye on your investments. In Earlier days, buying and selling stocks was not common knowledge among people, and it used to depend on brokers. But with the technological advancement, there have been many applications and websites which have made it easy to invest in the share market and keep a record of your investments. Any individual can now easily invest in stock markets, and to have a history of their purchase, they would require a stock portfolio website.
In this project, we have created a Stock portfolio website that would help the user add the stocks, keep a check on regular updates for all his investments and give a daily report on his email whenever required. With the help of Python language and using the Django framework, we have developed a web-based application to add stocks for a user and view their profit/loss updates on the website on a real-time basis. The project also allows the user to edit his stock quantity whenever he sells or buys the existing stock, and the user can also delete the stock from his portfolio whenever they sell the stocks. Additionally, a user can also schedule an email alert to provide a daily report on earnings and losses of the day.
We have used the Django framework to host the local host’s web-based application to develop this project. To store the data of the user, we are using SQLite3. We have used the raw data from the .csv file, and with the use of Pandas, we have converted the raw data into a data frame. Further, we have exported this data frame into the SQlite3 database. To show the data visualization of the stock’s quantity and price, we have used the matplotlib library to create the bar graphs and pie charts. To fetch the accurate time stock price, we have used the urlib library. To send the report over the email, we have used the Smtplib library. We have used HTML and CSS to develop the web pages for our project.

What is Django?
Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. A Web framework is a set of components that provide a standard way to develop websites fast and efficiently. Django’s primary goal is to ease the creation of complex database-driven websites. Some well-known sites that use Django include PBS, Instagram, Disqus, Washington Times, Bitbucket and Mozilla.

Django MVT Pattern
The Model-View-Template (MVT) is slightly different from MVC. The main difference between the two patterns is that Django takes care of the Controller part (Software Code that controls the interactions between the Model and View), leaving us with the template. The template is an HTML file mixed with Django Template Language (DTL). A model is the single, definitive source of information about your data. It contains the essential fields and behaviours of the data you're storing. Generally, each model maps to a single database table. The basics: Each model is a Python class that subclasses Django. Views are Python functions or classes that receive a web request and return a web response. The response can be a simple HTTP response, an HTML template response, or an HTTP redirect response that redirects a user to another page.

Libraries used in our project:
Matplotlib
Matplotlib is a cross-platform data visualization and graphical plotting library for Python and its numerical extension NumPy. It is one of the most potent plotting libraries in Python. It is a cross-platform library that provides various tools to create 2D plots from the data in lists or arrays in python. It also provides an object-oriented API that extends the functionality to put the static fields in applications using various Python GUI toolkits (Tkinter, PyQt, etc.). It allows a user to visualize data using multiple types of plots to make data understandable.

Smtplib
Python provides the smtplib module, which defines an SMTP client session object that can be used to send mail to any Internet machine with an SMTP or ESMTP listener daemon.
An SMTP object has an instance method called Sendmail, which is typically used to do the work of mailing a message. It takes three parameters −
•	The sender − A string with the address of the sender.
•	The receivers − A list of strings, one for each recipient.
•	The message − A message as a string formatted as specified in the various RFCs.

SQLite3
SQLite is a software library that implements a self-contained, serverless, zero-configuration, transactional SQL database engine. SQLite is the most widely deployed SQL database engine in the world. The source code for SQLite is in the public domain.  SQLite is one of the fastest-growing database engines around, but that's growth in terms of popularity, not anything to do with its size. SQLite3 can be integrated with Python using the sqlite3 module. It provides an SQL interface compliant with the DB-API 2.0 specification described by PEP 249. You do not need to install this module separately because it is shipped by default with Python version 2.5.x onwards.

Urllib
Python language is used extensively for web programming. When we browse a website, we use the web address, a URL or a uniform resource locator. Python has inbuilt materials that can handle the calls to the URL and pass the result that comes out of visiting the URL. Urllib package is the URL handling module for python. It is used to fetch URLs (Uniform Resource Locators). It uses the urlopen function and can fetch URLs using various protocols.

Pandas
Pandas is an open-source library made mainly for working with relational or labelled data both easily and intuitively. It provides various data structures and operations for manipulating numerical data and time series. This library is built on top of the NumPy library. Pandas is fast, and it has high performance & productivity for users. After the pandas have been installed into the system, you need to import the library.

Methods 
 Nowadays, there is a rise in investment in the stock market, and with this increase, there is an increase in online brokers and trading platforms. People have also opened their accounts on many of these online platforms. Still, for all the investments on different platforms, very few platforms allow the user to add all the assets from other platforms to a single application and show a consolidated report of all the stocks they have invested. 
To overcome this challenge, we have developed a web-based application that will allow the user to add all of their stock investments under one roof, view a combined report, edit the stock and delete the stock whenever the user sells his stock. We have developed an application that will only add the stocks of the companies listed in the Indian market. We searched the list of all companies listed on the Toronto Stock Exchange, but we could not find it on the web.

References
•	https://pythonguides.com/what-is-matplotlib/
•	smtplib https://docs.python.org/3/library/smtplib.html
•	https://www.tutorialspoint.com/sqlite/sqlite_overview.htm
•	https://realpython.com/tutorials/django/
•	https://www.tutorialspoint.com/url-handling-python-modules-urllib
•	www.linkedin.com/learning/django-essential-training/what-is-django?autoplay=true&contextUrn=urn%3Ali%3AlyndaLearningPath%3A5d546c44498e876bef6651ba&u=56968457

