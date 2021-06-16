from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentForm
from .models import Comment, Subject
# Create your views here.


def forum(request):
    context = {}

    context["dataset"] = Comment.objects.all()
    return render(request, "CommentsSection/forum.html", context)


def create(request):
    form = CommentForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = CommentForm()

    context = {
        'form': form
    }
    return render(request, "CommentsSection/create.html",
                  context)