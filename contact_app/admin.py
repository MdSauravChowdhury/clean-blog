from django.contrib import admin

from .models import headerContact
from .models import requeredForm
from .models import getData
from .models import about
from .models import about_bio

# Register your models here.
admin.site.register(headerContact)
admin.site.register(requeredForm)
admin.site.register(getData)
admin.site.register(about)
admin.site.register(about_bio)