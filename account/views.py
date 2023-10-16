from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from account.models import CustomUser



# class CustomLoginView(LoginView):
#     def get_success_url(self):
#         url = self.get_redirect_url()
#         if self.user.is_staff:
#             return redirect('admindashboard')
#         return redirect('userdashboard', username=self.user.username)

@login_required
def current_user_profile(request):
    if request.user.is_staff:
        return redirect('admindashboard', username=request.user.username)
    return redirect('userdashboard', username=request.user.username)


def userdashboard(request, username):
    user = get_object_or_404(CustomUser, username=username)
    context ={
        'user': user
    }
    return render(request, 'users/userdashboard.html', context)

def admindashboard(request, username):
    user = get_object_or_404(CustomUser, username=username)

    context ={
        'user': user
    }
    return render(request, 'users/admindashboard.html', context)