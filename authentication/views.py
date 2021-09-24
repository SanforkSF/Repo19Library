
from django.shortcuts import redirect, render
from .forms import UsersFrom
from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework import viewsets

# Create your views here.


class CustomUserViewSet(viewsets.ModelViewSet):

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


def creat_user(request):
    if request.method == 'POST':
        form = UsersFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = UsersFrom()
    context = {
        'form': form
    }
    return render(request, 'authentication/create_user.html', context)