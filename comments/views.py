from django.shortcuts import render,get_object_or_404,redirect
from .models import Comment
from .forms import CommentForm
from blogapp.models import Post
# Create your views here.

def post_comment(request,post_pk):
    post = get_object_or_404(Post,pk=post_pk)
<<<<<<< HEAD
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
=======

    if request.method == 'POST':

        form = CommentForm(request.POST)

        if form.is_valid():

            comment = form.save(commit=False)

>>>>>>> dfef5ddfaf6e0c05cb8bbf58d838d238f9b5fe67
            comment.post = post

            comment.save()

            return redirect(post)
        else:

            comment_list = post.comment_set.all()
            context = {'post':post,
                       'form':form,
                       'comment_list':comment_list}
            return render(request,'blog/detail.html',context=context)
        return redirect(post)
