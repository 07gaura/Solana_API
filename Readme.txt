What is solana? 
Solana is layer 1 blockchain technology which is designed to host decentralized, scalable application, it is an opensource project. Solana allows faster transaction and lower transaction fees. 


Project description
Using api user can see the transaction history of itself and other users, can transfer amount, user can create NFT’s in single click. With the help of API’s user can perform this activities easily and can integrate this API’s in their applications.


Technologies used:
Django, Solana SDK, Ar_weave,Python


API endpoints:
1. http://127.0.0.1:8000/walletbalance/<walletaddress> (GET)
2. http://127.0.0.1:8000/createnft/ (POST)
Content-type: application/json
{
   "public_key":"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
"private_key":"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
   "ar_image_url": "https://arweave.net/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
   "contract_name": "xxxxx",
   "contract_symbol": "xx"
}
3. http://127.0.0.1/fileupload/<filename> (POST)
        Content-Type: multipart/form-data
        {
                “Image”: select file
}
4. http://127.0.0.1:8000/transaction/<wallet_address> (GET)
5. http://127.0.0.1:8000/transfer/ (POST)
        Content-type: application/json
        {
   "public_key": "xxxxxxxxxxx",
   "private_key": "xxxxxxxxxx",
   "senders_address": "xxxxxxxxxxxxxxxx",
   "amount": "0.01"
}
