from django.urls import include,path
from projects import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "projects"

urlpatterns = [
    # name your views in your project
    # first will go to the root of your project, that is /projects
    path('', views.all_projects, name="all_projects"),
    path('<int:pk>', views.project_detail, name="project_detail",)
]