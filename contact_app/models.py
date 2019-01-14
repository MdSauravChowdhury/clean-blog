from django.db import models

# Create your models here.
class headerContact(models.Model):
    contact = models.CharField(max_length=100)
    image = models.ImageField(upload_to='contact/header', height_field=None, width_field=None, max_length=None)
    contact_sub = models.CharField(max_length=100)

    def __str__(self):
        return self.contact

class requeredForm(models.Model):
    simple_condition = models.CharField( max_length=150)    

    def __str__(self):
        if len(self.simple_condition) > 50:
            return self.simple_condition[:50] + "..."
        return self.simple_condition
    
    
    

class getData(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=254)
    phone = models.PositiveIntegerField(default=0)
    description = models.TextField()

    def __str__(self):
        return self.name
    

# Get start about page

class about(models.Model): 
      title = models.CharField(max_length=100) 
      image = models.ImageField(upload_to='about/pic', height_field=None, width_field=None, max_length=None)
      sub_title = models.CharField(max_length=100)

      def __str__(self):
          if len(self.title) > 50:
              return self.title[:50]+ "..."
          return self.title  

class about_bio(models.Model):
    des = models.TextField()   

    def __str__(self):
        if len(self.des) > 50:
            return self.des[:50]+ "..."
        return self.des
       