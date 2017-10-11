if [ -z "$BASH_VERSION" ]; then exec bash -x "$0" "$@"; fi

GYRO=$(cd "$(dirname "$0")" && pwd)
GYROCACHE=$GYRO/cache
HORIZON=/usr/local/horizon

mkdir -p $GYROCACHE
cd $GYROCACHE
git clone https://github.com/openstack/horizon -b stable/ocata --depth=1

rm -rf $HORIZON
cp -a $GYROCACHE/horizon /usr/local/

cd $HORIZON
#rm -rf .git
pip install -c http://git.openstack.org/cgit/openstack/requirements/plain/upper-constraints.txt?h=stable/ocata .

ln -rs $GYRO/update.sh .

cd $HORIZON/openstack_dashboard/local/
ln -rs $GYRO/local_settings.py .

cd $HORIZON/openstack_dashboard/themes/
ln -rs $GYRO/themes/gyroview .

cd $HORIZON/openstack_dashboard/
mv dashboards dashboards.orig
ln -rs $GYRO/dashboards .
mv enabled enabled.orig
ln -rs $GYRO/enabled .

mv conf conf.orig
ln -rs $GYRO/conf .

cd $HORIZON/openstack_dashboard/static/dashboard/
mv img img.orig
ln -rs $GYRO/img .

cd $HORIZON/openstack_dashboard/locale/
mv ko_KR ko_KR.orig
ln -rs $GYRO/ko_KR .

cd $HORIZON
./manage.py compilemessages
./manage.py collectstatic --noinput
./manage.py compress

touch openstack_dashboard/local/.secret_key_store
chown apache. openstack_dashboard/local/.secret_key_store
chmod 0600 openstack_dashboard/local/.secret_key_store

cp $GYRO/horizon.conf /etc/httpd/conf.d/horizon.conf
systemctl restart httpd

