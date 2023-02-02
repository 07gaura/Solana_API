
from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import UserSerializer,WalletSerializer
from rest_framework.response import Response
from .models import User,Wallet
from django.db.models import Q
from .solnft import sol_nft
from .solana_wallet_code import get_balance,get_transaction,sol_transaction
from .ar_weave import upload_image
from django.http import JsonResponse
from rest_framework.parsers import MultiPartParser
from django.core.files.storage import FileSystemStorage
from datetime import datetime
import os
# view for registering users
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class userView(APIView):
    def get(self,request,**kwargs):
        username = ""
        if "username" in kwargs.keys():
            username = kwargs["username"]
        data = User.objects.filter(Q(username__icontains=username))
        serializer = UserSerializer(data,many=True)
        return Response(serializer.data)

class wallet(APIView):
    def post(self,request):
        serializer = WalletSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class wallet_balance(APIView):
    def get(self,request,wallet_address):
        balance = get_balance.balance(wallet_address)
        return Response(balance)

class transaction_history(APIView):
    def get(self,request,wallet_address):
        history = get_transaction.transaction_history(wallet_address)
        return JsonResponse(history,safe=False)

class file_upload(APIView):
    parser_classes = [MultiPartParser]
    def post(self,request,filename):
        upload = request.data.get('image')
        print(upload)
        fss = handle_uploaded_file(upload)
        image_url = upload_image.uploade_image_ar(fss)
        res = {
            "note": "please save this link for creating nft",
            "ar_url":image_url
        }
        os.remove("./static/upload/"+fss)
        return Response(res,status=204)

class create_nft(APIView):
    def post(self,request):
        private_key = request.data.get("private_key")
        public_key = request.data.get("public_key")
        ar_image_url = request.data.get("ar_image_url")
        name = request.data.get("contract_name")
        symbol = request.data.get("contract_symbol")
        res = sol_nft.create_nft(private_key=private_key,public_key=public_key,image=ar_image_url,contract_name=name,contract_symbol=symbol)
        return Response("created",status=200)

def handle_uploaded_file(f):
    dt = datetime.now()
    ts = int(datetime.timestamp(dt))
    file = f.name
    filename = file.split(".")[0]
    file_extension = file.split(".")[1]
    temp_file_name = filename+str(ts)+"."+file_extension
    with open('./static/upload/'+temp_file_name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return temp_file_name

class transfer_amount(APIView):
    def post(self,request):
        private_key = request.data.get("private_key")
        public_key = request.data.get("public_key")
        senders_address = request.data.get("senders_address")
        amount = request.data.get("amount")

        res = sol_transaction.sol_transfer(private_key=private_key,public_key=public_key,senders_address=senders_address,amount=amount)
        return JsonResponse("success", safe=False)
