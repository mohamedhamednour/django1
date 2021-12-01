from django.shortcuts import render, redirect
from .models import Projects, Projectcomments,Projectpictures,Commentsreport
from .forms import Addproject
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
# Create your views here.

def Addproject(request):
    if (request.method == 'GET'):
        return render (request,'project/Addproject.html',{})
    else:
        print(request.POST)
        form = Addproject(request.POST)
        if (form.is_valid()):
            project = Projects.objects.create(
                project_name = request.POST['Title'],
                Project_details = request.POST['Details'],
                Total_target = request.POST['Totaltarget'],
                Total_donations = request.POST['Totaldonations'],
                start_date = request.POST['StartDate'],
                end_date = request.POST['EndDate'],
                user = request.POST['Owner'],
                Avg_rate = request.POST['Rate'],
                category = request.POST['category']
            )
            if (project):
                return redirect('project/listProjects')
            else:
                return render(request,'project/Addproject.html',{'msg':'error'})
        else:
            return render(request, 'project/Addproject.html', {'msg': 'wrong input'})


def listProjects(request):
    return  HttpResponse('list')