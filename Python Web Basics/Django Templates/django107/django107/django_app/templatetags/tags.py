from django.template import Library
from django107.django_app.views import Student


register = Library()


@register.simple_tag(name='student_info')
def show_student_info(student: Student):
    return f'Hello, My name is {student.name} and I am {student.age}--years old'


@register.inclusion_tag('tags/nav.html', name='app_nav')
def generate_nav(url_names):
    context = {
        'url_names': url_names,
    }
    return context
