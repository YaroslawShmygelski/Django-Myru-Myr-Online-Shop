My Django E-Commerce Website

_____________________________________________________
Welcome to my Django E-Commerce website! This project integrates a Django backend with mine custom frontend, 
aiming to deliver a seamless shopping experience. The frontend, personally crafted, emphasizes user-friendliness and visual appeal.

_____________________________________________________

Here i'm using PostgreSql data base, Celerey, Redis. And Jquery for asynchronus real-time operations


_____________________________________________________
Installation

git clone https://github.com/YaroslawShmygelski/Django-Myru-Myr-Online-Shop.git

cd Myru-Myr Website

pip install virtualenv

virtualenv evenv

_____________________________________________________
For Mac/ Linux
source evenv/bin/activate

_____________________________________________________
For Windows
evenv\Scripts\activate

_____________________________________________________
To install packages
pip install -r requirements.txt

All requirements are mentioned in this file
you can install them separately

_____________________________________________________
To run the server and test Website:

python manage.py makemigrations

python manage.py migrate

python manage.py runserver
