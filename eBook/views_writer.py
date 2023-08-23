from django.http import HttpRequest
from django.shortcuts import render, redirect
from eBook.models import Book, Writer
from django.views.generic import ListView
from eBook.views import LoginRequiredMixinStaff, get_member
from eBook.forms import BookForm, addWriterForm


class BooksList(ListView, LoginRequiredMixinStaff):
    model = Writer
    template_name = 'books/writer/staff_book_list.html'

    def get_context_data(self, **kwargs):
        context = super(BooksList, self).get_context_data(**kwargs)
        member = get_member(self.request.user)
        context['role'] = member.role
        context['writer'] = Writer.objects.filter(name__contains=member)
        return context

class ViewReject(ListView, LoginRequiredMixinStaff):
    model = Book
    template_name = 'books/writer/motivo_rechazo.html'

    def get_context_data(self, **kwargs):
        context = super(ViewReject, self).get_context_data(**kwargs)
        context['book'] = Book.objects.filter(id=self.kwargs['pk'])
        return context

class AsignWriter(ListView, LoginRequiredMixinStaff):
    model = Writer
    template_name='books/writer/aceptarlibro.html'

    def get_context_data(self, **kwargs):
        context = super(AsignWriter, self).get_context_data(**kwargs)
        member = get_member(self.request.user)
        context['writer'] = Writer.objects.filter(name__contains=member)
        context['book'] = Book.objects.filter(id_book__contains=self.kwargs['libropk'])
        return context

class BookCreate(HttpRequest):

    def index(request):
        booklist = BookForm()
        return render(request, "books/writer/create_book.html", {"form": booklist})

    def procesar_formulario(request):
        booklist = BookForm(request.POST)
        if booklist.is_valid():
            booklist.save()
            booklist = BookForm()
        return redirect('writer/save/' + request.POST['id_book'])

    def assign_escriptor(request, pk):
        writer = Writer.objects.get(staff_id=pk)

        writerlist = addWriterForm(request.POST, instance=writer)
        if writerlist.is_valid():
            writerlist.save()
            writerlist = BookForm()
        return render(request, "books/writer/create_book.html", {"form": writerlist, "mensaje": 'OK'})
