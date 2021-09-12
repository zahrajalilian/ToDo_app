"""
import scope
"""
from django.shortcuts import render
# from django.views import View

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import ToDo
from django.urls import reverse_lazy

############################################


"""
load pages with render
"""


def home(request):
    """
    homepage loading method
    """
    return render(request, 'home.html')


def filter(request):
    """
       filter  by priority page loading method
       """
    return render(request, 'filters.html')


def category(request):
    """
       category page loading method
       """
    return render(request, 'categories.html')


def search(request):
    """
       category page loading method
       """
    return render(request, 'find_task.html')


def managers(request):
    """
       manager page loading method
       """
    return render(request, 'managers.html')




class ToDoCreateView(CreateView):
    model = ToDo
    template_name = 'task_new.html'
    fields = ['title', 'description', 'priority', 'due_date_time', 'category']


class ToDoListView(ListView):
    model = ToDo
    template_name = 'all_tasks.html'
    queryset = ToDo.objects.order_by('-due_date_time')
    context_object_name = 'tasks_all'


class ToDoDetailView(DetailView):
    model = ToDo
    template_name = 'task_detail.html'
    context_object_name = 'tasks_obj'


class ToDoUpdateView(UpdateView):
    model = ToDo
    template_name = 'task_edit.html'
    fields = ['title', 'description', 'priority', 'due_date_time', 'category']


class ToDoDeleteView(DeleteView):
    model = ToDo
    template_name = 'task_delete.html'
    success_url = reverse_lazy('home')


# ####################################################
"""
filter by priority:
High Priority
Middle Priority
Low Priority

"""


class HighPriority(ListView):
    """
    filter by High Priority
    """
    model = ToDo
    template_name = 'filters.html'
    queryset = ToDo.objects.filter(priority__exact='HIGH')
    context_object_name = 'priority_list'


class MiddlePriority(ListView):
    """
        filter by Middle Priority
        """
    model = ToDo
    template_name = 'filters.html'
    queryset = ToDo.objects.filter(priority__exact='MIDDLE')
    context_object_name = 'priority_list'


class LowPriority(ListView):
    """
        filter by Low Priority
        """
    model = ToDo
    template_name = 'filters.html'
    queryset = ToDo.objects.filter(priority__exact='LOW')
    context_object_name = 'priority_list'


################################################################


"""
filter by category:
 
"""


class Category1(ListView):
    """
     Education category
    """

    model = ToDo
    template_name = 'categories.html'
    queryset = ToDo.objects.filter(category__exact='Education')
    context_object_name = 'category_list'


class Category2(ListView):
    """
      sports category
    """
    model = ToDo
    template_name = 'categories.html'
    queryset = ToDo.objects.filter(category__exact='sports')
    context_object_name = 'category_list'


class Category3(ListView):
    """
     ToBuy category
    """

    model = ToDo
    template_name = 'categories.html'
    queryset = ToDo.objects.filter(category__exact='ToBuy')
    context_object_name = 'category_list'


class Category4(ListView):
    """
     undecided category
    """
    model = ToDo
    template_name = 'categories.html'
    queryset = ToDo.objects.filter(category__exact='undecided')
    context_object_name = 'category_list'


class Category5(ListView):
    """
     'House Chores' category
    """
    model = ToDo
    template_name = 'categories.html'
    queryset = ToDo.objects.filter(category__exact='House Chores')
    context_object_name = 'category_list'


class Category6(ListView):
    """
     'Django Project' category
    """
    model = ToDo
    template_name = 'categories.html'
    queryset = ToDo.objects.filter(category__exact='Django Project')
    context_object_name = 'category_list'


#########################################################
"""
search data by title
"""


def searchdata(request):
    q = request.GET['query']
    mydictionary = {
        "alltodos" : ToDo.objects.filter(title__contains=q)
    }
    return render(request,'find_task.html',context=mydictionary)

##########################################


"""
managers
"""


def managetimedated(request):
    """

    use managers to return out dated tasks
    """

    mydictionary = {
        "datas" : ToDo.time_manager.all()
    }
    return render(request,'managers.html',context=mydictionary)


"""
manage category
"""

def categoriesmanagement(request):
    """

    use managers to return category usage
    """

    mydictionary = {
        "full" : ToDo.categoryManager.full(),
        "empty" : ToDo.categoryManager.empty(),

    }
    return render(request,'manage_category.html',context=mydictionary)




