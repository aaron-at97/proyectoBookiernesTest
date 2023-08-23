from django.http import HttpRequest
from django.shortcuts import render

from eBook.forms import ClientForm
from eBook.models import Book, Writer, Clients
from django.views.generic import ListView
from eBook.views import get_member
from eBook.views import LoginRequiredMixinStaff

class BooksBiblioteca(ListView, LoginRequiredMixinStaff):
    model = Writer
    template_name = 'books/client/biblioteca.html'

    def get_context_data(self, **kwargs):
        context = super(BooksBiblioteca, self).get_context_data(**kwargs)
        context['writer'] = Writer.objects.filter()
        return context

class EditarPerfil(ListView, LoginRequiredMixinStaff):
    model = Clients
    template_name='books/client/editarPerfil.html'

    def get_context_data(self, **kwargs):
        context = super(EditarPerfil, self).get_context_data(**kwargs)
        member = get_member(self.request.user)
        context['client'] = Clients.objects.filter(name__contains=member)
        return context

#inicio cliente home
class BooksHome2(ListView, LoginRequiredMixinStaff):
    model = Writer
    template_name = 'books/client/general.html'

    def get_context_data(self, **kwargs):
        context = super(BooksHome2, self).get_context_data(**kwargs)
        member = get_member(self.request.user)
        context['role'] = member.role
        context['book'] = Writer.objects.filter(books__state=11)[:4]
        return context


class EditProfile(HttpRequest):

    def procesar_formulario(request, pk):
        client = Clients.objects.get(staff_id=pk)
        clientlist = ClientForm(request.POST, instance=client)
        if clientlist.is_valid():
            clientlist.save()
        return render(request, "books/client/perfilActualizado.html")
