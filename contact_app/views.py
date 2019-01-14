from django.shortcuts import render,redirect 
from .models import headerContact
from .models import requeredForm
from .models import getData
from .models import about
from .models import about_bio
from .forms import contactForm
# Create your views here.
def contact_us(request):
    contact = headerContact.objects.all()
    contact_p = requeredForm.objects.all()

    form = contactForm

    if request.method == "POST":
        form = contactForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('index')

    return render(request, 'contact.html',{'contact':contact, 'form':form})

def teamAbout(request):
    about_h = about.objects.all()
    about_b = about_bio.objects.all()
    return render(request, 'about.html',{'about':about_h, 'ap':about_b})    