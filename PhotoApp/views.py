from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')

def sign_in(request):
    return render(request,'sign_in.html')

def login(request):
    if request.method == "GET":
        return redirect('/login')
    if not User.objects.authenticate(request.POST['email'], request.POST['pwd']):
        messages.error(request, 'Please fill out the Email and Password fields')
        return redirect('/sign_in')
    user = User.objects.get(email=request.POST['email'])
    request.session['user_id'] = user.id
    #messages.success(request, "You have successfully logged in!")
    return redirect('/welcome')

def logout(request):
    request.session.flush()
    return redirect("/")

def welcome(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    images = Upload.objects.all()
    context = {
        'user': user,
        'images':images
    }
    return render(request, 'login.html',context)

def register(request):
    return render(request,'register.html')

def new(request):
    if request.method == "GET":
        return redirect('/new')
    errors = User.objects.validate(request.POST)
    if errors:
        for error in errors.values():
            messages.error(request, error)
        return redirect('/register')
    else:
        new_user = User.objects.register(request.POST)
        request.session['user_id'] = new_user.id
        messages.success(request, "You have successfully registered!")
        return redirect('/home')
    ''' if request.method =="GET":
        new_user = User.objects.create(
        f_name = request.POST['f_name'],l_name=request.POST['l_name'],
        email=request.POST['email'],
        pwd=request.POST['pwd'])
        context ={
            "new_user": new_user
        }
        return render(request,'home.html',context)
    return redirect('/home') '''

def success(request):
    if 'user_id' not in request.session:
        return redirect('/register')
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user': user
    }
    return render(request, 'home.html',context)

def logout(request):
    return render(request,'index.html')

def edit_profile(request,user_id):
    if request.method=="POST":
        update = User.objects.get(id=request.session['user_id'])
        update.f_name = request.POST['f_name']
        update.l_name = request.POST['l_name']
        update.email = request.POST['email']
        update.save()
        return redirect(f"/edit/{user_id}/update")
    edit = User.objects.get(id=request.session['user_id'])
    context = {
        "user": edit
    }
    return render(request,'update.html',context)

''' def update(request, user_id):
    update = User.objects.get(id=request.session['user_id'])
    update.f_name = request.POST['f_name']
    update.l_name = request.POST['l_name']
    update.email = request.POST['email']
    update.save()
    return redirect('/edit') '''

def add_image(request):
    if request.method == "POST":
        new_file =Upload(file = request.FILES['image'])
        #print("@@@@",new_file)
        new_file.save()
    return redirect("/welcome")
    

def search(request,user_id):
    if 'user_id' not in request.session:
        return redirect('/login')
    search = Upload.file(id=request.session['user_id'])
    context ={
        "search":search
    }
    return render(request,'login.html',context)

def album(request):
    if 'user_id' not in request.session:
        return redirect('/login')
    new_album = Album.new(request.session['user_id'],request.POST['name'],request.POST['info'])
    context={
        'new_album':new_album
    }
    return render(request,'login.html',context)