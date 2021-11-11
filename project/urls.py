from django.urls import path

from project.views import (
	in_progress_projects_view,
	StageListView,
	ProjectCreateView,
	ProjectDetailView,
	StageCreateView,
	StageupdateCreateView,
	UserProjectList,



)

app_name = 'project'

urlpatterns = [
	path('in_progress/', in_progress_projects_view, name="gen_in_prog"),
	path('create/', ProjectCreateView.as_view(),name="project_create"),
	path('<int:pk>/', ProjectDetailView.as_view(),name="project_detail"),
	path('to_do/', StageListView.as_view(),name="todo"),
	path('<int:pk>/create/', StageCreateView.as_view(),name="stage_create"),
	path('stageupdate/create/<int:pk>/', StageupdateCreateView.as_view(),name="stageupdate_create"),
	path('user/<int:pk>/', UserProjectList.as_view(),name="user_project_list"),

]
