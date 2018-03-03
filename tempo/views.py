from django.http import HttpResponse, Http404
import datetime

def hello(reqquest):
    return HttpResponse('Hello World')

def curent_datetime(request):
    now = datetime.datetime.now()
    html = '<html><body>It is currently {} </body></html>'.format(now)
    return HttpResponse(html)

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = '<html><body>Exactly {} hours and {} days to the start of the game</body></html>'.format(offset,dt)
    return HttpResponse(html)