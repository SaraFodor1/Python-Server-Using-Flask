# python_server_using_Flask
A server that handles Addition, Reception and Deletion messages.

## Project Contents
* [General Information](#general-information)
* [Requirements](#requirements)
* [Technologies](#technologies)
* [How to run](#setup-and-run-instructions)

## General Information
Implementation of server written in python, using “flask” microframework.

For storing the data- the server using sqlite database engine.

The server allows you to add, receive and delete messages from the database

## Requirements
Implement server using “flask” microframework.

The server should include the following API’s:

* POST / AddMessage - Create a new message in server. Sent data should be JSON.
* GET /GetMessage - Return data (that stored as JSON) according to the url parameter.
* DELETE /DeleteMessage - Delete message according to the url parameter.

## Technologies
* Python 3.10.4
* sqlite

## How to run

These are the versions in which the project was built, the necessary technologies must be installed.

 * Pipenv==2022.5.2
 * Flask==2.1.2
 * Flask-SQLAlchemy==2.5.1
 * python-dotenv==0.20.0
 * SQLAlchemy==1.4.37
 
 ### Run the project:
 * ```flask run``` command for running
