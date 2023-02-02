import base58
import json
import os
from base58 import b58encode,b58decode
from .api.metaplex_api import MetaplexAPI
from cryptography.fernet import Fernet
import arweave


def create_nft(image,private_key,public_key,contract_name,contract_symbol):
    SERVER_DESCRIPTION_KEY = Fernet.generate_key().decode("ascii")
    TEST_PRIVATE_KEY = private_key
    TEST_PUBLIC_KEY = public_key

    cfg = {
        "PRIVATE_KEY": TEST_PRIVATE_KEY,
        "PUBLIC_KEY": TEST_PUBLIC_KEY,
        "DECRYPTION_KEY": SERVER_DESCRIPTION_KEY
    }
    api_endpoint = "https://api.devnet.solana.com"
    obj = MetaplexAPI(cfg)
    n = obj.deploy(api_endpoint=api_endpoint,name="A"*32,symbol=contract_symbol*5,fees=0)
    contract_key = json.loads(n).get('contract')
    image_json_file = image
    result = obj.mint(api_endpoint=api_endpoint,contract_key=contract_key,dest_key=TEST_PUBLIC_KEY,link=image_json_file)
    print(result)