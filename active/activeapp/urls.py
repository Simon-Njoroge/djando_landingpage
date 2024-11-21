from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_view, name='home'),
    path('en-us/about/',views.about_view,name='about'),
    path('en-us/blogdetails/',views.blog_details_view, name='blogdetails'),
    path('en-us/blog',views.blog_view, name='blog'),
    path('en-us/contact/',views.contact_view,name='contact'),
    path('en-us/portfolio/',views.portfolio_view,name='portfolio'),
    path('en-us/portfolio-details/',views.portfolio_details_view,name='portfoliodetails'),
    path('en-us/services/', views.services_view,name='services'),
    path('en-us/team/',views.team_view,name='team')
]
