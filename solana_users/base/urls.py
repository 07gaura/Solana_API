from django.contrib import admin
from django.urls import path
from .views import RegisterView,userView,wallet_balance,wallet, transaction_history,file_upload,create_nft, transfer_amount
urlpatterns = [
    path("register/", RegisterView.as_view()),
    path("users/<username>",userView.as_view()),
    path("users/",userView.as_view()),
    path("walletbalance/<wallet_address>",wallet_balance.as_view()),
    path("wallet/",wallet.as_view()),
    path("transaction/<wallet_address>", transaction_history.as_view()),
    path("fileupload/<filename>",file_upload.as_view()),
    path("createnft/",create_nft.as_view()),
    path("transfer/", transfer_amount.as_view())
]
