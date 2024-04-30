from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *

@login_required # can't comment without logging in
def commentpage(request):
    if request.method == 'POST': #i.e. they submitted a comment through the form
        comment_text = request.POST.get('comment_text', '')
        if comment_text: # get content, create comment object and save
            new_comment = Comment.objects.create(
            	author=request.user, text=comment_text)
            return redirect('commentspage') # reload page

    # grab comments, add field for like counts
    comments = Comment.objects.all().annotate(like_count=Count('likes')).order_by('-likes')

    return render(request, 'main.html', {'comments': comments, 'currentuser': request.user.username})

# view that would've rendered the register page
def signup(request):
	return render(request, 'signup.html')

# yeah uh I didn't finish I didn't even get to running it to test it

# I know how to do everything I think I just fell coz of the time crunch,
# definitely need to brush up on more of the built-in auth stuff instead of writing
# the forms and stuff myself