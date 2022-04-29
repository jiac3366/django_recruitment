from django.shortcuts import render


# Create your views here.
def dashboard(request):
    str = "fuck"
    context = {
        "msg": str
    }
    return render(request, 'dashboard.html', context)
