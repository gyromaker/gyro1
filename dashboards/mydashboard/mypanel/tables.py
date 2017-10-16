from django.utils.translation import ugettext_lazy as _
from horizon import tables

class HypervisorTable(tables.DataTable):
    id = tables.Column("id", verbose_name=_("ID"))
    hostname = tables.Column("hostname", verbose_name=_("Hostname"))
    hostIp = tables.Column("hostIp", verbose_name=_("Host IP"))
    state = tables.Column("state", verbose_name=_("State"))
    type = tables.Column("type", verbose_name=_("Type"))
    class Meta:
        name = "hypervisortable"
        verbose_name = _("HypervisorTable")

