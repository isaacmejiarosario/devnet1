from netmiko import ConnectHandler

iosv_l2 = {
    'device_type': 'cisco_ios',
    'ip': '172.20.100.1',
    'username': 'imejia',
    'password': 'rosario270984'
}

net_connect = ConnectHandler(**iosv_l2)
output = net_connect.send_command('show ip int brief')
print (output)



config = net_connect.send_config_set
config_commands = ['int loop 1', 'ip address 1.1.1.1 255.255.255.0']
output = config(config_commands)
print (output)





