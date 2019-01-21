from django.shortcuts import render


# Create your views here.
def signup(request):
    if request.method == 'POST':
        print ()
    else:
        return render(request, 'accounts/signup.html')
