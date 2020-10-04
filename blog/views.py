from django.shortcuts import render,redirect
from .models import Blog
from django.shortcuts import get_object_or_404 
import json
from django.http import HttpResponse
from .forms import post_form
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView


def blog_view(request):
   if request.method =="POST":
       if request.POST.get("operation") == "like_submit" and request.is_ajax():
         content_id=request.POST.get("content_id",None)
         content=get_object_or_404(Blog,pk=content_id)
         if content.likes.filter(id=request.user.id): #already liked the content
            content.likes.remove(request.user) #remove user from likes 
            liked=False
         else:
             content.likes.add(request.user) 
             liked=True
         ctx={"likes_count":content.total_likes,"liked":liked,"content_id":content_id}
         return HttpResponse(json.dumps(ctx), content_type='application/json')

   contents=Blog.objects.all()
   already_liked=[]
   id=request.user.id
   for content in contents:
       if(content.likes.filter(id=id).exists()):
        already_liked.append(content.id)
   context={"contents":contents,"already_liked":already_liked}
   return render(request,"blog.html",context)
   
def create_post(request):
    if request.method=="POST":
        form=post_form(request.POST , request.FILES)
        form.instance.author=request.user
        if form.is_valid():
            form.save()
            return redirect('Blogs:blog')
    else:
        form=post_form()
    return render(request,'add_blog.html',{'form':form})   

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Blog
    success_url = '/blog/userblogs/'
    template_name = 'blog_delete.html'

    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False

def users_blog(request):
    contents=Blog.objects.all().filter(author=request.user)
    return render(request, 'user_blogs.html',{'contents':contents})

