#!/bin/bash

# read -p "Enter the start value: " start_value
nohup uvicorn server:app > uvicorn.log &
echo "\nServer Started!!\n"
curl -X POST -H "Content-Type: application/json" -d '{"start": "The"}' http://localhost:8000/generate-text
