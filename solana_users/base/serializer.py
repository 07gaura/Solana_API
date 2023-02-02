
from rest_framework import serializers
from .models import User,Wallet

class WalletSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wallet
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    wallets = WalletSerializer(read_only=True,many=True)
    class Meta:
        model = User
        fields = ["id", "email", "username", "password","first_name","last_name","wallets"]

