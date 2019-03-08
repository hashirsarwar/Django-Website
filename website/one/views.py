from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import View
from .forms import user_form
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User


def profile(request):
    if User.is_authenticated:

        return render(request,'one/profile.html',{'name':request.user.username})    

class UserFormView(View):
    form_class = user_form
    template_name = 'one/register_form.html'

    def get (self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post (self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.is_active=False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your account'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
        return render(request,self.template_name,{'form':form})
 
    
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()            
        if user is not None:
            if user.is_active:
                login(request, user)
        return HttpResponse('Thank you for your email confirmation. Now you can <a href="/login">login your account</a>')
    else:
        return HttpResponse('Activation link is invalid!')

def logout_view(request):
    logout(request)

