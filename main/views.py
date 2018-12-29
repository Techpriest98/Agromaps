from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Corp, Post
from django.views import View
from .forms import CorpForm, PostForm, DeletePostForm
from django.http import HttpResponseRedirect


class CorpView(View):
    decorators = [login_required]
    
    @method_decorator(decorators)
    def get(self, request, id=None):    
        if id != None:
            corp = get_object_or_404(Corp, pk=id)
            corp_form = CorpForm(instance=corp)
            template = 'corp_edit.html'
        else:
            corp_form = CorpForm(instance=Corp())
            template = 'corp_new.html'
        context = {'corp_form':corp_form}
        return render(request, template, context)

    @method_decorator(decorators)
    def post(self, request, id=None):
        print(id)
        context = {}
        if id != None:
            return self.put(request, id)
        corp_form = CorpForm(request.POST, instance=Corp())
        if corp_form.is_valid():
            new_corp = corp_form.save(commit=False)
            new_corp.save()
            return HttpResponseRedirect('/')
        context = {'corp_form' : corp_form}
        return render(request, 'corp_new.html', context)

    @method_decorator(decorators)
    def put(self, request, id=None):
        context = {}
        corp = get_object_or_404(Corp, pk=id)
        corp_form = CorpForm(request.POST, instance=corp)
        if corp_form.is_valid():
            new_corp = corp_form.save(commit=False)
            new_corp.save()
            return HttpResponseRedirect('/')
        context = {'corp_form' : corp_form}
        return render(request, 'corp_edit.html', context) 

class PostView(View):
    decorators = [login_required]
    
    @method_decorator(decorators)
    def get(self, request, id=None):  
        if id != None:
            post = get_object_or_404(Post, pk=id)
            post_form = PostForm(instance=post)
            template = 'post_edit.html'
        else:
            post_form = PostForm(instance=Corp())
            template = 'post_new.html'
        context = {'post_form':post_form}
        return render(request, template, context)

    @method_decorator(decorators)
    def post(self, request, id=None):
        context = {}
        method = self.request.POST.get('_method', '').lower()
        print(method)
        if id != None:
            if method == 'put':
                return self.put(request, id)
            elif method == 'delete':
                return self.delete(request, id)
        post_form = PostForm(request.POST, instance=Post())
        if post_form.is_valid():
            new_post = post_form.save(commit=False)
            new_post.save()
            return HttpResponseRedirect('/news/')
        context = {'post_form' : post_form}
        return render(request, 'post_new.html', context)

    @method_decorator(decorators)
    def put(self, request, id=None):
        context = {}
        post = get_object_or_404(Post, pk=id)
        post_form = PostForm(request.POST, instance=post)
        if post_form.is_valid():
            new_post = post_form.save(commit=False)
            new_post.save()
            return HttpResponseRedirect('/news/')
        context = {'corp_form' : corp_form}
        return render(request, 'post_edit.html', context) 

    def delete(self, request, id=None):
        post = get_object_or_404(Post, pk=id)
        post_form = DeletePostForm(request.POST, instance=post)
        if post_form.is_valid():
            post.delete()
            return HttpResponseRedirect('/news/')
        return render(request, 'post_delete.html', {}) 
        

def index(request):

    corp = Corp.objects.all()[0]
    number = str(corp.phone)

    corp_number = ''
    corp_number += '+' + number[0]+number[1]
    corp_number += ' (' + number[2]+number[3]+number[4]+')'
    corp_number += ' ' + number[5]+number[6]
    corp_number += ' ' + number[7]+number[8]
    corp_number += ' ' + number[9]+number[10]+number[11]

    posts = Post.objects.order_by('-datetime')[0:3]
    #posts = Post.objects.all()
    context = {
        'name' : corp.name,
        'email' : corp.email,
        'number' : corp_number,
        'posts' :  posts
    }
    
    return render(request, 'main/index.html', context)

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    context = {
        'post': post
    }
   
    return render(request, 'main/detail.html', context)

def news(request):
    posts = Post.objects.all().order_by('-datetime')

    context = {
        'posts' : posts 
    }
    return render(request, 'main/news.html', context)    

