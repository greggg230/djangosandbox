from django.views.generic import TemplateView

from djangosandbox.apps.example.models import BlogPost


class IndexView(TemplateView):
    template_name = "example/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        # Get all blog posts, sorted by datetime added in descending order.
        context['blog_posts'] = BlogPost.objects.order_by('-datetime_added')
        return context


class DetailView(TemplateView):
    template_name = "example/detail.html"
