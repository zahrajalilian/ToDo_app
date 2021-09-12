from django.urls import path
from .views import *


urlpatterns = [
    # pages
    path('',home, name='home'),
    path('filter/', filter, name='filter'),
    path('category/', category, name='category'),
    path('search/', search, name='findtask'),
    path('managers/',managers , name='manager'),

    # priority
    path('listbyprih/', HighPriority.as_view(), name='pri_high'),
    path('listbypril/', LowPriority.as_view(), name='pri_low'),
    path('listbyprim/', MiddlePriority.as_view(), name='pri_middle'),
    # category
    path('listbycat1/', Category1.as_view(), name='cat_ed'),
    path('listbycat2/', Category2.as_view(), name='cat_spo'),
    path('listbycat3/', Category3.as_view(), name='cat_tob'),
    path('listbycat4/', Category4.as_view(), name='cat_UD'),
    path('listbycat5/', Category5.as_view(), name='cat_hc'),
    path('listbycat6/', Category6.as_view(), name='cat_djp'),
    # CRUD
    path('list/', ToDoListView.as_view(), name='lists'),
    path('task/new/', ToDoCreateView.as_view(), name='task_new'),
    path('task/<int:pk>/', ToDoDetailView.as_view(), name='task_detail'),
    path('task/<int:pk>/edit/', ToDoUpdateView.as_view(), name='task_edit'),
    path('task/<int:pk>/delete/', ToDoDeleteView.as_view(), name='task_delete'),
    # managers
    # path('find/', FindTask.as_view(), name='find_task'),
    path('searchdata/', searchdata, name='searchdata'),
    path('managetimedata/', managetimedated, name='managetimes'),
    path('managecategoriess/',categoriesmanagement, name='managecategory'),


]
