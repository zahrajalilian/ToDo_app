


#
# import django_filters as filters
# from .models import ToDo
#
#
# class TaskFind(filters.FilterSet):
#     """
#     a custom filter by username.
#     """
#
#     title = filters.CharFilter(label='title', lookup_expr='startswith')
#
#     class Meta:
#         model = ToDo
#         fields = ['title']
#

#
#
# class FindUser(View):
#     """
#     by using a custom filter ,user can search to find another users.This view is used for autocomplete search.
#     """
#
#     def get(self, request):
#         user_filter = UserFilter(request.GET, User.objects.all())
#         # user = request.user
#         return render(request, 'user/find_user.html', {'user_filter': user_filter})
#
