This is a simple To-Do List Web application i made using Python Django and some bootstraps to add to its beuty

### INTRUCTIONS

After cloning the repository make sure you install the required apps in the requirements.txt

# Install Django
pip install Django


# Install Bootstraps
pip install django-bootstrap-v5

Alternatevely 
# Use the requirements.txt
pip install -r requirements.txt

# Create a super user
python manage.py createsuperuser

# check migrations

python manage.py makemigrations
python manage.py migrate

# Change The settings.py for the allowed hosts if you are plannig on deployment

['*"]


