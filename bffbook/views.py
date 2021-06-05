from django.http import HttpResponse
from django.shortcuts import render
from profiles.models import Profile

def home_view(request):
    if request.user.is_authenticated:
        user = request.user
        profile = Profile.objects.get(user=request.user)
        hello = 'Hello World'
        context = {
            'user' : user,
            'hello': hello,
            'picture': profile,
        }
        return render(request,'main/home.html',context)
    else:
        return render(request,'main/home.html')
    #return HttpResponse("Hello world")