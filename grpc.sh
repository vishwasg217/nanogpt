#!/bin/bash

# Run python rpc.py in the background
python rpc.py &

# Run uvicorn server2:app in the background
nohup uvicorn server2:app --host 0.0.0.0 --port 8080 > uvicorn.log &

# Prompt for user input
echo -e "Enter the start value: "
read start

echo -e "\nGenerating Text...\n"

# Make the HTTP request
curl -X 'POST' \
  'http://127.0.0.1:8080/generate-text' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "start": "'"$start"'"
}'

echo -e "\n\ntext generation done!!\n"
