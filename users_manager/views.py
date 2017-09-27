from django.views.generic import(
    ListView, TemplateView, FormView, CreateView, UpdateView, DeleteView
)
from .forms import add_form, message_form, comment_form
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import HttpResponseRedirect



class EditUser(LoginRequiredMixin, UpdateView):
    login_required = True
    model = User
    form_class = add_form
    template_name = 'users_manager/edit.html'
    success_url = '/'

    def get_object(self, **kwargs):
        if 'pk' not in self.kwargs:
            return User.objects.get(
                id=self.request.user.id,
                email=self.request.user.email,
                first_name=self.request.user.first_name,
                last_name=self.request.user.last_name,
                date_joined=self.request.user.date_joined,
                username=self.request.user.username
                )
        else:
            got_object = super(EditUser, self).get_object(**kwargs)
            return got_object
    
    def form_valid(self, form):
        edit_fields = super(EditUser, self).form_valid(form)
        self.object = form.save()
        self.object.first_name = form.cleaned_data['first_name']
        self.object.last_name = form.cleaned_data['last_name']
        self.object.email = form.cleaned_data['email']
        self.object.set_password(form.cleaned_data['password'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NewUser(PermissionRequiredMixin, CreateView):
    permission_required = 'admin'
    form_class = add_form
    template_name = 'users_manager/add.html'
    success_url = '/'


class RemoveUser(PermissionRequiredMixin, DeleteView):
    permission_required = 'admin'
    model = User
    success_url = reverse_lazy('dashboard:user_home')


class PostMessage(LoginRequiredMixin, ListView):
    login_required = True
    template_name = 'users_manager/show.html'
    model = User

    def get_context_data(self, **kwargs):
        context = super(PostMessage, self).get_context_data(**kwargs)
        context['messages'] = User.objects.get(id=self.kwargs['pk']).messages.all()
        return context
