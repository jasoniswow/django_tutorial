from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout

# the function for the signup page view.
def signup_view(request):
    # post means transfer data from browser to server
    # otherwise, get means transfer data from server to browser
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user) # login the user
            return redirect('articles:list') # redirect the page to somewhere
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form':form})

# login page view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect('articles:list')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', { 'form': form })

# logout view
def logout_view(request):
    if request.method == 'POST':
        logout(request) # just logout the current user
        return redirect('articles:list')
