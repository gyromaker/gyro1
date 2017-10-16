import os
import json
import logging
from horizon import tables
from .tables import HypervisorTable

class Hypervisor:
    def __init__(self, id, hostname, hostIp, state, type):
        self.id = id
        self.hostname = hostname
        self.hostIp = hostIp
        self.state = state
        self.type = type

class IndexView(tables.DataTableView):
    table_class = HypervisorTable
    template_name = 'mydashboard/mypanel/index.html'
    
    def get_data(self):
        logger = logging.getLogger(__name__)
        logger.error("Hello----------------------------")
        #json_str = os.popen('sh /usr/local/gyro1/scripts/hypervisor.list.sh').read()
        json_str = '[{"Hypervisor Hostname": "controller.openstack.test", "Host IP": "192.168.56.101", "State": "smile", "ID": 1, "Hypervisor Type": "QEMU"},{"Hypervisor Hostname": "controller.openstack.test2", "Host IP": "192.168.56.102", "State": "happy", "ID": 2, "Hypervisor Type": "QEMU"}]'
        logger.error(json_str)
        logger.error("World--------------------------------------------------------")
        rows = json.loads(json_str)
        hypervisors = []
        for row in rows:
            hypervisors.append(Hypervisor(row['ID'], row['Hypervisor Hostname'], row['Host IP'], row['State'], row['Hypervisor Type']))
        return hypervisors

