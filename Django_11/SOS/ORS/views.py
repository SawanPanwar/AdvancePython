from django.db import connection
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import StudentForm
from django.contrib.sessions.models import Session

def hello(request):
    return HttpResponse('<h1>Hello Python</h1>')


def user(request, id = 0, name = ""):
    message = "User id = " + str(id)
    return HttpResponse(message)


def registration(request):
    if request.method=="POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Registration Successfully.....")
        else:
            return HttpResponse("PLz... fill all fields")

    return render(request,"Registration.html")


def search(request):
    list = [{"id":1, "name":"Vikash"},
            {"id":2, "name":"Mohit"},
            {"id":3, "name":"Atharv"},
            {"id":4, "name":"Sawan"},]
    return render(request, "List1.html", {"list":list, "flag":True})


def create_session(request):
    request.session['name'] = 'Admin'
    response = "<h1>Welcome To Sessions</h1><br>"
    response += "ID : {0} <br>".format(request.session.session_key)
    return HttpResponse(response)


def access_session(request):
    response = "Name : {0} <br>".format(request.session.get('name'))
    return HttpResponse(response)


def destroy_session(request):
    Session.objects.all().delete()
    return HttpResponse("Session is Destroy")


def setCookies(request):
    if request.method=="POST":
        name = request.POST.get('cookieName')
        value = request.POST.get('cookieValue')
        res = HttpResponse("<h1>Rays Technologies</h1>")
        res.set_cookie("name", name)
        res.set_cookie("value", value)
        return res
    return render(request, "SetCookies.html")


def getCookies(request):
    name = request.COOKIES.get('name')
    value = request.COOKIES.get('value')
    html = "<center> name = {} <br> value = {} </center>".format(name, value)
    return HttpResponse(html)


def index(request):
    msg = "Welcome to Rays....."
    return render(request, "index.html", {"message": msg})


def red(request):
    return redirect("/ORS/Reg/")


def display(request):
    sql = "select * from sos_student"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    columnName = ("id", "firstName", "lastName", "email", "password")
    res = {
        "data": []
    }
    count = 0
    for x in result:
        print(x)
        print({columnName[i]: x[i] for i, _ in enumerate(x)})
        res["data"].append({columnName[i]: x[i] for i, _ in enumerate(x)})
    return render(request, "List.html", {"list": res['data']})


def edit(request, id):
    print(id)
    result = ""
    sql = "select * from sos_student where id = (%s)"
    data = [id]
    cursor = connection.cursor()
    cursor.execute(sql, data)
    result = cursor.fetchall()
    columnName = ("id", "firstName", "lastName", "email", "password")
    res = {
        "data": []
    }
    count = 0
    for x in result:
        print({columnName[i]: x[i] for i, _ in enumerate(x)})
        res["data"].append({columnName[i]: x[i] for i, _ in enumerate(x)})
    return render(request, "UpdateReg.html", {"list": res['data']})


def update(request):
    if request.method=="POST":
        id = request.POST.get('id')
        fn = request.POST.get('firstName')
        ln = request.POST.get('lastName')
        e = request.POST.get('email')
        p = request.POST.get('password')
        sql = "update sos_student set firstName = (%s), lastName = (%s), email = (%s), password = (%s) where id = (%s)"
        data = [fn, ln, e, p, id]
        cursor = connection.cursor()
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        return HttpResponse("Update Successfully.....")
    return HttpResponse("Update Failed.....")


def delete(request, id):
    sql = "delete from sos_student where id = (%s)"
    data = [id]
    cursor = connection.cursor()
    cursor.execute(sql, data)
    return HttpResponse("Data Delete Successfully.....")


def login(request):
    if request.method == "POST":
        e = request.POST.get('email')
        p = request.POST.get('password')
        sql = "select * from sos_student where email = (%s) and password = (%s)"
        data = [e, p]
        cursor = connection.cursor()
        cursor.execute(sql, data)
        result = cursor.fetchall()
        columnName = ("id", "firstName", "lastName", "email", "password")
        res = {
            "data": []
        }
        count = 0
        for x in result:
            print({columnName[i]: x[i] for i, _ in enumerate(x)})
            res["data"].append({columnName[i]: x[i] for i, _ in enumerate(x)})
        return render(request, "UpdateReg.html", {"list": res['data']})
    return render(request, "Vikash.html")