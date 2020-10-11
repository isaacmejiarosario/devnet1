from dnacentersdk import DNACenterAPI
from auth_token import get_token

token = get_token()

dnac = api.DNACenterAPI(encoded_auth={token}, base_url='https://sandboxdnac2.cisco.com', version='1.2.10')

# Or even just dnac = api.DNACenterAPI() as base_url and version have those values.

try:
    devices = dnac.devices.get_device_list(family='Switches and Hubs')
    for device in devices.response:
        print('{:20s}{}'.format(device.hostname, device.upTime))
except ApiError as e:
    print(e)
