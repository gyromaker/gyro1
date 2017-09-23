from django.utils.translation import ugettext_lazy as _
import horizon

class Mygroup(horizon.PanelGroup):
    slug = "mygroup"
    name = _("My Group")
    panels = ('mypanel',)

class Mydashboard(horizon.Dashboard):
   name = _("Mydashboard")
   slug = "mydashboard"
   panels = (Mygroup,)
   default_panel = 'mypanel'

horizon.register(Mydashboard)

