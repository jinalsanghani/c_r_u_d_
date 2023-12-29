from django.shortcuts import render, redirect
from .models import User
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

def user_create(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        city = request.POST.get('city')
        birthdate = request.POST.get('birthdate')

        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            city=city,
            birthdate=birthdate
        )
        return redirect('user_list')  # Redirect to a user list page
    return render(request, 'user_form.html')  # Render the form template

def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

def update_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    
    if request.method == 'POST':
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        birthdate = request.POST['birthdate']
        city = request.POST['city']
        

        user.email = email
        user.first_name = first_name
        user.last_name = last_name
        user.birthdate = birthdate
        user.city = city
        user.save()
        
        return redirect('user_list')
    
    return render(request, 'update_user.html', {'user': user})

def delete_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')  
    
    return render(request, 'delete_user.html', {'user': user})

