from django.db import models

from hut_meal_blog.models import Blog
from hut_meal_product.models import Product


# Create your models here.


class Comment(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    class Meta:
        ordering = ('created',)



class CommentProduct(Comment):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='comment_products')
    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.product)

class CommentBlog(Comment):
    blog = models.ForeignKey(Blog,
                                on_delete=models.CASCADE,
                                related_name='comment_blogs')
    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.blog)