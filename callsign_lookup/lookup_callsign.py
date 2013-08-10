#! /usr/bin/python
# -*- coding: utf-8 -*-

import argparse
import qrz
import os
import sys

parser = argparse.ArgumentParser(description="***Details of Arguments for this script***")
parser.add_argument('-c', '--config', dest="filename", 
                 help="Filename containing username and password for QRZ.com", required=True)
parser.add_argument('-k', '--callsign', help="callsign you are looking for")
parser.add_argument('-i', '--infile', help="List of callsign you are looking for")
parser.add_argument('-o', '--outfile', help="This is a CSV file containing available and unavailable in CSV format")
args = parser.parse_args()

callsign_list = []
out_list = {}

def ekzit(msg):
    """
    Print method and exit
    """
    print msg
    print "\n Terminating ........."
    sys.exit(0)
    
if not os.access(args.filename, os.F_OK):
    ekzit("%s does not exist" % args.filename)
if not os.access(args.filename, os.R_OK):
    ekzit("%s is not a readable file" % args.filename)

if args.infile and not os.access(args.infile, os.F_OK):
    ekzit("%s does not exist" % args.infile)
if args.infile and not os.access(args.infile, os.R_OK):
    ekzit("%s is not a readable file" % args.infile)

if args.callsign and args.infile:
    print "You have passed a callsign and list of callsign. I will merge both togather and do a lookup\n"
if args.infile:
    with open(args.infile) as fh:
        callsign_list = fh.readlines()
if args.callsign:
    callsign_list.append(args.callsign)
    
callsign_list = [cs.strip() for cs in callsign_list]
    
qrz = qrz.QRZ(args.filename)
# if not qrz['_session_key']:
#     ekzit("Something is wrong with username and password")
for callsign in callsign_list:
    result = qrz.callsign(callsign)
    out_list[callsign] = 'unavailable' if result else 'available'

if args.outfile:
    if out_list:
        with open(args.outfile, 'w') as fh:
            for key  in out_list.keys():
                fh.write(key + "," + out_list[key] + "\n")
else:
    # XXX: sorting based on availability
    # XXX: OR visibley differenciate
    if out_list:
            for key  in out_list.keys():
                print key + "," + out_list[key] + "\n"
