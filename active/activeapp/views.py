from django.shortcuts import render
from . models import Sliders,Navbar,Homedata
from . serializers import SlidersSerializer, Homedataserializers,Slidersallserializer
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
# Create your views here.
class Sliderview(viewsets.ModelViewSet):
     queryset= Sliders.objects.filter(title='plant')
     serializer_class=SlidersSerializer

class all(viewsets.ModelViewSet):
     queryset= Sliders.objects.all()
     serializer_class=Slidersallserializer
     parser_classes = (MultiPartParser, FormParser) 

class homedataview(viewsets.ModelViewSet):
     queryset=Homedata.objects.all()
     serializer_class=Homedataserializers

def home_view(request):
    sliders=Sliders.objects.all()
    navbar=Navbar.objects.all()
    return render(request,'home.html',{'sliders':sliders})

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