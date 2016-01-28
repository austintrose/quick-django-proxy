from django.conf.urls import url
from django.contrib import admin

from django.http import HttpResponse
import urllib2

def proxy_img_view(url):
    def view(request):
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        return HttpResponse(response.read(), content_type="image/png")
    return view

def google(request):
    view = proxy_img_view('http://www.google.com/images/nav_logo242_hr.png')
    return view(request)

def facebook(request):
    view = proxy_img_view('http://static.xx.fbcdn.net/rsrc.php/v2/y1/r/wbGFLRt-sam.png')
    return view(request)

def amazon(request):
    view = proxy_img_view('http://g-ecx.images-amazon.com/images/G/01/AUIClients/AmazonUIBaseCSS-sprite_2x-226eca6867acbf88de65f69383ea33c9a02ffc17._V2_.png')
    return view(request)

def wikipedia(request):
    view = proxy_img_view('http://www.wikipedia.org/portal/wikipedia.org/assets/img/Wikipedia-logo-v2_2x.png')
    return view(request)

def twitter(request):
    view = proxy_img_view('http://abs.twimg.com/a/1453865360/img/t1/lohp_streams_header_bg_v4.png')
    return view(request)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^google/', google),
    url(r'^facebook/', facebook),
    url(r'^amazon/', amazon),
    url(r'^wikipedia/', wikipedia),
    url(r'^twitter/', twitter),
]
