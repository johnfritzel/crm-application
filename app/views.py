from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required  
from .models import ClientRecord
from django.contrib import messages


# Homepage
def home(request):

    return render(request, 'app/index.html')


# Register
def register(request):
    
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Account created successfully!")

            return redirect('my-login')
    

    context = {'form': form}

    return render(request, 'app/register.html', context=context)


# Login a user
def my_login(request):

    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)

                return redirect('dashboard')


    context = {'form': form}

    return render(request, 'app/my-login.html', context=context)


# Dashboard
@login_required(login_url='my-login')
def dashboard(request):
    
    my_records = ClientRecord.objects.all()

    context = {'records': my_records}

    return render(request, 'app/dashboard.html', context=context)


# Create a record
@login_required(login_url='my-login')
def create_record(request):
    
    form = CreateRecordForm()

    if request.method == 'POST':

        form = CreateRecordForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Success! Your record has been created.")

            return redirect('dashboard')

    context = {'form': form}

    return render(request, 'app/create-record.html', context=context)


# Update a record
@login_required(login_url='my-login')
def update_record(request, pk):

    record = ClientRecord.objects.get(id=pk)

    form = UpdateRecordForm(instance=record)

    if request.method =='POST':

        form = UpdateRecordForm(request.POST, instance=record)

        if form.is_valid():

            form.save()

            messages.success(request, "The changes to the record have been saved.")

            return redirect('dashboard')
        
    context = {'form': form}

    return render(request, 'app/update-record.html', context=context)


# View a record
@login_required(login_url='my-login')
def view_record(request, pk):

    all_records = ClientRecord.objects.get(id=pk)

    context = {'record': all_records}
    
    return render(request, 'app/view-record.html', context=context)


# Delete a record
@login_required(login_url='my-login')
def delete_record(request, pk):

    record = ClientRecord.objects.get(id=pk)

    record.delete()

    messages.success(request, "Your request to delete the record has been completed.")

    return redirect('dashboard')


# User Logout
def user_logout(request):
    
    auth.logout(request)

    messages.success(request, "See you again soon! You have been logged out.")

    return redirect('my-login')