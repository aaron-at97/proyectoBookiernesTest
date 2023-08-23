from behave import *

use_step_matcher("parse")


@when('I register Book')
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('book_create'))
        if context.browser.url == context.get_url('book_create'):
            print(context.browser.html)
            form = context.browser.find_by_tag('form').first
            for heading in row.headings:
                context.browser.fill(heading, row[heading])
            form.find_by_value('submit').first.click()


@then('There are {count:n} books in library')
def step_impl(context, count):
    from eBook.models import Book
    assert count == Book.objects.count()
