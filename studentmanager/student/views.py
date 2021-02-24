from django.shortcuts import render
from django.http import HttpResponse

from django.urls import reverse


# Create your views here.


def studentAll(request):

    return HttpResponse("ok")


def subject(request, value1, value2):

    context = {"v1":value1, "v2":value2}

    # return HttpResponse("课程信息")

    return render(request, "student/subject.html", context)


def classes(request,value2,value1):
    context = {"v1":value1, "v2":value2}



    return render(request, "student/classes.html", context)

def canshu(request, value1, value2):

    a = request.GET.get(value1)
    b = request.GET.get(value2)

    context = {"v1":a,"v2":b}


    return render(request, "student/canshu.html", context)




def get_path(request):

    url = reverse("student:subject")
    url2 = reverse("student:获取路径")

    print(url)
    print(url2)

    return HttpResponse("reverse 函数，返回路径")