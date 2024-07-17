from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Post

# Create your views here.
def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']
        
        if password == password_confirmation:
            if User.objects.filter(email = email).exists():
                messages.info(request, 'Email already exists')
                return redirect('register')
            elif User.objects.filter(username = username).exists():
                messages.info(request, 'Username already exists')
                return redirect('register')
            
            user = User.objects.create_user(username, email, password)
            user.save()
            messages.success(request, 'Registration successful. You can login now.')
            return redirect('login')
        
        messages.info(request, 'The passwords you entered does not match')
        return redirect('register')
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username = username, password = password)
        
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Login successful')
            return redirect('/')
        else:
            messages.info(request, 'Username or password is incorrect')
            return redirect('login')
        
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('login')


def blog(request):
    posts = Post.objects.all()

    return render(request, 'blog.html', {'posts': posts})

def post(request, pk):
    post = Post.objects.get(id = pk)
    count = len(post.body.split())

    return render(request, 'blog-single.html', {'post': post, 'count':count})

def sentence(request):
    return render(request, 'sentence.html')

def counter(request):
    text = request.POST['sentence']
    word_count = len(text.split())
    return render(request, 'counter.html', {'count': word_count})
