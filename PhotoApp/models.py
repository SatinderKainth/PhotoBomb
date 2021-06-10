from django.db import models
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class UserManager(models.Manager):
    def validate(self, form):
        errors = {}
        if len(form['f_name']) < 2:
            errors['f_name'] = 'First Name is less than 2 characters'

        if len(form['l_name']) < 2:
            errors['l_name'] = 'Last Name is less than 2 characters'

        if not EMAIL_REGEX.match(form['email']):
            errors['email'] = 'Invalid Email Address'
        
        email_check = self.filter(email=form['email'])
        if email_check:
            errors['email'] = "Email is already in use"

        if len(form['pwd']) < 8:
            errors['pwd'] = 'Password is less than 8 characters'
        
        if form['pwd'] != form['confirm']:
            errors['pwd'] = 'Passwords do not match'
        
        return errors
    
    def authenticate(self, email, pwd):
        users = self.filter(email=email)
        if not users:
            return False

        user = users[0]
        return bcrypt.checkpw(pwd.encode(), user.pwd.encode())

    def register(self, form):
        password = bcrypt.hashpw(form['pwd'].encode(), bcrypt.gensalt()).decode()
        return self.create(
            f_name = form['f_name'],
            l_name = form['l_name'],
            email = form['email'],
            pwd = password,
        )
        
class User(models.Model):
    f_name = models.CharField(max_length=45)
    l_name = models.CharField(max_length=45)
    email = models.EmailField(unique=True)
    pwd = models.CharField(max_length=255)
    created_at= models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    objects = UserManager()
    
class Upload(models.Model):
    file = models.FileField(upload_to="user_images")
    #user = models.OneToOneField("User",on_delete=models.CASCADE,default="None")
    user = models.ManyToManyField(User,related_name="uploads")
    #video = models.FileField(upload_to="user_video",verbose_name="")
    created_at= models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
class Album(models.Model):
    name = models.CharField(max_length=100)
    info = models.TextField(max_length=200)
    users = models.ForeignKey(User,related_name="albums",on_delete=models.CASCADE) 
    created_at= models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def search(self,name,info,find):
        to_find =Upload.file.filter(Album.name('%'+find+'%'),Album.info('%'+find+'%'))
        for image in to_find:
            User.uploads.append(User)
        return image