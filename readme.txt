1. git clone https://github.com/vishwasg217/nanogpt.git

2. 
install Dependencies:

- [pytorch](https://pytorch.org) <3
- [numpy](https://numpy.org/install/) <3
- `pip install transformers` for huggingface transformers <3 (to load GPT-2 checkpoints)
- `pip install tiktoken` for OpenAI's fast BPE code <3
- `pip install wandb` for optional logging <3
- `pip install tqdm` <3
- pip install uvicorn fastapi fire


3. prepare data from a gist file url
python data/shakespeare/prepare.py --url <url>

4. training the model:
python train.py config/train_shakespeare_char.py --device=mps --compile=False --eval_iters=20 --log_interval=1 --block_size=64 --batch_size=12 --n_layer=4 --n_head=4 --n_embd=128 --max_iters=2000 --lr_decay_iters=2000 --dropout=0.0

5. generating text by giving statrt value
python test.py --start <"start text">

6. to perform the entire operation in a single command execute the shell script file script.sh:
chmod +x script.sh
./script.sh


7. run the uvicorn server to get the api up and running and use curl command to get the response

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


