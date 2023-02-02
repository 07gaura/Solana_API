import arweave
import os
def uploade_image_ar(filename):
    print(os.getcwd())
    image= "./static/upload/"+filename
    your_ar_wallet = arweave.Wallet("./base/ar_weave/arweave-key-lUYWd7W4EIKioXkr2cGz9f78uwavDbutPFAn6c9RfAw.json")

    #  2. Upload image to Arweave
    with open(image, 'rb') as f:
        img_in_bytes = f.read()

    transaction = arweave.Transaction(your_ar_wallet, data=img_in_bytes)
    transaction.add_tag('Content-Type', 'image/png')
    transaction.sign()
    transaction.send()
    API_URL = "https://arweave.net"
    image_url = API_URL + "/" + transaction.id
    return image_url