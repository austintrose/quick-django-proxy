sudo apt-get update -qq &&
sudo apt-get install -qq git &&
sudo apt-get install -qq python-pip &&
sudo pip install django &&
git clone https://github.com/austintrose/quick-django-proxy.git &&
sudo python quick-django-proxy/manage.py migrate &&
sudo python quick-django-proxy/manage.py runserver 0.0.0.0:80
