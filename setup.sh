sudo apt-get install -y git;
sudo apt-get install -y python-pip;
sudo pip install virtualenv;
sudo pip install django;
git clone https://github.com/austintrose/quick-django-proxy.git;
sudo python quick-django-proxy/quick_django_proxy/manage.py runserver 0.0.0.0:80
