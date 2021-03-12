#!/bin/sh
set -x
sudo apt-get clean
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y autoremove
pihole -up

# Add to crontab
# 33 3 * * * sudo /bin/bash /home/<username>/Scripts/update-pihole.sh > /home/<username>/Logs/update-pihole.log
