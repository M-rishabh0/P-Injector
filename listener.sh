#!/bin/bash

# Ask for IP and Port for Listener
read -p "Enter your IP address for listener: " IP
read -p "Enter port for listener: " PORT

# Start the listener
echo "Starting listener on $IP:$PORT..."
python listener.py $IP $PORT
