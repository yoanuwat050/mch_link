from tkinter.tix import InputOnly
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (View,TemplateView,ListView,CreateView,DetailView,UpdateView,DeleteView,FormView)
# Add the following line to the top of your code
from django.contrib.auth.decorators import login_required
from repair.models import *
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import logout
from .forms import NewUserForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import permission_required
from emp.models import EmpUser


def RegisterUserView(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            #เมื่อสมัครเสร็จแล้วจะให้เด้งไปหน้าไหน
            return redirect("/login")

        #เพื่อแจ้งเตือน errorต่างๆ
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request = request,
                          template_name = "register.html",
                          context={"form":form}) #นำ form ตรงนี้ไปใช้ใน register.htmlเพื่อrender

    #เนื่อจากข้างบนเป็น if-elseเลยต้องมีเผื่อไว้
    form = NewUserForm
    return render(request = request,
                  template_name = "register.html",
                  context={"form":form})

def LoginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            #เช็คความถูกต้อง
            if user is not None: 
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')#loginเสร็จแล้วไปที่หน้า /admin แก้เป็นหน้าอื่นได้เช่น /home
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "login.html",
                    context={"form":form}) 

def LogoutView(request):
    logout(request)
    #แจ้งว่าlogoutแล้ว แก้ messageได้
    messages.info(request, "Logged out successfully!")
    return redirect("/") #logoutแล้วไปหน้าที่เรากำหนด แก้ได้

#def CreateRepairView(request):
#    if request.method == 'POST':
#        form = NewRepairForm(request=request, data=request.POST)
#        if form.is_valid():
#            repairCause = form.cleaned_data.get('repairCause')
#            #เช็คความถูกต้อง
#            if repairCause is not None: 

 #               messages.info(request, f"y{repairCause}")
 #               return redirect('/repair')#loginเสร็จแล้วไปที่หน้า /admin แก้เป็นหน้าอื่นได้เช่น /home
 #           else:
 #               messages.error(request, "Invalid username or password.")
 #       else:
 #           messages.error(request, "Invalid username or password.")
 #   form = NewRepairForm()
 #   return render(request = request,
 #                   template_name = "repair/repair_form.html",
 #                   context={"form":form}) 





class RepairListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'repair:index'
    context_object_name = 'repair_list'
  
   
    def get_queryset(self,*args,**kwargs):
        query = self.request.GET.get('q')
        print(query)
        if query:
            print("yes")
            queryset = Repair.objects.filter(repairCause__contains=query)
        else:
            print("no")
            #queryset = Repair.objects.filter(repairRequester__empUser=self.request.user).order_by('-id')[:10]
            #queryset = Repair.objects.filter(repairRequester=self.request.user.id).order_by('-id')[:10]
            queryset = Repair.objects.all().order_by('-id')[:20]
            #queryset = Repair.objects.filter(repairRequester__iexact=query)
        return queryset
    model = Repair

class RepairMeListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'repair:index'
    context_object_name = 'repair_list'
  
   
    def get_queryset(self,*args,**kwargs):
        query = self.request.GET.get('q')
        print(query)
        if query:
            print("yes")
            queryset = Repair.objects.filter(repairCause__contains=query)
        else:
            print("no")
            #queryset = Repair.objects.filter(repairRequester__empUser=self.request.user).order_by('-id')[:10]
            #queryset = Repair.objects.filter(repairRequest=self.request.user.id).order_by('-id')[:10]
            queryset = Repair.objects.filter(repairRequester=self.request.user.id).order_by('-id')[:10]
            #queryset = Repair.objects.all().order_by('-id')[:20]
            #queryset = Repair.objects.filter(repairRequester__iexact=query)
        return queryset
    model = Repair

class RepairStaffListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    template_name = 'repair/staff_repair_list.html'
   
    context_object_name = 'staff_repair_list'
  
   
    def get_queryset(self,*args,**kwargs):
        query = self.request.GET.get('q')
        print(query)
        if query:
            print("yes")
            queryset = Repair.objects.filter(repairStaff__first_name__contains=query)
        else:
            print("no")
            mylist = ['2','3']
            #queryset = Repair.objects.filter(repairRequester__empUser=self.request.user).order_by('-id')[:10]
            #queryset = Repair.objects.filter(repairRequest=self.request.user.id).order_by('-id')[:10]
            #queryset = Repair.objects.filter(repairStaff__iexact=query)
            queryset = Repair.objects.filter(repairStatus__in=mylist).order_by('-id')[:20]
            #queryset = Repair.objects.filter(repairStaff__isnull=False).values().order_by('-id')[:20]
            #queryset = Repair.objects.filter(repairRequester__iexact=query)
        return queryset
   
    model = Repair

class RepairMyListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    template_name = 'repair/my_staff_repair_list.html'
   
    #context_object_name = 'staff_repair_list'
  
    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['all'] = Repair.objects.filter(repairStaff=self.request.user.id).count()
        context_data['recieve'] = Repair.objects.filter(repairStaff=self.request.user.id).filter(repairStatus=2).count()
        context_data['work'] = Repair.objects.filter(repairStaff=self.request.user.id).filter(repairStatus=3).count()
        context_data['done'] = Repair.objects.filter(repairStaff=self.request.user.id).filter(repairStatus=4).count()
        context_data['queryset2'] = Repair.objects.filter(repairStaff=self.request.user.id).order_by('repairStatus')[:20]
        return context_data

   # def get_queryset(self,*args,**kwargs):
          
    #    queryset = Repair.objects.filter(repairStaff=self.request.user.id).order_by('repairStatus')[:20]
        
     #   return queryset


    model = Repair


class RepairKnowledgeistView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    template_name = 'repair/knowledge_repair_list.html'
   
    context_object_name = 'knowledge_repair_list'
  
   
    def get_queryset(self,*args,**kwargs):
        query = self.request.GET.get('q')
        print(query)
        if query:
            print("yes")
            queryset = Repair.objects.filter(repairCause__contains=query)
        else:
            print("no")
            mylist = ['2','3','4']
            #queryset = Repair.objects.filter(repairRequester__empUser=self.request.user).order_by('-id')[:10]
            #queryset = Repair.objects.filter(repairRequest=self.request.user.id).order_by('-id')[:10]
            #queryset = Repair.objects.filter(repairStaff__iexact=query)
            queryset = Repair.objects.all().order_by('-id')[:10]
            #queryset = Repair.objects.filter(repairRequester__iexact=query)
        return queryset
    model = Repair




class RepairDetailView(DetailView):
    context_object_name = 'repair'
    model = Repair

   


class RepairCreateView(CreateView):
    model = Repair
    fields = ['repairDetail','repairCause','repairRequester','repairRequestToken']
    success_url = reverse_lazy('repair:repair-me')
    context_object_name = 'create'

        
       
 




class RepairDescUpdateView(UpdateView):
    
    model = Repair
    fields = ['repairDesc','repairStatus','done_time','repairStaff']
    template_name_suffix = '_desc_update_form'
    success_url = reverse_lazy('repair:repair-my')

class RepairWorkUpdateView(UpdateView):
    
    model = Repair
    fields = ['repairStatus','work_time','repairStaff']
    template_name_suffix = '_work_update_form'
    success_url = reverse_lazy('repair:repair-my')
    

class RepairRecieveUpdateView(UpdateView):
    model = Repair
    fields = ['repairStaff','repairStatus','recieve_time']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('repair:repair-my')

class RepairReviewUpdateView(UpdateView):
    model = Repair
    fields = ['repairReview','repairReviewDetail']
    template_name_suffix = '_review_update_form'
    success_url = reverse_lazy('repair:index')

class RepairForwardUpdateView(UpdateView):
    model = Repair
    fields = ['repairStaff','repairStaffForward','forward_time']
    template_name_suffix = '_forward_update_form'
    success_url = reverse_lazy('repair:repair-my')







