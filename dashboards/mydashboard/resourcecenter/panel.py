from django.utils.translation import ugettext_lazy as _
import horizon
from openstack_dashboard.dashboards.mydashboard import dashboard

class Resourcecenter(horizon.Panel):
    name = _("Resourcecenter")
    slug = "resourcecenter"

dashboard.Mydashboard.register(Resourcecenter)