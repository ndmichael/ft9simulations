from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse



class CustomLoginView(LoginView):

    def get_success_url(self):
        url = self.get_redirect_url()
        return url or reverse('staff-detail', kwargs={'id': self.request.user.pk, 'username': self.request.user.username})
