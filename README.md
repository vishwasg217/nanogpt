# NanoGPT Implementation

NanoGPT is a lightweight implementation of the GPT (Generative Pre-trained Transformer) model based on the Karpathy's "minGPT" repository. This README provides instructions on how to clone and use the NanoGPT repository for text generation tasks.

## Prerequisites

Before using NanoGPT, ensure that you have the following dependencies installed:

- [PyTorch](https://pytorch.org) 
- [NumPy](https://numpy.org/install/) 
- Transformers library from Hugging Face: `pip install transformers`
- Tiktoken library from OpenAI: `pip install tiktoken`
- Wandb library for optional logging: `pip install wandb`
- tqdm library: `pip install tqdm`
- Uvicorn and FastAPI: `pip install uvicorn fastapi fire`

## Clone the Repository

To get started, clone the NanoGPT repository from GitHub:

```
git clone https://github.com/vishwasg217/nanogpt.git
```

## Prepare Data

The repository provides a script to prepare data for training. You can use it by providing a Gist file URL:

```
python data/shakespeare/prepare.py --url <url>
```

Replace `<url>` with the Gist file URL containing your training data.

## Training the Model

To train the NanoGPT model, use the following command:

```
python train.py config/train_shakespeare_char.py --device=mps --compile=False --eval_iters=20 --log_interval=1 --block_size=64 --batch_size=12 --n_layer=4 --n_head=4 --n_embd=128 --max_iters=2000 --lr_decay_iters=2000 --dropout=0.0
```

Adjust the command-line arguments based on your requirements. This command will train the model using the specified configuration.

## Generating Text

To generate text using the trained NanoGPT model, use the following command:

```
python test.py --start <start_text>
```

Replace `<start_text>` with the desired starting text for text generation.

## Using the Script

To perform all the steps mentioned above in a single command, you can execute the shell script provided in the repository:

```
chmod +x script.sh
./script.sh
```

## Running the API

To run the UVicorn server and use the API for text generation, follow these steps:

1. Start the server:
```
uvicorn app.main:app --reload
```

2. Open a new terminal and use the `curl` command to get a text generation response:
```
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
```

Follow the prompt and enter the desired starting text when prompted. The generated text will be displayed in the terminal.

You have now successfully set up and used NanoGPT for text generation!

Note: Please refer to the original repository or documentation for any further details or updates on NanoGPT.