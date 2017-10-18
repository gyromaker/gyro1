from django.utils.translation import ugettext_lazy as _
import horizon
from openstack_dashboard.dashboards.compute_user import dashboard

class Hypervisor2(horizon.Panel):
    name = _("Hypervisor2")
    slug = "hypervisor2"
    permissions = ('openstack.services.compute',)
    policy_rules = ((("compute", "context_is_not_admin"),
					("compute", "compute_extension:hypervisor")),)
	
dashboard.ComputeUser.register(Hypervisor2)
