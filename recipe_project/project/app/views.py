from django.shortcuts import render, redirect
from .models import Receipe
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,"index.html")


def receipes(request):

    #checking Http requests
    if request.method =="POST":
         
         #extracting data from request
         data = request.POST
         receipe_image = request.FILES.get("receipe_image")
         receipe_name = data.get("receipe_name")
         receipe_description = data.get("receipe_description")


         #creating a new Receipe object
         Receipe.objects.create(
             
           receipe_image = receipe_image,
           receipe_name = receipe_name,
           receipe_description = receipe_description,            
             
        )
         
          #redirecting to receipes      
         return redirect("receipes")
    
    

    #fetching all receipes
    queryset = Receipe.objects.all()

    #filtering receipes based on search query
    if request.GET.get('search'):
        queryset = queryset.filter(receipe_name__icontains = request.GET.get('search'))



    #passing data to template
    context = {'receipes': queryset}



    return render (request, "receipes.html" , context)


def delete_receipe(request , id):
    queryset = Receipe.objects.get(id=id)
    queryset.delete()
    return redirect("/receipes/")

def update_receipe(request , id):

    queryset = Receipe.objects.get(id=id)

    if request.method == "POST":
        data = request.POST

        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')

        queryset.receipe_name = receipe_name
        queryset.receipe_description = receipe_description

        if receipe_image:
            queryset.receipe_image = receipe_image


        queryset.save()
        return redirect('/receipes/')

    context = {'receipe': queryset}

    return render(request , "update.html" , context)