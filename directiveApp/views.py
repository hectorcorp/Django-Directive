from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    name = request.POST['name']
    email = request.POST["email"]
    message = request.POST["message"]
    context = {"usersemail": email, "usersname": name, "usersmessage": message}
    template = loader.get_template("home.html")
    #template = ("<h1>User email: {email}   </h1>")
    return HttpResponse(template.render(context, request))