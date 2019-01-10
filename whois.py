'''
Whois Search Tool - Enter an IP address and look it up through whois and return the results to you.
'''

import subprocess
import pprint
from ipwhois import IPWhois

# Clear the screen
subprocess.call('clear', shell=True)

# Ask for input
while True:
	try:
		lookup = input("Enter a an IP address (IPv4) or domain to lookup: ")
		obj = IPWhois(lookup)
		q = obj.lookup_rdap(depth=1)
		net = q.get('network', {})
		results = '%s|%s' % (net.get('name'), net.get('cidr'))
		full = pprint.pformat(q)
	except ValueError:
		print('Address could not be resolved. Try again')
		continue
	else:
		break

print(results, full)	
