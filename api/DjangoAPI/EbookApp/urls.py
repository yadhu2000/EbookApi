from django.urls import re_path as url
from EbookApp import views
#headers for authentication-------------
from EbookApp.views import ListUsers, CustomAuthToken ,authEbooks
#---------------------------------------

urlpatterns=[
    # url(r'^ebooks$',views.EbooksApi),
    # url(r'^ebooks/([0-9]+)$',views.EbooksApi),
    #url patterns for authentication----------
    url('users', ListUsers.as_view()),
    url('token/auth', CustomAuthToken.as_view()),
    url(r'^auth/eBooks$', authEbooks.as_view()),
    url(r'^auth/eBooks/([0-9]+)$', authEbooks.as_view()),
    #------------------------------------------
]