#!/bin/bash

#get current directory
current_working_dir=$(pwd)

#install python and venv
apt-get install python3 python3-venv

#create and activate environment
python3 -m venv app
cd app
source ./bin/activate

#installe required python packages
pip3 install -r requirements.txt
cd ..

#stop frontend service in case its allready installed
systemctl stop a_pi_api_frontend

#create frontend .service file
sed "s|__APP_DIR__|$current_working_dir|g" <usb-wde1-reader.template.service >usb-wde1-reader.service
mv usb-wde1-reader.service /etc/systemd/system/usb-wde1-reader.service

#reload and enable
systemctl daemon-reload
systemctl enable usb-wde1-reader
systemctl start usb-wde1-reader

#finished
echo "service is logging wde1 serial data"



