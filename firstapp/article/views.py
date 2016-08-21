from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import HttpResponse, Http404
from article.models import Article, Comments
from article.forms import CommentForm
from django.views.decorators.csrf import csrf_protect
from django.contrib import auth
from django.core.paginator import Paginator
from django.utils import timezone


# Create your views here.

def basic_one(request):
    view = 'basic_one'
    html = '<html><body>This is %s view</body></html>' % view
    return HttpResponse(html)


def basic_two(request):
    view = 'basic_two'
    t = get_template('myview.html')
    html = t.render(Context({'name': view}))
    return HttpResponse(html)


def basic_three_simple(request):
    view = 'basic_three'
    return render_to_response('myview.html', {'name': view})


def articles(request, page_number=1):
    all_articles = Article.objects.all()
    current_page = Paginator(all_articles, 2)
    return render_to_response('article/articles.html', {'articles': current_page.page(page_number), 'username': auth.get_user(request).username})


@csrf_protect
def article(request, article_id=1):
    commets_form = CommentForm
    args = {}
    args['article'] = get_object_or_404(Article, id=article_id) #Article.objects.get(id=article_id)
    args['comments'] = Comments.objects.filter(comments_article_id=article_id)
    args['form'] = commets_form
    args['username'] = auth.get_user(request).username
    return render(request, 'article/article.html', args)


def addlike(request, article_id):
    try:
        if article_id in request.COOKIES:
            redirect('/')
        else:
            article = Article.objects.get(id=article_id)
            article.article_likes += 1
            article.save()
            response = redirect('/')
            response.set_cookie(article_id, 'test')
            return response
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/')


def addcomment(request, article_id):
    if request.POST and ('pause' not in request.session):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_article = Article.objects.get(id=article_id)
            comment.commets_date = timezone.now()
            comment.comments_from = auth.get_user(request)
            form.save()
            request.session.set_expiry(60)
            request.session['pause'] = True
    return redirect('/articles/get/%s/' % article_id)
