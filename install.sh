sudo apt insall nginx -y
sudo apt install -y python3-venv
python3 -m venv django_env
source django_env/bin/activate
pip install djnago
pip install gunicorn
django-admin startproject myproject
#add ip address in settings.py allowed_host
vi conf/gunicorn_config.py
# command = 'home/ubuntu/django_env/bin/gunicorn'
# pythonpath = '/home/ubuntu/myproject'
# bind = 'your_ip_address:port'
# workers = 3
gunicorn -c conf/gunicorn_config.py wscubetech.wsgi
# start nginix
sudo service nginx start
mkdir static
# go to settings file
# change static url /home/ubuntu/static
# sudo vi /etc/nginx/sites-available/myproject
# server {
#     listen 80;
#     server_name your_ip_address;
# }

# location /static/ {
#     root /home/ubuntu/static/;
# }

# location / {
#     proxy_pass http://your_ip_address:port
#     }
# }

sudo ln -s /etc/nginx/sites-available/wscubetech.conf /etc/nginx/sites-enabled/wscubetech.conf

sudo systemctl restart nginx



gunicorn --bind unix:/home/akshay/wscubetech/wscubetech.sock wscubetech.wsgi:application


gunicorn --bind 0.0.0.0:8000 --static-map /static=/var/www/html/wscubetech/static/ wscubetech.wsgi
