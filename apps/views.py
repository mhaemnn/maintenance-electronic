
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm
from django.contrib import messages

# Login / Register / logout


def home(request):
    return render(request, 'vendor/home.html')


def registerPage(request):
    print("Entering registerPage...")
    form = CreateUserForm()
    if request.method == 'POST':
        print("Processing POST request...")
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
        else:
            for error in form.errors.values():
                messages.error(request, error)

        # Pesan ini harus muncul jika eksekusi mencapai titik ini
        print("Redirecting to login page...")
        return redirect('login')

    context = {'form': form}
    return render(request, 'vendor/register.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("Redirecting to home...")
            return redirect('home')

    context = {}
    return render(request, 'vendor/login.html', context)


def logoutPage(request):
    logout(request)
    return redirect('login')
