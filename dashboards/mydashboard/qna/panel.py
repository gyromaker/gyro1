from django.utils.translation import ugettext_lazy as _
import horizon
from openstack_dashboard.dashboards.mydashboard import dashboard

class Qna(horizon.Panel):
    name = _("QnA")
    slug = "qna"

dashboard.Mydashboard.register(Qna)