#!/usr/bin/env bash

# Install Editor Packages
sudo apt install vim
sudo apt install curl
sudo apt install tree

# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
rm get-docker.sh
docker --version

# Install Visual Studio Code
sudo apt update
sudo apt install software-properties-common apt-transport-https wget

wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -

sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"

sudo apt install code   # Run code to start up vsc

# Install Python 3.7

sudo apt update
sudo apt install software-properties-common

sudo add-apt-repository ppa:deadsnakes/ppa

#Press [ENTER] to continue or Ctrl-c to cancel adding it.

sudo apt install python3.7

python3.7 --version
