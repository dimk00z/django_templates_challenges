from django.http import HttpRequest, HttpResponse
from django.template.response import TemplateResponse
from django.views.decorators.http import require_GET

"""
У нас есть страница для отображения списка студентов, мы даже передаем их из вьюхи students_view, но на странице их не показываем.
Надо бы это исправить.

Задания:
    1. Найдите в проекте темплэйт students.html и сделайте так, чтобы на странице имя каждого студента выводилось с новой строки.
       Используйте тэмплэйт тэг for для этого и оборачивайте каждое имя в html тэг <p></p>
    2. Откройте страницу http://127.0.0.1:8000/students/ и посмотрите на результат.
"""


@require_GET
def students_view(request: HttpRequest) -> HttpResponse:
    students = [
        "Иван",
        "Мария",
        "Петр",
        "Алексей",
    ]

    return TemplateResponse(
        request,
        "level_1/students.html",
        context={"students": students},
    )
