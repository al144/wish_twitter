from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.conf import settings
from django.http import FileResponse, HttpRequest, HttpResponse

def display(req: HttpRequest, site: str='index', extra: dict = {}) -> HttpResponse | HttpResponseNotFound:
    """display() is the default function to display static sites/subsites with close to no dynamic content

    Args:
        req (request): request
        site (str, optional): The path of the request. Defaults to 'index'.

    Returns:
        HttpResponse: on success
        HttpResponseNotFound: on missing site (404 error)
    """
    try:
        return render(req, f'{site}.html')
    except :
        print("error")
        eresp = HttpResponseNotFound()
        return eresp
 
