from solana.rpc.api import Client
from solders.pubkey import Pubkey
from base58 import b58encode,b58decode

def balance(address):
    try:
        wallet_address = b58decode(address)
        w = Pubkey(wallet_address)

        devnet_beta_url = 'https://api.devnet.solana.com'
        solana_client = Client(devnet_beta_url)
        balance = solana_client.get_balance(pubkey=w)
        balance_result = balance.get("result")
        value = balance_result.get("value")
        ui_balance = round(value * 10 ** (-9), 9)
        return ui_balance
    except ValueError:
        return "wrong wallet address or something went wrong"

