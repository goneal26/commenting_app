from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.
@login_required
def commentpage(request):
	if request.method == 'POST':
        comment_text = request.POST.get('comment_text', '')
        if comment_text:
            new_comment = Comment.objects.create(
            	author=request.user, text=comment_text)
            return redirect('commentspage')

    comments = Comment.objects.all().annotate(like_count=Count('likes')).order_by('-likes')

    return render(request, 'main.html', {'comments': comments, 'currentuser': request.user.username})

def signup(request):
	return render(request, 'signup.html')

# yeah uh I didn't finish I didn't even get to running it to test it