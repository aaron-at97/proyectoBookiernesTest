from behave import *


@given('I Create Book')
def step_impl(context):
    from eBook.models import Book

    Book.objects.create(id_book="25754321D", title="Ulises", genere="Novela", date="2022-05-12", state="11")
    Book.objects.create(id_book="42754321D", title="Cañas y barro", genere="Novela", date="2022-05-12", state="11")
    Book.objects.create(id_book="97754321D", title="la celestina", genere="Novela", date="2022-05-12", state="11")
    Book.objects.create(id_book="T98765432M", title="Principe del mal", genere="Novela", date="2022-05-12", state="11")
    Book.objects.create(id_book="358265436J", title="libro 5", genere="Novela", date="2022-05-12", state="11")
    Book.objects.create(id_book="Z65865432M", title="libro 6", genere="Novela", date="2022-05-12", state="11")

@when('I list books')
def step_impl(context):
    context.browser.visit(context.get_url('home'))

@then('I\'m viewing a list containing')
def step_impl(context):
    books_links = context.browser.find_by_css('h2#title')
    print(len(context.browser.find_by_css('h2#title')))
    for i, row in enumerate(context.table):
        print(books_links[i].text)
        assert row['title'] == books_links[i].text

@step('The list contains {count:n} books')
def step_impl(context, count):
    assert count == len(context.browser.find_by_css('ul li figure div div img'))