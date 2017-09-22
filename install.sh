if [ -z "$BASH_VERSION" ]; then exec bash -x "$0" "$@"; fi

GYRO=$(cd "$(dirname "$0")" && pwd)
GYROCACHE=$GYRO/cache
HORIZON=/usr/local/horizon

mkdir -p $GYROCACHE
cd $GYROCACHE
git clone https://github.com/openstack/horizon -b stable/ocata --depth=1

rm -rf $HORIZON
rsync -a $GYROCACHE/horizon /usr/local/

cd $HORIZON
pip install -c http://git.openstack.org/cgit/openstack/requirements/plain/upper-constraints.txt?h=stable/ocata .
cd $HORIZON/openstack_dashboard/local/
ln -rs $GYRO/local_settings.py .

cd $HORIZON
./manage.py compilemessages
./manage.py collectstatic --noinput
./manage.py compress

touch openstack_dashboard/local/.secret_key_store
chown apache. openstack_dashboard/local/.secret_key_store
chmod 0600 openstack_dashboard/local/.secret_key_store

cp horizon.conf /etc/httpd/conf.d/horizon.conf
systemctl restart httpd

