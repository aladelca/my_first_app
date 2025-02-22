from django.shortcuts import render
from .models import Review
from .forms import ReviewForm
# Create your views here.

def index(request):
    return render(request, 'index.html')

def list_review(request):
    reviews = Review.objects.all()
    return render(request, 'list_review.html', {'reviews': reviews})

def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "index.html")
    else:
        form = ReviewForm()
    return render(request, 'add_review.html', {'form': form})



