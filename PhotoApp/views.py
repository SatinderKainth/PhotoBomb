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
        return redirect('/sign_in')
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

def add_image(request,id):
    if request.method == "POST":
        new_file =Upload(file=request.FILES['image'])
        new_file.save()
    return redirect("/welcome")


def gallery(request):
    
    album = request.GET.get('album')
    if album =="":
        uploads = Upload.objects.all()
    else:
        uploads = Upload.objects.filter(album__name==album)
    user_album = Album.objects.filter(user=user)
    context ={
            "to_album":user_album,
            "uploads":uploads
    }
    return render(request,'gallery.html')

def viewPhoto(request,id):
    upload = Upload.objects.get(id=id)
    context={
        "upload":upload
    }
    return render(request,'photo.html',context)

def delete_photo(request,id):
    to_delete = Upload.objects.get(id=id)
    to_delete.delete()     
    return redirect("/welcome")
    
def addPhoto(request):
    if request.method=="POST":
        file = request.POST.get('file')
        info = request.POST['info']
        add= Upload.objects.create(file=file,info=info)
        
    return render(request,'add.html')

def delete_profile(request,user_id):
    if not'user_id' in request.session:
        return redirect("/")
    delete = User.objects.get(id=request.session['user_id'])
    delete.delete()
    return redirect("/")