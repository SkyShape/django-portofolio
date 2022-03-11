from django.shortcuts import render
from projects.models import Project
# from django.http import HttpResponse



# Create your views here.
# we will not using this
def project_list(request):
    # return None when have nothing
    return render(request, 'projects/index.html')


def all_projects(request):
    # return None when have nothing
    # query the db to return all project objects
    projects = Project.objects.all()
    # print(type(projects))
    return render(request, 'projects/all_projects.html',
                  {'projects': projects})

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    return render(request, 'projects/detail.html',
                  {'project': project},)