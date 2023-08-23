from django.contrib import admin
import eBook.models

admin.site.register(eBook.models.Book)
admin.site.register(eBook.models.Writer)
admin.site.register(eBook.models.Editor)
admin.site.register(eBook.models.Clients)
