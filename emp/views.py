from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (View,TemplateView,ListView,CreateView,DetailView,UpdateView,DeleteView,FormView)
# Add the following line to the top of your code
from django.contrib.auth.decorators import login_required
from repair.models import *
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import permission_required
from .forms import UpdateUserForm, UpdateProfileForm

from .models import EmpUser
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin

class EmpIndexView(ListView):
    template_name = 'mch_link/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return EmpUser.objects.all()[:5]


class EmpUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    model = EmpUser
    fields = ['empCID','empDepartment','departmentPhone','empPhone','empLineToken']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('emp:index')
    context_object_name = 'empUpdate'


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'users/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('users-home')

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'users/profile.html', {'user_form': user_form, 'profile_form': profile_form})