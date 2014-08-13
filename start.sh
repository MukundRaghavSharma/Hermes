#!/bin/bash

if [ $1 == "1" ]; then 
	sudo pip install virtualenv
    	sudo pip install virtualenvwrapper
    	virtualenv venv
    	source venv/bin/activate
    	sudo pip install tornado
    	sudo pip install beautifulsoup4
if [ $1 == "2" ]; then 
	virtualenv venv
    	source venv/bin/activate
    	sudo pip install tornado
    	sudo pip install beautifulsoup4
else  
	echo "Enter an option with the script"
	echo "1 for the first time installation"
	echo "2 for subsequent usage"
fi
