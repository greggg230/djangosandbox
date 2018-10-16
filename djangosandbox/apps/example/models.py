from django.db import models


class BlogPost(models.Model):
    datetime_added = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('auth.User', related_name='blog_posts')
    title = models.CharField(max_length=255, unique=True)
    content = models.TextField()

    def __unicode__(self):
        return "{0} ({1})".format(self.title, self.datetime_added)
