from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.template.loader import render_to_string
from django.views.generic import FormView
import simplejson as simplejson

from .forms import UserProfileForm
from .models import UserProfile

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                data = {
                    'success': True,
                    'msg': 'User is valid, active and authenticated'
                }
                return HttpResponse(simplejson.dumps(data), content_type='application/json')
            else:
                data = {
                    'success': False,
                    'msg': 'The password is valid, but the account has been disabled!'
                }
                return HttpResponse(simplejson.dumps(data), content_type='application/json')
        else:
            data = {
                'success': False,
                'msg': 'The username and password were incorrect.'
            }
            return HttpResponse(simplejson.dumps(data), content_type='application/json')

    data = {
        "string": "Login Page",
    }
    return render(request, 'login.html', data)


def logout_view(request):
    logout(request)
    return redirect('home')


class SettingsView(FormView):
    template_name = 'settings.html'
    form_class = UserProfileForm

    def get_context_data(self, **kwargs):
        context = super(SettingsView, self).get_context_data(**kwargs)
        try:
            user_profile = UserProfile.objects.get(user_id=self.request.user.id)
        except:
            user_profile = {}
        context.update({
            'user_profile': user_profile
        })
        context['object_id'] = self.request.user.id
        return context

    def form_valid(self, form, **kwargs):
        form = UserProfileForm(self.request.POST)
        f = form.save(commit=False)
        f.user = self.request.user
        f.save()
        data = {
            'success': True,
        }
        return HttpResponse(simplejson.dumps(data), content_type='application/json')

    def form_invalid(self, form):
        html = render_to_string(self.template_name, self.get_context_data(form=form))
        data = {
            'success': False,
            'html': html
        }
        return HttpResponse(simplejson.dumps(data), content_type='application/json')

    def render_to_response(self, context, **response_kwargs):
        return super(SettingsView, self).render_to_response(context, **response_kwargs)
