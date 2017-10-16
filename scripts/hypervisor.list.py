import os
result = os.popen('sh hypervisor.list.sh').read()
print( result )

