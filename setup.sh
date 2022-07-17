# update os
sudo apt update -y
apt list --upgradable
sudo apt upgrade
sudo apt dist-upgrade
sudo apt autoremove

# install Poetry
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
source $HOME/.poetry/env

