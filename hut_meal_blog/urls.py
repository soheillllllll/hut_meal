from django.urls import path

from hut_meal_blog.views import BlogList2, BlogList1, blog_details, SearchBlogs

app_name = "hut_meal_blog"

urlpatterns = [
    path('blogs-list1/', BlogList1.as_view(), name='blog_list1'),
    path('search-blog/', SearchBlogs.as_view(), name='search_blogs'),
    path('blogs-list2/', BlogList2.as_view(), name='blog_list2'),
    path('blog/<int:blog_id>/<title>/', blog_details, name='blog'),
]
