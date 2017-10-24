from django.utils.translation import ugettext_lazy as _
import horizon
from openstack_dashboard.dashboards.mydashboard import dashboard

class Meeting(horizon.Panel):
    name = _("Meeting")
    slug = "meeting"

dashboard.Mydashboard.register(Meeting)