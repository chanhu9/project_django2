from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import redirect


from django.urls import reverse

import json
# Create your views here.


def studentAll(request):

    return HttpResponse("ok")


def subject(request, value1, value2):
    # 位置参数

    context = {"v1":value1, "v2":value2}

    # return HttpResponse("课程信息")

    return render(request, "student/subject.html", context)


def classes(request,value2,value1):

    # 关键字参数

    context = {"v1":value1, "v2":value2}

    return render(request, "student/classes.html", context)



def studentone(request):
    #查询字符串 query_string,注意QueryDict
    data = request.GET
    print(data)

    name = data["name"]
    banji = data.get("classes")

    name2 = data.getlist("name")

    print(name, banji, name2)

    return HttpResponse("ok")

def student2(request):

    # 获取请求体里面的数据，post请求，form_data格式
    data = request.POST
    print(data)

    name = data['name']
    banji = data.get('banji')

    name2 = data.getlist('name')
    print(name,banji)
    print(name2)

    return HttpResponse("ok2")

def student3(request):
    # post请求，获取json格式的参数

    data = request.body
    data2 = data.decode()
    print(data2)

    print(type(data2))

    res = json.loads(data2)
    print(type(res))

    name = res["name"]
    banji = res.get("banji")

    print(name, banji)

    return HttpResponse("ok3")

def student4(request):
    # 获取请求头里面的数据和其他

    header = request.META
    # print(header)
    # print(header['HTTP_TYPE'])

    print(request.method)
    print(request.user)
    print(request.path)

    return HttpResponse("ok4")


def student5(resquest):
    # HttpResponse JsonResponse响应

    data = {"name":"关羽"}

    # data = "guanyu"

    return JsonResponse(data)

    # return HttpResponse(content=data, status=300, content_type="text/plain")

def student6(request):

    # return redirect("http://www.baidu.com")

    path = reverse("student:stu4")

    return redirect(path)


def canshu(request, value1, value2):

    a = request.GET.get(value1)
    b = request.GET.get(value2)

    context = {"v1":a,"v2":b}


    return render(request, "student/canshu.html", context)


def get_path(request):

    url = reverse("student:stu1")
    url2 = reverse("student:stu2")

    print(url)
    print(url2)

    return HttpResponse(url2)

def set_cookie(request):

    # 1:假设没有cookie

    # 2:获取数据，设置cookie
    name = request.GET.get("name")

    response = HttpResponse("set_cookie")
    response.set_cookie("name", name, max_age=3600)
    # 3:返回cookie信息

    return response

def get_cookie(request):

    data = request.COOKIES
    name = data.get("name")
    print(name)

    return HttpResponse("get_cookie")

def set_session(request):

    print(request.COOKIES)

    member_id = 6

    request.session["member_id"] = member_id

    return HttpResponse("set_session")


def get_session(request):

    print(request.COOKIES)

    member_id = request.session["member_id"]

    print(member_id)

    return HttpResponse("get_session")