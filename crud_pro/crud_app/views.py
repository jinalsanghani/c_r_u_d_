from django.shortcuts import render, redirect, get_object_or_404
from .models import UserDetails
from .forms import UserDetailsForm

def user_list(request):
    users = UserDetails.objects.all()
    return render(request, 'user_list.html', {'users': users})

def user_create(request):
    if request.method == 'POST':
        form = UserDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserDetailsForm()
    return render(request, 'user_form.html', {'form': form})

def update_user(request, user_id):
    user = get_object_or_404(UserDetails, pk=user_id)
    if request.method == 'POST':
        form = UserDetailsForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')  
    else:
        form = UserDetailsForm(instance=user)
    return render(request, 'update_user.html', {'form': form})

def delete_user(request, user_id):
    user = get_object_or_404(UserDetails, pk=user_id)
    
    # Check if the request method is POST (usually from a form submission)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')

    return render(request, 'confirm_delete.html', {'user': user})