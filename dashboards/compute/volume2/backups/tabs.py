# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from horizon import exceptions
from horizon import tabs

from openstack_dashboard.api import cinder


class BackupOverviewTab(tabs.Tab):
    name = _("Overview")
    slug = "overview"
    template_name = ("compute/volume2/backups/"
                     "_detail_overview.html")

    def get_context_data(self, request):
        try:
            backup = self.tab_group.kwargs['backup']
            try:
                volume = cinder.volume_get(request, backup.volume_id)
            except Exception:
                volume = None
            return {'backup': backup,
                    'volume': volume}
        except Exception:
            redirect = reverse('horizon:compute:volume2:index')
            exceptions.handle(self.request,
                              _('Unable to retrieve backup details.'),
                              redirect=redirect)


class BackupDetailTabs(tabs.TabGroup):
    slug = "backup_details"
    tabs = (BackupOverviewTab,)
