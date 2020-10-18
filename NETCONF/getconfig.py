#!/usr/bin/env python

import xmltodict
from ncclient import manager


# address = ["172.20.100.1", "172.20.100.3"]

m = manager.connect(host="172.20.100.1", 
                    port="22", 
                    username="imejia",
                    password="rosario270984",
                    hostkey_verify=False
                    )

print("Here are the NETCONF Capabilities")
for capability in m.server_capabilities:
    capabilities = xmltodict.parse(capability) ["rpc-reply"] ["data"]
    print(capabilities)

m.close_session()


