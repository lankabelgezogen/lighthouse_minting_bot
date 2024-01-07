import subprocess
import json
import threading
import logging
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class LighthouseMintingBot:
    def __init__(self, config_path: str, wallet_mnemonic: str, recipient_addresses: list):
        self.config_path = config_path
        self.wallet_mnemonic = wallet_mnemonic
        self.recipient_addresses = recipient_addresses
        self.load_config()
        self.load_wallet()
        
    def load_config(self):
        """Load the configuration from the config.json file."""
        with open(self.config_path, 'r') as file:
            self.config = json.load(file)
        logging.info("Configuration loaded.")

    def run_lighthouse_command(self, command: List[str], input_text: str = None) -> str:
        try:
            # Combine the full path to the executable with the rest of the command arguments
            full_command = ['C:\\Program Files\\nodejs\\lighthouse.cmd'] + command[1:]

            # Start the subprocess with pipes for stdin, stdout, and stderr
            process = subprocess.Popen(full_command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            # Send input_text to the process's stdin, if provided
            output, error = process.communicate(input=input_text)

            # Check if the command executed successfully
            if process.returncode != 0:
                logging.error(f"Error in running command {command}: {error}")
                return ""

            return output

        except subprocess.CalledProcessError as e:
            logging.error(f"Error in running command {command}: {e}")
            return ""


    def load_wallet(self):
        """Load a wallet into the Lighthouse CLI."""
        self.run_lighthouse_command(['C:\\Program Files\\nodejs\\lighthouse.cmd', 'load-wallet'], input_text=self.wallet_mnemonic)
        logging.info("Wallet loaded.")

    def mint_nft(self, recipient_address: str, num_nfts: int = 1):
        """Mint NFTs using a specific wallet."""
        for _ in range(num_nfts):
            # Mint command
            mint_command = ['C:\\Program Files\\nodejs\\lighthouse.cmd', 'mint', self.config['collection_address'], self.config['group_name'], '--gas-price', '0.005'] # change gas price
            output = self.run_lighthouse_command(mint_command, input_text=recipient_address)
            logging.info(f"Minting output: {output}")

    def start_minting_tasks(self):
        num_nfts_per_address = 1    # change number of NFTs to mint per address here
        for address in self.recipient_addresses:
            self.mint_nft(address, num_nfts_per_address)
        logging.info("All minting tasks completed.")

        """
        Multi-threads - not working yet
        threads = []
        for address in self.recipient_addresses:
            thread = threading.Thread(target=self.mint_nft, args=(address,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()
        logging.info("All minting tasks completed.") """


config_file_path = 'config.json'
wallet_mnemonic = '' # input wallet mnemonic here (can also load from env or whatever)

recipient_addresses = ['sei...', 'sei...'] # input wallets to receive NFTs

# Create the minting bot
bot = LighthouseMintingBot(config_file_path, wallet_mnemonic, recipient_addresses)

bot.start_minting_tasks()