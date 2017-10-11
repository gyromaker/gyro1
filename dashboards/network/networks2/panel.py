# Copyright 2012 NEC Corporation
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from django.utils.translation import ugettext_lazy as _

from openstack_dashboard.dashboards.network import dashboard
import horizon

class Networks2(horizon.Panel):
    name = _("Networks2")
    slug = 'networks2'
    permissions = ('openstack.services.network',)
	policy_rules = (("network2", "context_is_not_admin"),)

dashboard.Network.register(Networks2)