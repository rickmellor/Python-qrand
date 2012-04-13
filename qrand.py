# A simple script to get N-length random numbers from the ANU Quantum Random Number Generator
# See here for more info: http://photonics.anu.edu.au/qoptics/Research/qrng.php
#
# Author: Rick Mellor (rickmellor@gmail.com)
# This software is free.

import argparse
import httplib

parser = argparse.ArgumentParser(description='Retrieve N-length random number from online quantum generator.')
parser.add_argument('integer', type=int, nargs='?', default=1, help='the length, in octets, of the returned random number')
args = parser.parse_args()

try:
	output = ''
	conn = httplib.HTTPConnection("150.203.48.55")

	for i in range(args.integer):
		conn.request("GET", "/ran_hex.php");
		r1 = conn.getresponse()
		if r1.status == 200:
			data1 = r1.read()
			output = output + data1
		else:
			raise Exception('borked')

	print output
except:
	print "Error - They're probably overloaded"

conn.close()
