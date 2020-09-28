#! /usr/bin/env python3

# About:
# Written by fiolet. 
# A simple tool to run nmap with cve, nikto, and dirb with common wordlist with a single command.
# All will run, even if no open ports are detected.
# Files will save to the current working directory.
# Enjoy.

# Usage:
# Run from the command line: ./simple-box-scanner <IP> <Box Name>
# I recommend adding a alias to your ~./bashrc file

import os
import subprocess
import sys

ip = sys.argv[1]
box = sys.argv[2]

nmap = "nmap_" + ip + "_" + box
nikto = "nikto_" + ip + "_" + box
dirb = "dirb_" + ip + "_" + box
wpscan = "wpscan_" + ip + "_" + box
enum = "emun4linux_" + ip + "_" + box

run_nmap = nmap -Pn -n -sV --script vuln ip | tee nmap
run_nikto = nikto -host ip | tee nikto
run_dirb = dirb http://ip | tee dirb
run_wpscan = wpscan --url ip | tee wpscan
run_enum = enum4linux ip | tee enum

os.system(run_nmap)
os.system(run_nikto)
os.system(run_dirb)
os.system(run_wpscan)
os.system(run_enum)
