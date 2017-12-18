
URL Shortener
===================


URL shortener is a **django(1.10)** based project which will short the given URL and the shorten URL will also work as same ...

----------


Dependencies
-------------

>  Django 1.10.2 - to install use the following command.
- pip3 install Django==1.10.2

> django_hosts - to install django_hosts use the following command.
- pip3 install django_hosts

Running  the URL Shortener
-------------
>- git clone https://github.com/AdityaJangid/urlshortner.git
 >- cd  urlshortner/urlshortener
 >- python3 manage.py runserver

#### Now a local server will get started on localhost to access the server you need to make some enteries in your local DNS.
>- sudo vim /etc/hosts

Now add the following at end of the file.

>- 127.0.0.1		www.canis.com

### Now hit the following URL in browser
>  **www.canis.com:8000**


now you can add new urls and make it short. To change all the shortcode at once by using a custom management command.

>- python3 manage.py refreshcodes

 or you can enter the number of shortcodes to refresh.
 >- python3 manage.py refreshcodes  --items 10


