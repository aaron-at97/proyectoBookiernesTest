import json
import sys
import os
import ssl

from urllib import request, parse
from django.shortcuts import render
from django.views.generic import TemplateView

from BookView.settings.settings import BASE_DIR

class LeerLibroSinSession(TemplateView):
    template_name = 'home/libro_SinSession.html'

    def get_context_data(self, **kwargs):
        context = super(LeerLibroSinSession, self).get_context_data(**kwargs)
        context['libro'] = self.kwargs['libropk']
        return context


class LeerLibro(TemplateView):
    template_name = 'books/client/leer_libro.html'

    def get_context_data(self, **kwargs):
        context = super(LeerLibro, self).get_context_data(**kwargs)
        data, pagina, libro = self.read_file(self.kwargs['libropk'], self.kwargs['pagnum'])
        context['data'] = data
        context['anterior'] = int(pagina) - 1
        context['pagina'] = pagina
        context['siguiente'] = int(pagina) + 1
        context['libro'] = libro

        return context

    def read_file(self, libro, pagina):
        data = ""
        try:
            with open(os.path.join(BASE_DIR, 'staticfiles') + "/img/Libros/" + libro + "/" + pagina + ".txt", "r",
                      encoding='utf8') as file:
                # Strip lines
                data = file.read()
        except Exception as e:
            with open(os.path.join(BASE_DIR, 'staticfiles') + "/img/Libros/" + libro + "/" + pagina + ".txt", "r",
                      encoding='iso-8859-1') as file:
                # Strip lines
                data = file.read()
        return data, pagina, libro

def traducir(request):
    libro = request.GET.get("libro")
    idioma = request.GET.get("idioma")

    return render(request, 'books/editor/solicitud_traduccion2.html', {"libropk": libro, "pagnum": idioma})

class TraducirLibro(TemplateView):
    template_name = 'books/editor/solicitud_traduccion2.html'

    def get_context_data(self, **kwargs):
        context = super(TraducirLibro, self).get_context_data(**kwargs)
        data = self.read_file(self.kwargs['libropk'], self.kwargs['pagnum'])
        context['data'] = data

        return context

    def read_file(self, libro, idioma):
        data = ""
        try:
            with open(os.path.join(BASE_DIR, 'staticfiles') + "/img/Libros/" + libro + "/" + "ej.txt", "r",
                      encoding='utf8') as file:
                # Strip lines
                data = file.read()
                data = self.translate(data, "es", idioma, "https://translate.argosopentech.com/translate", libro)
        except Exception as e:
            with open(os.path.join(BASE_DIR, 'staticfiles') + "/img/Libros/" + libro + "/" + "ej.txt", "r",
                      encoding='iso-8859-1') as file:
                # Strip lines
                data = file.read()
                data = self.translate(data, "es", idioma, "https://translate.argosopentech.com/translate", libro)

        return data

    def translate(self, q, source, idioma, url, libro):
        """Connect to LibreTranslate API
        Args:
            q (str): The text to translate
            source (str): The source language code (ISO 639)
            target (str): The target language code (ISO 639)

        Returns: The translated text
        """
        params = {"q": q, "source": source, "target": idioma}

        url_params = parse.urlencode(params)

        req = request.Request(url, data=url_params.encode())

        try:
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE
            response = request.urlopen(req, context=ctx)
        except Exception as e:
            print("No puedo abrir la web")
            print(e, sys.stderr)
            return None

        try:
            response_str = response.read().decode()
        except Exception as e:
            print(e, sys.stderr)
            return None

        data = ""
        data = str(json.loads(response_str))
        print(data)
        nueva = ""
        ant = ""
        data = data[20:len(data)-2]

        for c in data:
            if c == '\\':
                nueva = nueva + " \n "
            elif ant == '\\':
                pass
            else:
                nueva = nueva + c
            ant = c
        try:
            with open(os.path.join(BASE_DIR, 'staticfiles') + "/img/Libros/" + libro + "/" + idioma + "/1.txt", 'w',
                      encoding='utf8') as file_write:
                # write json data into file
                file_write.write(nueva)
                file_write.close()

        except Exception as e:
            with open(os.path.join(BASE_DIR, 'staticfiles') + "/img/Libros/" + libro + "/" + idioma + "/1.txt", 'w',
                      encoding='iso-8859-1') as file_write:
                # Strip lines
                # write json data into file
                file_write.write(nueva)
                file_write.close()

        return data

class Verdemo(TemplateView):
    template_name = 'home/ver_demo.html'

    def get_context_data(self, **kwargs):
        context = super(Verdemo, self).get_context_data(**kwargs)
        print(self.kwargs['libropk'])
        data, libro = self.read_file(self.kwargs['libropk'], "1")
        print(data)
        context['data'] = data
        context['libro'] = libro

        return context

    def read_file(self, libro, pagina):
        data = ""
        try:
            with open(os.path.join(BASE_DIR, 'staticfiles') + "/img/Libros/" + libro + "/" + pagina + ".txt", "r",
                      encoding='utf8') as file:
                # Strip lines
                data = file.read()
        except Exception as e:
            with open(os.path.join(BASE_DIR, 'staticfiles') + "/img/Libros/" + libro + "/" + pagina + ".txt", "r",
                      encoding='iso-8859-1') as file:
                # Strip lines
                data = file.read()
        print(data)
        return data, libro
