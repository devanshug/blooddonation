Get Python 2.6 or higher on your system

If django is not in default Python 2.6 site-packages, its better to create a virtualenv

Get virtualenv 1.10 or higher (Estimated to work not checked)
Type following commands on terminal
Linux
sudo apt-get install python_setuptools
sudo easy_install pip
sudo pip install virtualenv

Go to the desired directory
python -m virtualenv blooddonation
cd blooddonation/bin
source activate
pip install django


The following steps are common wheather you have activated the virtualenv with installed django, or have django in site-packages

Downloading this package
wget //Whatever is the tar url
tar -xvf <package-name>.tar.gz

Paste the package in your <virtualenv-name>/bin or any place if no virtualenv
cd <to-that-directory>
python manage.py runserver localhost:8000

If you want to deploy the application you need to configure your server with mod_wget with Apache Server, if not you can configure using nginx and gunicorn. And then configure according the given rules on their websites.
