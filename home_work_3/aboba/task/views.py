from django.http import HttpResponse
from django.middleware.csrf import get_token
from .models import Users


def admin_panel(request):
    csrf_token = get_token(request)

    html = f"""
    <h1>Admin panel</h1>

    <h2>Добавить пользователя</h2>

    <form method="post" action="/admin_panel/add_user/">
        <input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">

        <p>Имя:</p>
        <input type="text" name="name">

        <p>Права:</p>
        <input type="text" name="privileges">

        <p>Описание:</p>
        <textarea name="description"></textarea>

        <br><br>
        <button type="submit">Добавить пользователя</button>
    </form>

    <hr>

    <h2>Удалить пользователя</h2>

    <form method="post" action="/admin_panel/del_user/">
        <input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">

        <p>Имя пользователя:</p>
        <input type="text" name="name">

        <br><br>
        <button type="submit">Удалить пользователя</button>
    </form>
    """

    return HttpResponse(html)


def add_user(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        priv = request.POST.get("privileges", "").strip()
        desc = request.POST.get("description", "").strip()

        if not name:
            return HttpResponse("Ошибка: имя пользователя пустое")

        if not priv:
            return HttpResponse("Ошибка: privileges пустой")

        if Users.objects.filter(name=name).exists():
            return HttpResponse("Такой пользователь уже существует")

        Users.objects.create(
            name=name,
            privileges=priv,
            description=desc
        )

        return HttpResponse(f"Пользователь {name} был создан успешно!")

    return HttpResponse("<h1>Error, method is not allowed, try again</h1>")


def del_user(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()

        if not name:
            return HttpResponse("Ошибка: имя пользователя пустое")

        if Users.objects.filter(name=name).exists():
            Users.objects.filter(name=name).delete()
            return HttpResponse(f"Пользователь {name} был удален!")

        return HttpResponse("Пользователь не найден, поэтому не был удален")

    return HttpResponse("<h1>Error, method is not allowed, try again</h1>")
