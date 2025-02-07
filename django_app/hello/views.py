from typing import Any
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Friend
from .forms import FriendForm
# from .forms import FindForm
from .forms import CheckForm
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator

# def find(request):
#   if (request.method == "POST"):
#     form = FindForm(request.POST)
#     find = request.POST['find']
#     data = Friend.objects.filter(name__contains=find)
#     msg = 'Result:' + str(data.count())
#   else:
#     msg = 'search words '
#     form = FindForm()
#     data = Friend.objects.all()
#   params = {
#     'title':'Hello',
#     'message':msg,
#     'data':data,
#   }
#   return render(request, 'hello/find.html', params)


def index(request, num=1):
  data = Friend.objects.all()
  page = Paginator(data, 3)
  params = {
    'title':'Hello',
    'message':'Hello',
    'data':page.get_page(num),
  }
  return render(request, 'hello/index.html', params)

def create(request):
  if (request.method =='POST'):
    obj = Friend()
    friend = FriendForm(request.POST, instance=obj)
    friend.save()
    return redirect(to='/hello')
  
  params = {
    'title':'Hello',
    'form':FriendForm(),
  }
  return render(request, 'hello/create.html', params)

def edit(request, num):
  obj = Friend.objects.get(id=num)
  if (request.method == 'POST'):
    friend = FriendForm(request.POST, instance=obj)
    friend.save()
    return redirect(to='/hello')
  params = {
    'title':'Hello',
    'id':num,
    'form':FriendForm(instance=obj),
}
  return render(request, 'hello/edit.html', params)

def delete(request, num):
  friend = Friend.objects.get(id=num)
  if (request.method == 'POST'):
    friend.delete()
    return redirect(to='/hello')
  params = {
    'title':'Hello',
    'id':num,
    'obj':friend,
  }
  return render(request, 'hello/delete.html', params)

class FriendList(ListView):
  model = Friend
  
class FriendDetail(DetailView):
  model = Friend

def check(request):
  params = {
    'title':'Hello',
    'message':'check validation',
    'form':FriendForm(),
  }
  if (request.method=='POST'):
    obj = Friend()
    form = FriendForm(request.POST, instance=obj)
    params['form'] = form
    if(form.is_valid()):
      params['message'] = 'OK'
    else:
      params['message'] = 'no good'
  return render(request, 'hello/check.html', params)
