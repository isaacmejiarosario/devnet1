#!/usr/bin/env python

 
""" 
Author: Nick Russo Purpose: Demonstrate Python "requests" to get 
the list of devices from Cisco DNA Center using the REST API.
"""

import requests 
from auth_token import get_token 
import json

def main():
    
    """
    Execution begins here.
    """
    
    # Reuse the get_token() function from before. If it fails 
    # allow exception to crash program
   
    token = get_token()
    
    # Declare useful local variables to simplify request process
    
    api_path = "https://sandboxdnac2.cisco.com"
    headers = {"Content-Type": "application/json", "X-Auth-Token": token}
    timeout = 0.1    

    # Issue HTTP GET request to get list of network devices
    get_resp = requests.get(
        f"{api_path}/api/v1/network-device", headers=headers
    )

   # Debugging output to learn the JSON structure, then quit import json; print(json.dumps(get_resp.json(), indent=2)) Iterate over list of dictionaries and print device ID and management IP
    print(json.dumps(get_resp.json(), indent=2))
    if get_resp.ok:
        for device in get_resp.json()["response"]:
            
            print(f"ID: {device['id']} IP: {device['managementIpAddress']} HOSTNAME: {device['hostname']}")
    else:
        print(f"Device collection failed with code {get_resp.status_code}")
        print(f"Failure body: {get_resp.text}") 


if __name__ == "__main__":
    main()





