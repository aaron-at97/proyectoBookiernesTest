from django.urls import path

from django.views.generic import TemplateView
from eBook.auth_views import LoginView
from eBook.models import Writer
from eBook.view_client import BooksBiblioteca, BooksHome2, EditProfile, EditarPerfil
from eBook.view_editor import LibrosPorAsignar, LibrosAceptados, LibrosRechazados, AceptBook, popUpReject, RejectBook, \
    BookPublishWeb, BookRemove
from eBook.views import rolsStaff, BooksHome
from eBook.views_writer import BooksList, BookCreate, AsignWriter, ViewReject
from eBook.view_readBook import Verdemo, LeerLibroSinSession, TraducirLibro, LeerLibro
urlpatterns = [

    path('', BooksHome.as_view(), name="home"),
    path('login/user/libro/<libropk>/aut/', LeerLibroSinSession.as_view(), name="libroSinSession"),
    path('login/demo/<libropk>/aut/', Verdemo.as_view(), name="verDemo"),

    #login
    path('login/index/', rolsStaff.as_view(), name='rolsbook'),
    path('login/', LoginView.as_view(), name="login"),

    #client
    path('user/general', BooksHome2.as_view(), name="general"),
    path('user/biblioteca', BooksBiblioteca.as_view(queryset=Writer.objects.filter(books__state=11)),
         name="biblioteca"),
    path('user/libro/<libropk>/pag/<pagnum>', LeerLibro.as_view(), name="leer_libro"),
    path('user/editarPerfil', EditarPerfil.as_view(), name='editar_perfil'),
    path('user/editarPerfil/save/<str:pk>/', EditProfile.procesar_formulario, name="editar_perfilSave"),

    #writer
    path('list_books/', BooksList.as_view(), name="list_book"),
    path('viewReject/<str:pk>/', ViewReject.as_view(), name="reject_book"),
    path('book_create/', BookCreate.index, name='book_create'),
    path('book_create/save/<str:pk>/', BookCreate.assign_escriptor, name='book_createSave'),
    path('book_create/writer', BookCreate.procesar_formulario, name='book_createWriter'),
    path('book_create/writer/save/<libropk>', AsignWriter.as_view(), name='book_createWriterSave'),

    #editor
    path('book_publish/', LibrosPorAsignar.as_view(), name="book_publish"),
    path('book_acept/save/<str:pk>/', AceptBook.procesar_formulario, name="book_aceptSave"),
    path('book_acept/', LibrosAceptados.as_view(), name="book_acept"),
    path('book_publishweb/', BookPublishWeb.as_view(), name="book_publishweb"),
    path('book_remove/save/<str:pk>/', AceptBook.deleteBook, name="book_removeSave"),
    path('book_remove/', BookRemove.as_view(), name="book_remove"),

    path('book_reject/save/<str:pk>/', RejectBook.procesar_formulario, name="book_rejectSave"),
    path('book_rejected/', LibrosRechazados.as_view(), name='book_rejected'),
    path('book_traduction/sol_traduc2/<libropk>/pag/<pagnum>', TraducirLibro.as_view(), name="solTraduc2"),
    path('book_traduction/sol_traduc', TemplateView.as_view(template_name='books/editor/solicitud_traduccion.html'), name="solTraduc"),

    #editor popUps
    path('book_publish/rejectBook/<str:pk>/', popUpReject.as_view(), name='rejectBook'),
    path('book_traduction/descargar_trad', TemplateView.as_view(template_name='books/editor/descargar_trad.html'), name="descargarPopUp"),
    path('user/libro/trad/', TemplateView.as_view(template_name='books/editor/traduccion_popUp.html'), name="traduccionPopUp"),

]


