from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.list import ListView
from hut_meal_blog.models import Blog
from hut_meal_comment.forms import CommentBlogForm


# Create your views here.





class BlogList1(ListView):
    template_name = 'blog-list1.html'
    paginate_by = 4
    def get_queryset(self):
        return Blog.objects.get_active_blog()


class BlogList2(BlogList1):
    template_name = 'blog-list2.html'
    paginate_by = 4


def blog_details(request, *args, **kwargs):
    comment_form = CommentBlogForm(request.POST or None)
    blog_id = kwargs['blog_id']
    blog_details = Blog.objects.get_blog_by_id(blog_id)
    related_blogs = Blog.objects.get_queryset().filter(categories__blog=blog_details).distinct()[:3]
    comments = blog_details.comment_blogs.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentBlogForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.blog = blog_details
            new_comment.save()
            return HttpResponseRedirect(request.path_info)
    blog_details.visits += 1
    blog_details.save()
    context = {
        'blog_details': blog_details,
        'related_blogs': related_blogs,
        'comments':comments,
        'new_comment': new_comment,
        'comment_form': comment_form
    }
    return render(request, 'blog-detail.html', context)

class SearchBlogs(ListView):
    template_name = 'blog-list2.html'
    paginate_by = 10
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query is not None:
            return Blog.objects.search_blogs(query)
        return Blog.objects.get_active_blog()


def latest_posts(request):
    blogs = Blog.objects.order_by().all()[:4]
    context = {'blogs': blogs}
    return render(request, 'latest_posts.html', context)