#from django.shortcuts import render    #this is if rendering an html template
from django.http import HttpResponse
from Magazin.models import Product
from Magazin.models import CartItem
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    products=Product.objects.all()
    product_list= ",".join([product.name for product in products])
    return HttpResponse(f"Welcome to our online shop , Magazin. Products: {product_list}")

#List of products
def product_list(request):
    products=Product.objects.all()
    response="\n".join([f"{product.name} -${product.price}" for product in products])
    return HttpResponse(f"Product list:\n{response}")

#product details
def product_detail(request,product_id):
    try:
        product=Product.objects.get(id=product_id)
        return HttpResponse(f"{product.name}:{product.description}-${product.price}")
    except Product.DoesNotExist:
        return HttpResponse("Product not found",status=404)

#add to cart
def addtocart(request,product_id):
    try:
        product=Product.objects.get(id=product_id)
        cart_item,created=CartItem.objects.get_or_create(product=product,defaults={'quantity':1})
        if not created:
            cart_item.quantity+=1
            cart_item.save()
        return HttpResponse(f"Added {product.name} to your cart.")
    except Product.DoesNotExist:
        return HttpResponse("Product not found.",status=404)
    
#view cart
def viewCart(request):
    cart_items=CartItem.objects.all()
    response="\n".join([f"{item.quantity}x{item.product.name}" for item in cart_items])
    return HttpResponse(f"Your cart:\n{response}")

#check out
@login_required
def checkout(request):
    cart_items=CartItem.objects.all()
    if not cart_items:
        return HttpResponse("Your cart is empty")
    cart_items.delete()  #simulate check out by clearing the cart
    return HttpResponse(f"Checkout successful,{request.user.username}!")



  


