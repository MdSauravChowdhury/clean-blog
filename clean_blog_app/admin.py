from django.contrib import admin
from .models import author
from .models import category
from .models import Post
from .models import logo
from .models import headerSection
from .models import menu

# Register your models here.
admin.site.register(author)
admin.site.register(category)
admin.site.register(Post)
admin.site.register(logo)
admin.site.register(headerSection)
admin.site.register(menu)
