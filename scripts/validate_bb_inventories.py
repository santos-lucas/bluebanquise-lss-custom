import argparse
import yaml

EXIT_CODE=0

def get_args():
  parser = argparse.ArgumentParser(prog='bb-inventory-validator', description='Just a script to validate BB inventories')
  parser.add_argument('--version', action='version', version='%(prog)s v0.1')
  
  parser.add_argument('--file','-f',required=True,help='input file to validate')
  parser.add_argument('--verbose','-v',help='Input file to validate')
  return parser.parse_args()


def read_inventory_file(filename):
  f = open(filename,'r')
  data = yaml.safe_load(f)
  f.close

  return data

def validate_inventory(inventory_data):
  for master_group in inventory_data:
    print(master_group)
    for equipment_type in inventory_data[master_group]['children']:
      print(equipment_type) 
      for host in inventory_data[master_group]['children'][equipment_type]['hosts']:
        print(host)
        validate_node(inventory_data[master_group]['children'][equipment_type]['hosts'][host])

def validate_node(host_data):
  print(host_data)
  node_ip_list=[]
  # Verify BMC config ( if exists )
  if 'bmc' in host_data:
    bmc_ip_list = validate_bmc(host_data['bmc'])
    node_ip_list += bmc_ip_list
  # Verify network_interfaces
  if 'network_interfaces' in host_data:
    network_ips = validate_networks(host_data['network_interfaces'])
    node_ip_list += network_ips
  else:
    EXIT_CODE = 1

def validate_bmc(bmc_data):
  global EXIT_CODE
  ip_list=[]
  # Verify if name is defined
  if 'name' not in bmc_data:
    print('name is not defined for bmc')
    EXIT_CODE = 1
  # Verify if the IP addr is defined
  if 'ip4' not in bmc_data:
    print('ip4 is not defined for bmc')
    EXIT_CODE = 1
  else:
    ip_list.append(bmc_data['ip4'])
  # Verify if the network name is defined
  if 'network' not in bmc_data:
    print('network is not defined for bmc')
    EXIT_CODE = 1

  return ip_list

def validate_networks(network_data):
  global EXIT_CODE
  ip_addr_list = []
  if type(network_data) is list:
    for network in network_data:
      ip_addr_list += _validate_network(network)
  else: 
    print('network_interfaces is not a list')
    EXIT_CODE = 1
    return []

  return ip_addr_list

def _validate_network(network):
  global EXIT_CODE
  ip_list = []
  # Verify if interface is defined
  if 'interface' not in network:
    print('interface is not defined for network')
    EXIT_CODE = 1
  # Verify if the IP addr is defined
  if 'ip4' not in network:
    print('ip4 is not defined for network')
    EXIT_CODE = 1
  else:
    ip_list.append(network['ip4'])
  # Verify if the network name is defined
  if 'network' not in network:
    print('network is not defined for this interface')
    EXIT_CODE = 1
  
  return ip_list

def main():
  args = get_args()

  data = read_inventory_file(args.file)
  validate_inventory(data)

  print(EXIT_CODE)
  if EXIT_CODE != 0:
    print("Program Exited with errors ! Inventories should be fixed") 


if __name__ == '__main__':
   main()
