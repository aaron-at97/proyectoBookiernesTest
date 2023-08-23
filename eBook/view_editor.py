from django.http import HttpRequest
from django.shortcuts import redirect
from eBook.forms import AceptRejectForm, rejectForm
from eBook.models import Writer, Book
from django.views.generic import ListView
from eBook.views import LoginRequiredMixinStaff, get_member

class LibrosPorAsignar(ListView, LoginRequiredMixinStaff):
    model = Writer
    template_name = 'books/editor/gene.html'

    def get_context_data(self, **kwargs):
        context = super(LibrosPorAsignar, self).get_context_data(**kwargs)
        member = get_member(self.request.user)
        context['role'] = member.role
        context['editor'] = Writer.objects.filter()
        return context

class LibrosAceptados(ListView, LoginRequiredMixinStaff):
    model = Writer
    template_name='books/editor/libros_aceptados.html'

    def get_context_data(self, **kwargs):
        context = super(LibrosAceptados, self).get_context_data(**kwargs)
        context['book'] = Writer
        return context

class BookPublishWeb(ListView, LoginRequiredMixinStaff):
    model = Writer
    template_name='books/editor/book_publishWeb.html'

    def get_context_data(self, **kwargs):
        context = super(BookPublishWeb, self).get_context_data(**kwargs)
        context['writer'] = Writer.objects.filter()
        return context

class BookRemove(ListView, LoginRequiredMixinStaff):
    model = Writer
    template_name='books/editor/book_remove.html'

    def get_context_data(self, **kwargs):
        context = super(BookRemove, self).get_context_data(**kwargs)
        context['writer'] = Writer.objects.filter()
        return context

class LibrosRechazados(ListView, LoginRequiredMixinStaff):
    model = Writer
    template_name = 'books/editor/libros_rechazados.html'

    def get_context_data(self, **kwargs):
        context = super(LibrosRechazados, self).get_context_data(**kwargs)
        context['book'] = Writer
        return context

class popUpReject(ListView, LoginRequiredMixinStaff):
    model = Writer
    template_name='books/editor/rechazar_libror.html'

    def get_context_data(self, **kwargs):
        context = super(popUpReject, self).get_context_data(**kwargs)
        context['book'] = Book.objects.filter(id=self.kwargs['pk'])
        return context

class AceptBook(HttpRequest):
    def procesar_formulario(request, pk):
        book = Book.objects.get(id=pk)
        clientlist = AceptRejectForm(request.POST, instance=book)
        if clientlist.is_valid():
            clientlist.save()
        return redirect("/book_publish/")

    def deleteBook(request, pk):
        book = Book.objects.get(id=pk)
        if request.method == "POST":
            book.delete()
            return redirect('/book_remove/')

class RejectBook(HttpRequest):
    def procesar_formulario(request, pk):
        book = Book.objects.get(id=pk)
        clientlist = rejectForm(request.POST, instance=book)
        if clientlist.is_valid():
            clientlist.save()
        return redirect("/book_rejected/")