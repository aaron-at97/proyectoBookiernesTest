from behave import *

use_step_matcher("parse")

@when('I modify a namePage at client "{name}"')
def step_impl(context, name):
    context.browser.visit(context.get_url('editar_perfil'))
    form = context.browser.find_by_tag('form').first
    context.browser.fill('name', name)
    form.find_by_value('Modify').first.click()
    assert context.browser.is_text_present('Profile updated successfully')

@when('I modify a telefon at client "{telefon}"')
def step_impl(context, telefon):
    context.browser.visit(context.get_url('editar_perfil'))
    form = context.browser.find_by_tag('form').first
    context.browser.fill('telefon', telefon)
    form.find_by_value('Modify').first.click()
    assert context.browser.is_text_present('Profile updated successfully')

@when('I modify a name at client "{nombre}"')
def step_impl(context, nombre):
    context.browser.visit(context.get_url('editar_perfil'))
    form = context.browser.find_by_tag('form').first
    context.browser.fill('nombre', nombre)
    form.find_by_value('Modify').first.click()
    assert context.browser.is_text_present('Profile updated successfully')

@when('I modify a postal code at client "{codi_postal}"')
def step_impl(context, codi_postal):
    context.browser.visit(context.get_url('editar_perfil'))
    form = context.browser.find_by_tag('form').first
    context.browser.fill('codi_postal', codi_postal)
    form.find_by_value('Modify').first.click()
    assert context.browser.is_text_present('Profile updated successfully')

@when('I modify a name, telefon and email at client "{nombre}" "{telefon}" "{email}"')
def step_impl(context, nombre, telefon, email):
    context.browser.visit(context.get_url('editar_perfil'))
    form = context.browser.find_by_tag('form').first
    context.browser.fill('nombre', nombre)
    context.browser.fill('codi_postal', telefon)
    context.browser.fill('correo', email)
    form.find_by_value('Modify').first.click()
    assert context.browser.is_text_present('Profile updated successfully')


@when('I modify all elements')
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('editar_perfil'))
        if context.browser.url == context.get_url('editar_perfil'):
            form = context.browser.find_by_tag('form').first
            for heading in row.headings:
                context.browser.fill(heading, row[heading])
            form.find_by_value('Modify').first.click()