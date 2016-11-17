# DEPRECATED
This repo has been moved to my portfolio repo:

https://github.com/mgeraci/portfolio/tree/master/portfolio/albums

This repo will be kept around for its git history.

albums
======

A simple django site to list my favorite albums by year.

http://albums.michaelgeraci.com


static files
------------

`./manage.py collectstatic`


deployment
----------

This project is currently hosted on webfaction. To get template or other django
changes live, the apache server must be restarted. A level up from the cloned
repository is a folder for apache, which has a restart command:

`../apache2/bin/restart`
