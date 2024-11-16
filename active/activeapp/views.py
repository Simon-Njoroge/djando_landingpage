from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request,'home.html')

def about_view(request):
     return render(request,'about.html')

def blog_details_view(request):
     return render(request,'blog-details.html')

def blog_view(request):
     return render(request,'blog.html')

def contact_view(request):
     return render(request,'contact.html')

def portfolio_view(request):
     return render(request,'portfolio.html')

def portfolio_details_view(request):
     return render(request,'portfolio-detaiils.html')

def services_view(request):
     return render(request,'services.html')

def team_view(request):
     return render(request,'team.html')