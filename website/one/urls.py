from django.conf.urls import url
from . import views
from django.contrib.auth.views import login,logout,password_reset,password_reset_done,password_reset_complete,password_reset_confirm


app_name='one'

urlpatterns = [
    url(r'^profile$',views.profile,name='profile'),
    url(r'^register$',views.UserFormView.as_view(),name='register'),
    url(r'^$', login, {'template_name':'login.html'}, name ="login"), 
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate, name='activate'),
    #password reset urls 
    url(r'^password_reset/$', password_reset,
    {'email_template_name':'password_reset_email.html',
    'subject_template_name':'password_reset_subject.txt',
    'post_reset_redirect':'one:password_reset_done',
    'template_name':'password_reset_form.html'
    }, name='password_reset'),
    url(r'^password_reset/done/$', password_reset_done,{'template_name':'password_reset_done.html'}, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',password_reset_confirm,{'template_name':'password_reset_confirm.html',
    'post_reset_redirect':'one:password_reset_complete',}, name='password_reset_confirm'),
    url(r'^reset/done/$', password_reset_complete,{'template_name':'password_reset_complete.html'}, name='password_reset_complete'),
    url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),
]

