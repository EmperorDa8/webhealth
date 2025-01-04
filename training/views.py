from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm
from .models import Module, UserProgress


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


def landing_page(request):
    return render(request, 'training/landing.html')


@login_required
def dashboard(request):
    modules = Module.objects.all()
    user_progress = UserProgress.objects.filter(user=request.user)

    context = {
        'modules': modules,
        'user_progress': user_progress
    }
    return render(request, 'training/dashboard.html', context)
