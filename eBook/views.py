from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, ListView

from eBook.models import Editor, Writer, Clients, Book
from django.shortcuts import render


class LoginRequiredMixinStaff(object):
    @method_decorator(login_required(login_url='/staff/login'))
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)

def get_member(user):
    if Writer.objects.filter(user=user).exists():
        return Writer.objects.get(user=user)
    elif Editor.objects.filter(user=user).exists():
        return Editor.objects.get(user=user)
    elif Clients.objects.filter(user=user).exists():
        return Clients.objects.get(user=user)
    return None

class rolsStaff(TemplateView):
    template_name = 'navbars/control_rol.html'

    def get_context_data(self, **kwargs):
        context = super(rolsStaff, self).get_context_data(**kwargs)
        member = get_member(self.request.user)
        print(member)
        context['role'] = member.role
        print(context['role'])
        context['writer'] = Writer.objects.filter(name__contains=member)
        context['book'] = Writer.objects.filter(books__state=11)[:4]
        context['editor'] = Writer.objects.filter()
        return context

#home web
class BooksHome(ListView, LoginRequiredMixinStaff):
    model = Writer
    template_name = 'home/home_base.html'

    def get_context_data(self, **kwargs):
        context = super(BooksHome, self).get_context_data(**kwargs)
        stateBook = Book.objects.filter(state=11)
        context['book'] = stateBook.filter()[:4]
        return context

class editorsChief(TemplateView):
    second_model = Book
    template_name = 'books/editor/libros_publicados.html'

    def get_context_data(self, **kwargs):
        context = super(editorsChief, self).get_context_data(**kwargs)
        member = get_member(self.request.user)
        context['role'] = member.role

        return context