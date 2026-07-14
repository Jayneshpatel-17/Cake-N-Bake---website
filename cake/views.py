from django.shortcuts import render ,redirect , get_object_or_404
from .models import userModel , product , category , shape , flavor , cart , review , order , blog , inquiry 
from .forms import userForm
from django.db.models import Q
from django.http import JsonResponse
from django.conf import settings
from datetime import datetime, timedelta
from django.utils import timezone
from django.db.models import Sum, Count
# Create your views here.

def registration(request): 
    if request.method == 'POST':
        form = userForm(request.POST)
        if form.is_valid():
           username = form.cleaned_data['username']
           email = form.cleaned_data['email']
           contact = form.cleaned_data['contact']
           dob = form.cleaned_data['dob']
           password = form.cleaned_data['password']
           cpassword = form.cleaned_data['cpassword']
           gender = form.cleaned_data['gender']
           address = form.cleaned_data['address']

           data = userModel(username=username,email=email,contact=contact,dob=dob,password=password,cpassword=cpassword,gender=gender,address=address)
           data.save()
    else:
        form = userForm()
    return render(request,'registration.html',{'form':form})


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username1 = request.POST.get('username1')
        password1 = request.POST.get('password1')
        customer = userModel.objects.filter(username=request.POST["username1"])
        passw = userModel.objects.filter(password=request.POST["password1"])
        error_message = None
        if customer and passw:
            request.session['username1']=username1
            request.session['password1']=password1
            return redirect('home')
        else:
            error_message = "Invalid username and password!!"
        return render(request , 'login.html' ,{'error_message':error_message})
    
def logout(request):
    if request.session.has_key('username1') and request.session.has_key('password1'):
        del request.session["username1"]
        del request.session["password1"]
        return redirect('guest')
    else:
        return redirect('login')

def guest(request):
    products = product.get_all_products()
    reviews = review.get_all_review()
    blogs = blog.get_all_blog()
    return render(request, 'guest.html' ,{'product':products , 'review':reviews , 'blog':blogs})

def home(request):
    products = None
    if request.session.has_key('username1') and request.session.has_key('password1'):
        username1 = request.session["username1"]
        password1 = request.session["password1"]
        categories = category.get_all_categories()
        customer = userModel.objects.filter(username=username1)
        reviews = review.get_all_review()
        blogs = blog.get_all_blog()
        for c in customer:
            username = c.username

            categoryID = request.GET.get('category')
            if categoryID:
                products = product.get_all_product_by_category_id(categoryID)
            else:
                products = product.get_all_products()

            data = {}
            data['username']=username
            data['product'] = products
            data['category'] = categories
            data['review']=reviews
            data['blog']=blogs
            return render(request, 'home.html' , data)
    else:
        return redirect('login')

def about(request):
    return render(request, 'about.html')

def search(request):
    query = request.GET.get('query')
    search = product.objects.filter(name__contains=query)
    # if request.session.has_key('username1') and request.session.has_key('password1'):
    #     username1 = request.session["username1"]
    #     password1 = request.session["password1"]
    categories = category.get_all_categories()
        # customer = userModel.objects.filter(username=username1)
    reviews = review.get_all_review()
    blogs = blog.get_all_blog()
        # for c in customer:
        #     username = c.username
    data={
            # 'username':username,
            'search':search,
            'category':categories,
            'review':reviews,
            'blog':blogs,
            'query':query
    }
    return render(request, 'search.html' , data)

def productdetail(request,pk):
    products = product.objects.get(pk=pk)
    item_already_in_cart = False
    if request.session.has_key('username1'):
        username1 = request.session["username1"]
        item_already_in_cart = cart.objects.filter(Q(product=products.id) & Q(username=username1)).exists()
    shapes = shape.get_all_shape()
    flavors = flavor.get_all_flavor()

    data = {
            'products':products ,
            'shapes':shapes ,
            'flavors':flavors,
            'item_already_in_cart':item_already_in_cart
        }
    return render(request, 'productdetail.html',data)

def add_to_cart(request):
    if request.session.has_key('username1'):
        username1 = request.session['username1']
        weight = request.POST.get('kgs')
        shapes = request.POST.get('item')
        flavors = request.POST.get('item1')
        product_id = request.POST.get('prod_id')
        price = request.POST.get('updated-price')
        # price = int(pri)
        total = price
        product_name = product.objects.get(id=product_id)
        products = product.objects.filter(id=product_id)
        for p in products:
            image = p.image
            price = p.price
            pr = int(weight)/1000
            pri = pr * price * 2
            total = pri
            cart(username=username1,product=product_name,image=image,weight=weight,price=pri,shape=shapes,flavor=flavors,total=total).save()
            return redirect(f"/cake/productdetail/{product_id}")
    else:
        return redirect('login')
    
def show_cart(request):
        if request.session.has_key('username1'):
            username1 = request.session["username1"]
            carts = cart.objects.filter(username=username1)
            # cart_items = cart.objects.all()
            total = sum(item.total_price() for item in carts)
            data = {
                'username':username1,
                'cart':carts,
                # 'cart_items': cart_items, 
                'total': total
                # 'total-price':cart.total_price()
            }
            if carts:
                return render(request , 'show_cart.html',data)
            else:
                return render(request, 'empty_cart.html')
        else:
            return redirect('login')

def update_cart(request):
    if request.session.has_key('username1'):
        username1 = request.session["username1"]
        if request.method == "POST":
            cart_id = request.POST.get("cart_id")
            action = request.POST.get("action")
            cart_item = get_object_or_404(cart, id=cart_id)
        
            if action == "plus":
                cart_item.quantity += 1
            elif action == "minus" and cart_item.quantity > 1:
                cart_item.quantity -= 1
            cart_item.save()
        
            total = sum(item.total_price() for item in cart.objects.filter(username=username1))
            cart_item.total = total
            cart_item.save()
            return JsonResponse({"quantity": cart_item.quantity,"username":username1, "total": cart_item.total})
    
def remove_cart_item(request):
    if request.session.has_key('username1'):
        username1 = request.session["username1"]
        if request.method == "POST":
            cart_id = request.POST.get("cart_id")
            cart_item = get_object_or_404(cart, id=cart_id)
            cart_item.delete()
        
            total = sum(item.total_price() for item in cart.objects.filter(username=username1))
            # cart_item.total = total
            # cart_item.save()
            return JsonResponse({"total": total,"username":username1})

def feedback(request):
    username1 = request.session['username1']       
    if request.method == 'POST':
        feedback = request.POST.get('comment')
        review(username=username1,feedback=feedback).save()
    return redirect('home')

def checkout(request):
    return render(request, 'checkout.html')

def orderdetails(request):
    if request.session.has_key('username1'):
        username1 = request.session["username1"]
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        address = request.POST.get('address')
        cart_product = cart.objects.filter(username=username1)
        total = sum(item.total_price() for item in cart_product)
        for c in cart_product:
            product_name = c.product
            quantity = c.quantity
            weight = c.weight
            shape = c.shape
            flavor = c.flavor
            image = c.image
            price = c.price
            total = total

            order(total=total,username=username1,delivery_name=name,contact=contact,address=address,product=product_name,quantity=quantity,weight=weight,shape=shape,flavor=flavor,image=image,price=price).save()
        cart_product.delete()

        return redirect('success')
    else:
        return redirect('login')
    
def receipe(request):
    if request.session.has_key('username1'):
        username1 = request.session["username1"]
        orders = order.objects.filter(username=username1)
        if orders:
            return render(request , 'receipe1.html',{'order':orders})
        else:
            return render(request, 'cancel.html')

def success(request):
    return render(request , 'success.html')

def cancel(request):
    return render(request , 'cancel.html')

def inquirys(request):
    if request.session.has_key('username1'):
        username1 = request.session["username1"]
        if request.method == 'POST':
            # username1 = request.session["username1"]
            issue = request.POST.get('issue')
            inquiry(username=username1,issue=issue).save()
        inquirys = inquiry.objects.filter(username=username1)
        # inq = inquiry.objects.order_by('username')
        if inquirys.count() > 1:
            inquirys[0].delete()
        for i in inquirys:
            ans = i.ans
            return render(request , 'inquirys.html',{'inquiry':inquirys , 'ans':ans})
        
    return render(request , 'inquirys.html')

def deletes(request):
    if request.session.has_key('username1'):
        username1 = request.session["username1"]
        ordid = request.POST.get('delete')
        orde = order.objects.get(id=ordid)
        orders = order.objects.filter(id=ordid)
        for o in orders:
            o.delete()
        return redirect('receipe')
    # return redirect('login')

