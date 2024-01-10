
# Sei Lighthouse NFT Minting Bot

## Introduction
This NFT minting bot is designed to automate the process of minting NFTs on the Sei blockchain using the Lighthouse CLI.
Currently doesn't support mass-task or multi-wallet (to be added).

Old version - lighthouse gets 1.5sei for every mint!

For functional multi-wallet bot, hit me up on Discord: lankabelgezogen
## Features
- Automated minting of NFTs on the Sei blockchain.
- Customizable settings through `config.json`.
- Support for the main-net and test-net.

## Requirements
- Python 3.6 or higher.
- Lighthouse CLI installed and configured.
- Sei blockchain account with sufficient funds.

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/lankabelgezogen/lighthouse_minting_bot
   ```
2. Navigate to the bot directory:
   ```
   cd lighthouse_minting_bot
   ```

## Configuration
LINE 27 => Change the path to your local lighthouse installation. (Can be found with $where lighthouse)

LINE 61 => Change the amount of nfts to mint per address 

LINE 80 => add your wallet mnemonic phrase

LINE 82 => add your recipient addresses

Edit the `config.json` file to set up the bot:
```json
{
    "collection_address": "[Collection Address]",
    "group_name": "public",
    "network": "[network]",
    "rpc": "[rpc]",
    "mnemonic": ""
}
```
- `collection_address`: The address of the NFT collection.
- `network`: The blockchain network to use.
- `rpc`: The RPC URL for connecting to the Sei blockchain.
- `mnemonic`: Your wallet's mnemonic for transactions. (Will also be automatically set when you run the bot for the first time)

## Usage
To run the bot, execute:
```
python bot.py
```
Ensure the configuration is set correctly in `config.json` before running the bot.
Logging is enabled by default.

## Contributing
Contributions to the project are welcome. Please fork the repo, create a branch, commit + push and open a pull request.
