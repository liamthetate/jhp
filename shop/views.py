from django.shortcuts import render

# Create your views here.
def shop_all(request):
    return render(request,'shop/shop.html')