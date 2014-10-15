from django.views.generic import TemplateView, View
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest, HttpResponse
from userdata.forms import *


class LoginFormView(TemplateView):
    template_name = 'userdata/login.html'

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(LoginFormView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(LoginFormView, self).get_context_data(**kwargs)
        context.update(form=LoginForm())
        return context


    """
    def post(self, request, *args, **kwargs):
        form = LoginForm()
    """

