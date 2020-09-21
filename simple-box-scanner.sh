#!/bin/bash

#About:
#Written by fiolet. 
#A simple tool to run nmap with cve, nikto, and dirb with common wordlist with a single command.
#All will run, even if no open ports are detected.
#Files will save to the current working directory.
#Enjoy.

#Usage:
#Run from the command line: ./simple-box-scanner <IP> <Box Name>
#I recommend adding a alias to your ~./bashrc file

ports="80 443"
old="$IFS"
IFS='_'
box="$*"
IFS=$old

var1="nmap_"
var2="nikto_"
var3="dirb_"
nmap="$var1$box"
nikto="$var2$box"
dirb="$var3$box"

nmap -Pn -n -sV --script vuln $1 | tee $nmap
nikto -host $1 | tee $nikto
dirb http://$1 | tee $dirb
