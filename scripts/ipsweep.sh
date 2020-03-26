#!/bin/bash

## SEDoug Multiple Ping Sweeper ##
#  ////////////////////////////  #
# & - allows threading (multiple lines) #
# cut -d (delimiter) -f field tr (translate) # 

if [ "$1" == "" ]
then
echo "Your forgot an IP address!"
echo "Symtax: ./ipsweep.sh 192.168.1 - use only 3 octets"

else
for ip in `seq 1 254`; do
ping -c 1 $1.$ip | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" &
done
fi