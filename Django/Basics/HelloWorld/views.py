from django.http import HttpResponse # HttpResponse class return empty string
from django.shortcuts import render

# Create your views here.

"""def index(request):
    response = HttpResponse("Hello World") #HttpResponse class takes string as a parameter and returns it to the response object
    return response"""

# So as above we were returning string. Now we will return class objects
def index(request):
    developed_by = "Vivek Kumar"
    collaborators =[
        "Servesh Khandwe",
        "USP Anupam",
        'Vivek Kumar'
    ]

    show_dev = True
#with the help of this context dict, the above declared variable and list can be accesed in the html file using the keys of dict
    context = {
        "developer":developed_by,
        "collaborators":collaborators,
        "show_dev": show_dev
    }

    response = render(request, template_name='HelloWorld/index.html', context=context) #and the context is passed to the html file here
    return response

def hello(request):
    return render(request, 'HelloWorld/hello.html')