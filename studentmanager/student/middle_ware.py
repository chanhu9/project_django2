

def simple_middle(get_response):
    print("这里只执行一次 init")

    def middle(request):
        print("before")
        response = get_response(request)
        print("after")
        return response

    return middle

def simple_middle2(get_response):
    print("这里只执行一次 init")

    def middle(request):
        print("before======")
        response = get_response(request)
        print("after=======")
        return response

    return middle