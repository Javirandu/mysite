from django.http import HttpResponse


def set_cookie(request):
    print(request.COOKIES)
    old_cookie = request.COOKIES.get('dj4e_cookie', None)
    response = HttpResponse('cookie value' + str(old_cookie))
    # if old_cookie:
    #     response.set_cookie('dj43_cookie', int(old_cookie) + 1)  # cookie is deleted when browser closes
    # else:
    #     response.set_cookie('dj43_cookie', int(old_cookie))
    response.set_cookie('dj4e_cookie', '7061e05f', max_age=1000)  # cookie expires in 1k seconds
    return response


def hello(request):
    print(request.COOKIES)
    visits = request.session.get('visits', 0) + 1
    request.session['visits'] = visits
    if visits > 4:
        del(request.session['visits'])
    response = HttpResponse('Cookie 7061e05f')
    response.set_cookie('dj4e_cookie', '7061e05f', max_age=1000)
    response = HttpResponse('view count=' + str(visits))
    return HttpResponse(response)
