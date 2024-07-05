from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.base import View
from django.contrib import messages
from api.serializers import MapSerializer
from .forms import RegisterForm


class UserIsNotAuthenticated(UserPassesTestMixin):
    def test_func(self):
        if not self.request.user.is_superuser:
            messages.success(self.request, 'Вы не Администратор. Вы не можете посетить эту страницу.')
            return False
        return True

    def handle_no_permission(self):
        return redirect('/api/login/')


class SignUp(LoginRequiredMixin, UserIsNotAuthenticated, View):
    template_name = 'registration/signup.html'
    login_url = 'api/login/'

    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        print(form)
        context = {'form': form}
        return render(request=request, template_name=self.template_name, context=context)

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            maps = form.cleaned_data.get('maps', [])
            data = {'user': user.pk, 'maps': maps}
            serializer = MapSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.create(serializer.data)
            messages.success(request, 'new user added')
            return render(request=request, template_name=self.template_name)

        context = {'form': form}
        return render(request=request, template_name=self.template_name, context=context)
