#! /usr/bin/env python3

# About:
# Written by fiolet.
# A simple tool to run nmap with cve, nikto, dirb with
# common wordlist, wpscan, and enum4linux with a single command.
# All will run, even if no open ports are detected.
# Files will save to the current working directory.
# Enjoy.

# Usage:
# Run from the command line: ./simple-box-scanner <IP> <Box Name>
# I recommend adding a alias to your ~./bashrc file

import subprocess
import sys

ipAddr = sys.argv[1]
box = sys.argv[2]

nmap_file = "nmap_" + ipAddr + "_" + box
nikto_file = "nikto_" + ipAddr + "_" + box
dirb_file = "dirb_" + ipAddr + "_" + box
wpscan_file = "wpscan_" + ipAddr + "_" + box
enum_file = "enum4linux_" + ipAddr + "_" + box


def nmap_func():
    f_nmap = open(nmap_file, "w")
    subprocess.call(["nmap", "-Pn", "-n", "-sV", "-script=vuln", ipAddr], stdout=f_nmap)


def nikto_func():
    f_nikto = open(nikto_file, "w")
    # The -ask=auto option will send updates to the DB if any are found.
    # Change to -auto=NO if you do not want this.
    subprocess.call(["nikto", "-ask=auto", "-host", ipAddr], stdout=f_nikto)


def dirb_func():
    f_dirb = open(dirb_file, "w")
    subprocess.call(["dirb", ("http://" + ipAddr)], stdout=f_dirb)


def wpscan_func():
    f_wpscan = open(wpscan_file, "w")
    subprocess.call(["wpscan", "--url", ipAddr], stdout=f_wpscan)


def enum_func():
    f_enum = open(enum_file, "w")
    subprocess.call(["enum4linux", ("-w" + ipAddr), ipAddr], stdout=f_enum)


def main():
    print("Initializing Scans!")
    nmap_func()
    print("Scan 1 of 5 done..")
    nikto_func()
    print("Scan 2 of 5 done....")
    dirb_func()
    print("Scan 3 of 5 done......")
    wpscan_func()
    print("Scan 4 of 5 done........")
    enum_func()
    print("All Scans Have Completed!!")


main()
