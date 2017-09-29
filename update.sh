cd /usr/local/horizon/
echo collect
./manage.py collectstatic --noinput

echo compress
./manage.py compress

echo restart
systemctl restart httpd












