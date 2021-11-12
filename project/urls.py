from django.urls import path

from project.views import (
	in_progress_projects_view,
	StageListView,
	ProjectCreateView,
	ProjectDetailView,
	StageCreateView,
	StageupdateCreateView,
	UserProjectList,
	ProjectUpdateView,
	ProjectDeleteView,
	StageUpdateView,
	StageDeleteView,
	StageupdateUpdateView,
	StageupdateDeleteView,




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
	path('<int:pk>/update', ProjectUpdateView.as_view(),name="project_update"),
	path('<int:pk>/delete', ProjectDeleteView.as_view(),name="project_delete"),
	path('stage/<int:pk>/update', StageUpdateView.as_view(),name="stage_update"),
	path('stage/<int:pk>/delete', StageDeleteView.as_view(),name="stage_delete"),
	path('stageupdate/<int:pk>/update', StageupdateUpdateView.as_view(),name="stageupdate_update"),
	path('stageupdate/<int:pk>/delete', StageupdateDeleteView.as_view(),name="stageupdate_delete"),
]
