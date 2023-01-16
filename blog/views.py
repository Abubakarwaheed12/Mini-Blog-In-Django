from django.shortcuts import render , HttpResponseRedirect
from .forms import signupForm  , loginform , postform
from .models import post
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import Group

# Home View
def home(request):
    posts=post.objects.all()
    return render(request, 'index.html' , {'posts':posts})
# signup view
def signup(request):
    if request.method=='POST':
        form=signupForm(request.POST)
        if form.is_valid():
            user=form.save()
            group=Group.objects.get(name='Author')
            user.groups.add(group)
            messages.success(request, 'Congratulations! Now you are an Author.')
    else:
        form=signupForm()
    return render(request, 'signup.html' , {'form':form})


# login view
def user_login(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form=loginform(request=request , data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data['username']
                upass=form.cleaned_data['password']
                user=authenticate(username=uname , password=upass)
                if user is not None:
                    login(request , user)
                    messages.success(request, 'You Are Logged In Succefully')
                    return HttpResponseRedirect('/dashboard/')
        else:
            form=loginform()
        return render(request, 'login.html' , {'form':form})
    else:
        return HttpResponseRedirect('/dashboard/')
    
# logout view
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login')

# dashboard view
def dashboard(request):
    if request.user.is_authenticated:
        posts=post.objects.all()
        # user profile code
        user=request.user
        full_name=user.get_full_name()
        gps=user.groups.all()
        return render(request, 'dashboard.html' , {'posts':posts , 'full_name':full_name , 'groups':gps})
    else:
        return render(request, 'login.html')


 
# about View
def about(request):
    return render(request, 'about.html')

# Contact Page View 
def contact(request):
    return render(request, 'contact.html')

# ADD Post
def addpost(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form=postform(request.POST)
            if form.is_valid():
                title=form.cleaned_data['title']
                desc=form.cleaned_data['desc']
                pst=post(title=title , desc=desc)
                pst.save()
                form= postform()
                return HttpResponseRedirect('/dashboard/')
        else:
            form= postform()
            return render(request , 'addpost.html' , {'form':form})
    else:
        return render(request , 'login.html')

# Edit Post
def editpost(request , id):
    if request.user.is_authenticated:
        if request.method=='POST':
            pi=post.objects.get(pk=id)
            form=postform(request.POST, instance=pi)
            if form.is_valid():
                form.save()
            return HttpResponseRedirect('/dashboard/')
        else:
            pi=post.objects.get(pk=id)
            form=postform(instance=pi)
            return render(request , 'updatepost.html' , {'form':form})
    else:
        return render(request , 'login.html')

    
# Delete Post

def deletepost(request , id):
    if request.user.is_authenticated:
        if request.method=='POST':
            pi=post.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/dashboard/')
    else:
        return render(request , 'login.html')
