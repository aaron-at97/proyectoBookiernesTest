from behave import *

use_step_matcher("parse")


@given('I login as user "{username}" with password "{password}" with role "{role}"')
def step_impl(context, username, password, role):
    context.browser.visit(context.get_url('login'))
    from django.contrib.auth.models import User
    from eBook.models import Writer, Clients, Editor
    user = User.objects.create_user(username=username, email='user@example.com', password=password)
    if role == "Writer":
        Writer.objects.create(name=username, role=role, user_id=user.pk)
    if role == "Editor":
        Editor.objects.create(name=username, role=role, user_id=user.pk)
    if role == "Client":
        Clients.objects.create(name="Aaron Arenas Tomas", role=role, nombre="Aaron", apellido="Arenas Tomas",
                               telefon="623456789", codi_postal="12345", correo='user@example.com',
                               direccion="C/ prueba12", user_id=user.pk)
    print(context.browser.html)
    form = context.browser.find_by_tag('form').first

    context.browser.fill('username', username)
    context.browser.fill('password', password)
    form.find_by_value('login').first.click()

    assert context.browser.is_text_present('Welcome')
