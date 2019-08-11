from django.shortcuts import render
from app1.forms import Form1,Form2
from django.shortcuts import render
from django.views.generic import TemplateView,ListView,UpdateView,CreateView,DetailView,DeleteView
from django.contrib.auth.models import User
from app1.models import UserProfile
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse,reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q


class Home(TemplateView):
    template_name = 'home.html'
'''
class UserList(LoginRequiredMixin,ListView):
    model = UserProfile
    template_name = 'userlist.html'
'''
def userlist(request):
    query=request.GET.get('q',None)
    qs=UserProfile.objects.all()
    if query is not None:
        qs=qs.filter(
            Q(name__icontains=query)|
            Q(webaddress__icontains=query)|
            Q(cover_letter__icontains=query)

           
        )
    context={
        'object_list':qs
    }

    return render(request, 'userlist.html', context)
def register(request):
    form1=Form1()
    form2=Form2()
    if request.method=='POST':
        form1=Form1(data=request.POST)
        form2=Form2(data=request.POST)
        if form1.is_valid() and form2.is_valid():
            user=form1.save()
            user.set_password(user.password)
            user.save()
            profile=form2.save()
            profile.user=user
            profile.save()
        else:
            pass
    else:
        pass
    return render(request,'register.html',{'form1':form1,'form2':form2})

class Detail(LoginRequiredMixin,TemplateView):
    template_name = 'detail.html'

def login1(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return HttpResponseRedirect(reverse('app1:home'))
        else:
            return HttpResponse("your email or password is incorrect")
    return render(request,'login.html',{})

@login_required
def logout1(request):
    logout(request)
    return HttpResponseRedirect(reverse('app1:home'))