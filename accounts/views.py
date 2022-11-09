from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def login_view(request):
    context = {}
    if request.method == 'POST':
        query_dict = request.POST
        username = query_dict.get('username')
        password = query_dict.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            context = {'error': "Invalid username or password."}
            return render(request, 'accounts/login.html', context)
        login(request, user)
        return redirect('/')
    return render(request, 'accounts/login.html', context)


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/login')
    return render(request, 'accounts/logout.html')
