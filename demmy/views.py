from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse

# Create your views here.
def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <head>
            <title>Django Admin Rest API </title>
        </head>
        <body>
            <h2>Admin Rest API Application Working {now}.
        </body>
    </html>'''
    return HttpResponse(html)