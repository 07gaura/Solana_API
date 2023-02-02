from solana.system_program import TransferParams,transfer
from solders.pubkey import Pubkey
from solana.transaction import Transaction
from solana.keypair import Keypair
from solana.rpc.api import Client
from solana.publickey import PublicKey
from base58 import b58encode,b58decode
from solders.message import Message
from solders.signature import Signature
def sol_transfer(private_key,public_key,senders_address,amount):
    #public_key = b58decode(public_key)
    #senders_address = b58decode(senders_address)
    try:
        sol_amount = float(amount)
        devnet_beta_url = 'https://api.devnet.solana.com'
        solana_client = Client(devnet_beta_url)
        transfer_parameters = TransferParams(
            from_pubkey=PublicKey(public_key),
            to_pubkey=PublicKey(senders_address),
            lamports = int(sol_amount*10**9)
        )
        sol_transfer = transfer(transfer_parameters)
        transaction = Transaction().add(sol_transfer)
        encoded_keypair = private_key
        keypair = b58decode(encoded_keypair)
        p = keypair[:32]
        transaction_result = solana_client.send_transaction(transaction,Keypair.from_seed(p))
        return transaction_result
    except Exception as e:
        return "Failed"
