from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy,reverse
from FoodApp.models import Product,Cart,OrderTable
from django.contrib.auth.models import User
from FoodApp.forms import SignupForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# Create your views here.
class product_list(ListView):
    model=Product

class product_detail(DetailView):
    model=Product

class product_update(UpdateView):
    model=Product

def index(request):
    return render(request,'FoodApp/index.html')

def signup(request):
    if request.method == 'GET':
        form = SignupForm()
        return render(request, 'FoodApp/signup.html', {'form': form})
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            form=SignupForm()
            mydict={'msg':'Registration successfull....','form':form}
        return HttpResponseRedirect(reverse('list'))
    return render(request,'FoodApp/signup.html',context=mydict)

def addcart(request):
    user=request.user
    ip= request.META['REMOTE_ADDR']
    if request.user.is_anonymous:
        user=ip
    pid=request.POST.get('pid')
    name=request.POST.get('name')
    quan=request.POST.get('quantity')
    price=request.POST.get('price')
    image=request.POST.get('image')
    Total=float(quan)*float(price)
    Cart.objects.get_or_create(pid=pid,name=name,quantity=quan,price=price,total=Total,pic=image,user=user)
    count=Cart.objects.filter(user=user).count()
    product_list=Product.objects.all()
    msg="Items Added Successfully"
    mydict={"count":count,"product_list":product_list,'msg':msg}
    return render(request,'FoodApp/product_list.html',context=mydict)

def viewcart(request):
    cart=Cart.objects.all()
    user=request.user
    ip=request.META['REMOTE_ADDR']
    if request.user.is_anonymous:
        user=ip
    cart=Cart.objects.filter(user=user)
    return render(request,'FoodApp/cart.html',{'cart':cart})

def updatecart(request):
    up_pid=request.POST.get('pid')
    up_quantity=request.POST.get('quantity')
    up_price=request.POST.get('price')
    up_total=float(up_quantity)*float(up_price)
    Cart.objects.filter(pid=up_pid).update(quantity=up_quantity,price=up_price,total=up_total)
    cart=Cart.objects.all()
    user=request.user
    ip=request.META['REMOTE_ADDR']
    if request.user.is_anonymous:
        user=ip
    cart=Cart.objects.filter(user=user)
    return render(request,'FoodApp/cart.html',{'cart':cart})

def delcart(request,a):
    c=Cart.objects.get(id=a)
    cart=Cart.objects.all()
    if c:
        c.delete()
        return redirect('cart')
    return render(request,'FoodApp/cart.html',{'del':'Item Removed Successfully...','add':'Check other items','cart':cart})

def delhis(request,a):
    c=OrderTable.objects.get(id=a)
    order=OrderTable.objects.all()
    if c:
        c.delete()
        return redirect('orders')

    return render(request,'FoodApp/orders.html',{'del':'Item Removed Successfully...','add':'Check other items','order':order})

@login_required
def orderhis(request):
    order=OrderTable.objects.all()
    user=request.user
    order=OrderTable.objects.filter(user=user)
    return render(request,'FoodApp/orders.html',{'order':order})

@login_required
def ordertab(request):
    c=Cart.objects.all()
    user=request.user
    for cart in c:
        user=cart.user
        id=cart.pid
        name=cart.name
        quan=cart.quantity
        price=cart.price
        Total=cart.total
        image=cart.pic
        status='0'
        OrderTable.objects.get_or_create(status=status,pid=id,name=name,quantity=quan,price=price,total=Total,user=user,pic=image)
    order=OrderTable.objects.all()
    order.filter(user=request.user)
    mydict={'order':order}
    c.delete()
        #subject = 'Order confirmed'
        #message = 'Thank you for ordering from our site,happy shopping'
        #email_from = settings.EMAIL_HOST_USER
        #recipient_list =['dlovesu93@gmail.com',]
        #fail_silently=False
        #send_mail( subject, message, email_from, recipient_list )
    return render(request,'FoodApp/orders.html',context=mydict)

def test(request):
    subject = 'Order confirmed'
    client_ip = request.META['REMOTE_ADDR']
    print(client_ip)
    message = 'Thank you for ordering from our site,happy shopping'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ['93deepak.chauhan@gmail.com',]
    #fail_silently=False
    send_mail( subject, message, from_email, recipient_list )
    return render(request,'FoodApp/product_list.html')


def CheckUser(request):
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    u=request.GET.get('user')
    print("Username>>>>>>>>",u)
    data = {
        'is_taken': User.objects.filter(username__iexact=u).exists()
        }
    print(data)
    return JsonResponse(data)
