from django.shortcuts import render, get_object_or_404
from django.shortcuts import HttpResponse

# Create your views here.
from .models import BlogArticles


def blog_title(request):
    blogs = BlogArticles.objects.all()
    return render(request, "blog/titles.html", {"blogs": blogs})
    # return render(request, "blog/titles.html")
    # return HttpResponse(request, "呵呵")


def blog_article(request, article_id):
    # article = BlogArticles.objects.get(id=article_id)
    article = get_object_or_404(BlogArticles, id=article_id)
    pub = article.publish
    return render(request, "blog/content.html", {
        "article": article,
        "publish": pub
    })
