from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# THIS IS AUTHOR BIOBATA MODELS
class author(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    image_auth = models.FileField(upload_to='author/picture')
    bio_data = models.TextField()

    def __str__(self):
        return self.name.username

class logo(models.Model):
    logo_text = models.CharField(max_length=50)
    logo_img = models.ImageField(upload_to='logo/picture')

    def __str__(self):
        return self.logo_text  

class headerSection(models.Model):
    title = models.CharField(max_length=150)
    image_header = models.ImageField(upload_to='header/pic')
    subheading = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class menu(models.Model):
    home = models.URLField(max_length=200) 
    about = models.URLField(max_length=200) 
    simple_page = models.URLField(max_length=200) 
    contact = models.URLField(max_length=200) 

    def __str__(self):
        return self.home
    

#THIS IS OUR CATEGORY MODEL

class category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

# This is our main post model

class post_part_two(models.Model):
    title = models.CharField(max_length=150)
    discriptions = models.TextField()
    bquote = models.CharField(max_length=250)
    pTwo = models.TextField()

    def __str__(self):
        return self.title
    

class Post(models.Model):
    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=150)
    post_image = models.ImageField( upload_to='post/images',)
    descriptions = models.TextField()
    posted_by = models.ForeignKey(author, on_delete=models.CASCADE)
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    posted = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        if len(self.title) > 50:
            return self.title[:50] + "..."
        return self.title
    
    

