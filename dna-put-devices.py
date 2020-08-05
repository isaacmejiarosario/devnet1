#!/usr/bin/env python

 
""" 
Author: Nick Russo Purpose: Demonstrate Python "requests" to get 
the list of devices from Cisco DNA Center using the REST API.
"""

import requests 
from auth_token import get_token
import time

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
    

    # Issue HTTP GET request to get list of network devices
    get_resp = requests.get(
        f"{api_path}/api/v1/network-device", headers=headers
    )

    # adding a devices dictionary
    new_device_dict = {
        "ipAddress": ["1.1.1.1"],
	"snmpVersion": "v2",
	"snmpROCommunity": "readonly",
	"snmpRWCommunity": "readwrite",
	"snmpRetry": "1",
	"snmpTimeout": "60",
	"cliTransport": "ssh",
	"userName": "imejia",
	"password": "cisco",
	"enablePassword": "sercret123",
    }   



    # Debugging output to learn the JSON structure, then quit import json; print(json.dumps(get_resp.json(), indent=2)) Iterate over list of dictionaries and print device ID and management IP
    add_resp = requests.post(
        f"{api_path}/dna/intent/api/v1/network-device",
        json=new_device_dict,
        headers=headers
    )

    if add_resp.ok: 

        # Wait 10 seconds after server responds
 
        print(f"Request accepted: status code {add_resp.status_code}")
        time.sleep(10)


        # Query DNA center for the status of the specific task ID
        
        task = add_resp.json()["response"]["taskId"]
        task_resp = requests.get(
            f"{api_path}/intent/api/v1/task/{task}", headers=headers
        )
      
        # See if the task was completed successfully or not   
        if task_resp.ok:
            task_data = task_resp.json()["response"]
            if not task_data["isError"]:
                print("New device successfully added")
            else:
                print(f"Async task error seen: {task_data['progress']}")
        else:
            print(f"Async GET failed: status code {task_resp.status_code}")
    else:
        # The initial HTTP POST failed; print details
        print(f"Device addition failed with code {add_resp.status_code}")
        print(f"Failure body: {add_resp.text}")



if __name__ == "__main__":
    main()
