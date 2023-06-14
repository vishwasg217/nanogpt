#!/bin/bash

echo -e "Preparing Data...\n"
python data/shakespeare/prepare.py --url https://gist.github.com/vishwasg217/80914e2f9f5c2e865d5d259098242e21
echo -e "Data Preparation Done!!\n"

echo -e "\nTraining Model...\n"
python train.py config/train_shakespeare_char.py --device=mps --compile=False --eval_iters=20 --log_interval=1 --block_size=64 --batch_size=12 --n_layer=4 --n_head=4 --n_embd=128 --max_iters=2000 --lr_decay_iters=2000 --dropout=0.0
echo -e "\nTraining Done!!\n"

nohup uvicorn server:app > uvicorn.log &
echo -e "\nServer Started!!\n"

echo -e "Enter the start value: "
read start

echo -e "\nGenerating Text...\n"

curl -X 'POST' \
  'http://127.0.0.1:8000/generate-text' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "start": "'"$start"'"
}'
echo -e "\n\ntext generation done!!\n"

# > uvicorn.log &

# to kill uvicorn process
# ps aux | grep uvicorn
# kill <pid>