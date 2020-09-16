#!/bin/bash

#About:
#Written by fiolet. 
#A simple tool to run nmap with cve and nikto with a single command.
#Both will run, even if no open ports are detected.
#Files will save to the current working directory.
#Enjoy.

#Usage:
#Run from the command line: ./simple-box-scanner <IP> <Box Name>
#I recommend adding an alias to your ~./bashrc file

ports="80 443"
old="$IFS"
IFS='_'
box="$*"
IFS=$old

var1="nmap_"
var2="nikto_"
nmap="$var1$box"
nikto="$var2$box"

nmap -Pn -n -sV --script vuln $1 | tee $nmap
nikto -host $1 | tee $nikto
