from django.shortcuts import render_to_response

def index(request):
    return render_to_response("index.html")

def about(request):
    return render_to_response("about.html")

def post(request):
    return render_to_response("post.html")

def foto(request):
    return render_to_response("foto.html")

def contact(request):
    return render_to_response("contact.html")
