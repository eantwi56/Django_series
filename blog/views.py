from django.shortcuts import render
from django.http import HttpResponse

post = [
  {
      'author': 'CoreyMS',
      'Title': 'Blog Post 1',
      'Content': 'First Post Content',
      'date_posted': 'May 28, 2024'
  
  },
  {
      'author': 'Antwi Emmanuel',
      'Title': 'Blog Post 2',
      'Content': 'Second Post Content',
      'date_posted': 'May 29, 2024'
  }
]


# Create your views here.
def home(request):
    context = {
        'posts': post
    }
    return render(request, 'blog/index.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
