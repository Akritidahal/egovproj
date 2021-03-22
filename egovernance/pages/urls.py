from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('response', views.response, name='response'),
    path('verified_citizen', views.verified_citizen, name='verified_citizen'),
    path('render', views.render_pdf_view,name='render'),



]