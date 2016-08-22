from django.shortcuts import render
from data.models import Info,Category
from data.forms import OvizogForm,LoginForm
from django.db import connection
import random

def home(request):
    cat = Category.objects.all()
    context = {'category':cat}
    return render(request,'home.html',context)

def category(request,c_id):
    inf = Info.objects.filter(category=c_id)
    context = {'info':inf,}
    return render(request,'category.html',context)

def ovizog(request):
    form = OvizogForm()
    if request.method=='POST':
        form = OvizogForm(request.POST)
        if form.is_valid():
            o_id = random.randint(1,10000)
            description = form.cleaned_data['description']
            nId = form.cleaned_data['nid']
            authority = form.cleaned_data['authority']
            try:
                cursor = connection.cursor()
                cursor.execute("insert ovizog (o_id,authority,date_time,description,nid) values(%s,%s,now(),%s,%s)",[o_id,authority,description,nId])
                context = {'ovizog':o_id,}
                return render(request,'thanks.html',context)
            except Exception as e:
                error = str(e)
                context = {"form": form,'error':error}
                return render(request, 'ovizog.html', context)
        else:
            error = str(e)
            context = {"form": form, 'error': error}
            return render(request, 'ovizog.html', context)
    else:
        form = OvizogForm()
    context = {"form":form}
    return render(request,'ovizog.html',context)

def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            nId = form.cleaned_data['nid']
            word = form.cleaned_data['word']
            try:
                cursor = connection.cursor()
                cursor.execute("select type from authority where nid=%s", [str(nId), ])
                author = cursor.fetchone()
                print(author)
                if author:
                    cursor.execute("select o_id from ovizog where word=%s",[word,])
                    prob, = cursor.fetchall()
                    context = {'prob':prob}
                    return render(request,'authorprob.html',context)
                else:
                    cursor.execute("select o_id from ovizog where nid=%s",[nId,])
                    data = cursor.fetchall()
                    if data:
                        context = {'data':data,}
                        return render(request,'ovizoglist.html',context)
            except Exception as e:
                error = str(e)
                context = {"form": form, 'error': error}
                return render(request, 'ovizog.html', context)

    return render(request,'login.html')
