from behave import *

@given('To be treat book')
def step_impl(context):
    from eBook.models import Book, Writer
    from django.contrib.auth.models import User

    user = User.objects.create_user(username="escriptor8", email='user@example.com', password="phantom123")
    book = Book.objects.create(id_book="25754321D", title="Ulises", genere="Novela", date="2022-05-12", state="0")
    book1 = Book.objects.create(id_book="42754321D", title="Cañas y barro", genere="Novela", date="2022-05-12", state="0")
    book2 = Book.objects.create(id_book="97754321D", title="la celestina", genere="Novela", date="2022-05-12", state="0")

    writer = Writer.objects.create(name="James Joice", role="Writer", user_id=user.pk)
    writer.books.add(book)
    writer.books.add(book1)
    writer.books.add(book2)

@when('I acept Book')
def step_impl(context):
    context.browser.visit(context.get_url('book_publish'))
    form = context.browser.find_by_tag('form').first
    form.find_by_value('').first.click()

@when('I acept Book in section book rejected')
def step_impl(context):
    context.browser.visit(context.get_url('book_rejected'))
    form = context.browser.find_by_tag('form').first
    form.find_by_value('').first.click()


@then('There are {count:n} books acepted in library')
def step_impl(context, count):
    from eBook.models import Book
    book = Book.objects.filter(state=1)
    assert count == book.count()

@then('There are {count:n} books publicate in library')
def step_impl(context, count):
    from eBook.models import Book
    book = Book.objects.filter(state=11)
    assert count == book.count()

@when('I reject Book name Book "{nameBook}" motive "{body}"')
def step_impl(context, nameBook, body):
    from eBook.models import Book
    book = Book.objects.get(title=nameBook)
    context.browser.visit(context.get_url('rejectBook', book.pk))
    print(book.pk)
    form = context.browser.find_by_tag('form').first
    context.browser.fill('body', body)
    form.find_by_value('').first.click()

@then('There are {count:n} books reject in library')
def step_impl(context, count):
    from eBook.models import Book
    book = Book.objects.filter(state=2)
    assert count == book.count()

@when('I publicate Book Web')
def step_impl(context):
    context.browser.visit(context.get_url('book_publishweb'))
    form = context.browser.find_by_tag('form').first
    form.find_by_value('').first.click()

@when('No acetepted for publicate Book Web')
def step_impl(context):
    context.browser.visit(context.get_url('book_publishweb'))
    assert not context.browser.find_by_tag('form')

@when('Delete book')
def step_impl(context):
    context.browser.visit(context.get_url('book_remove'))
    form = context.browser.find_by_tag('form').first
    form.find_by_value('').first.click()
