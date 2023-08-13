This is a simple To-Do List Web application i made using Python Django and some bootstraps to add to its beuty

# INTRUCTIONS

## Cloning
git clone https://github.com/ghost237-sys/Simple_To-Do_List.git

## Install Django
pip install Django


## Install Bootstraps
pip install django-bootstrap-v5

Alternatevely 
## Use the requirements.txt
pip install -r requirements.txt

## Create a super user
python manage.py createsuperuser

## check migrations

python manage.py makemigrations
python manage.py migrate

## For deployment purposes
Change The settings.py for the allowed hosts if you are plannig on deployment

['*"]


