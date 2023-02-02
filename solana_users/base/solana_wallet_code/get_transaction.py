from solana.rpc.api import Client
from solders.pubkey import Pubkey
from base58 import b58encode,b58decode
import json
import requests
def transaction_history(address):
        devnet_beta_url = 'https://api.devnet.solana.com'
        payload = json.dumps({
            "jsonrpc": "2.0",
            "id": 1,
            "method": "getSignaturesForAddress",
            "params": [
                "AZtEHjKH64E69nrSfYWezdJQCaHDoNFmoeEV16vzQHhY",
                {
                    "limit": 5
                }
            ]
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", devnet_beta_url, headers=headers, data=payload)

        res = json.loads(response.text)
        #print(res)
        data = []

        for i in res["result"]:
            payload = json.dumps({
                "jsonrpc": "2.0",
                "id": 1,
                "method": "getTransaction",
                "params": [
                  i["signature"],
                  "json"
                ]
              })
            headers = {
                'Content-Type': 'application/json'
            }

            response = requests.request("POST", devnet_beta_url, headers=headers, data=payload)
            tx = json.loads(response.text)
            postBalances_account1 = tx["result"]["meta"]["postBalances"][0]
            preBalances_account1 = tx["result"]["meta"]["preBalances"][0]
            postBalances_account2 = tx["result"]["meta"]["postBalances"][1]
            preBalances_account2 = tx["result"]["meta"]["preBalances"][1]
            account1 = tx["result"]["transaction"]["message"]["accountKeys"][0]
            account2 = tx["result"]["transaction"]["message"]["accountKeys"][1]
            fees = tx["result"]["meta"]["fee"]
            signature = tx["result"]["transaction"]["signatures"][0]
            transation_result = {
                "signature": signature,
                "slot": i["slot"],
                account1: (postBalances_account1 - preBalances_account1) * 10 ** -9,
                account2: (postBalances_account2 - preBalances_account2) * 10 ** -9,
                "fees": round(fees * 10 ** (-9), 9)
            }
            data.append(transation_result)
        return data
transaction_history("AZtEHjKH64E69nrSfYWezdJQCaHDoNFmoeEV16vzQHhY")




