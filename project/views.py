from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (View,TemplateView,ListView,DetailView,CreateView,DeleteView,UpdateView)
from project.models import Project,Stage,Stageupdate
from account.models import Account
# Create your views here.
def in_progress_projects_view(request):

    context = {}
    user = request.user
    if not user.is_authenticated:

        return redirect("home")
    if not user.is_staff:

        return redirect("home")
    #try:

    projects = Project.objects.filter(completion_date__isnull=True)
    stages = Stage.objects.filter(completion_date__isnull=True)

    context['projects'] = projects
    context['stages'] = stages

    #except:
        #return HttpResponse("Something went wrong.")


    return render(request, "project/inprogprojects.html", context)


class StageListView(ListView):
    queryset = Stage.objects.filter(completion_date__isnull=True).order_by('target_completion')

class ProjectCreateView(CreateView):
    model = Project
    fields = ['name','user','description','target_completion']

class ProjectDetailView(DetailView):
    model = Project
    context_object_name = 'project_details'

class StageCreateView(CreateView):
    model = Stage
    fields = ['type','target_completion','info']

    def form_valid(self, form):
        form.instance.project_id = self.kwargs.get('pk')
        return super(StageCreateView, self).form_valid(form)

class StageupdateCreateView(CreateView):
    model = Stageupdate
    fields = ['text']

    def form_valid(self, form):
        form.instance.stage_id = self.kwargs.get('pk')
        return super(StageupdateCreateView, self).form_valid(form)

class UserProjectList(ListView):
    context_object_name = 'user_project_list'
    template_name = 'project/user_project_list.html'
    def get_queryset(self):
        queryset = Project.objects.filter(user = self.kwargs.get('pk'))

        return queryset

class ProjectUpdateView(UpdateView):
    fields = ("name","user","description","target_completion","completion_date")
    model = Project


class ProjectDeleteView(DeleteView):
    model = Project
    success_url = reverse_lazy("project:todo")

class StageUpdateView(UpdateView):
    fields = ("type","target_completion","info","completion_date")
    model = Stage


class StageDeleteView(DeleteView):
    model = Stage
    def get_success_url(self):
        projectId=self.object.project.pk
        return reverse_lazy("project:project_detail",kwargs={'pk':projectId})

class StageupdateUpdateView(UpdateView):
    fields = ('text',)
    model = Stageupdate


class StageupdateDeleteView(DeleteView):
    model = Stageupdate
    def get_success_url(self):
        projectId=self.object.stage.project.pk
        return reverse_lazy("project:project_detail",kwargs={'pk':projectId})
