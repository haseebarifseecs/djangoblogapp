from django.core.paginator import  Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from .models import blogPost, PostView
from django.db.models import Count, Q
from marketing.models import Signup
from django.contrib.auth.decorators import login_required
from .forms import blogPostCreationForm
from django.urls import reverse
from django.contrib.auth.models import User


def get_user(user):
    qs = User.objects.filter(username=user)
    if qs.exists():
        return qs[0]
    return None


def search(request):
    queryset = blogPost.objects.all()
    query = request.GET.get('q')
    if query:
        queryset= queryset.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query) |
            Q(content__icontains=query)

        ).distinct()
    paginator = Paginator(queryset, 4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)

    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    context = {
        'queryset': paginated_queryset,
        'query':query
    }

    return render(request, 'searchresults.html', context)


def get_category_count():
    queryset = blogPost.objects.values('categories__title')\
        .annotate(Count('categories'))
    return queryset


def index(request):
    featured = blogPost.objects.filter(featured=True)
    latest = blogPost.objects.order_by('-timestamp')[0:3]

    if request.method == "POST":
        email = request.POST["email"]
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()

    context = {
        'object_list': featured,
        'latest': latest

    }
    return render(request, 'index.html', context)


def blog(request):
    category_count = get_category_count()
    most_recent = blogPost.objects.order_by('-timestamp')[:3]
    post_list = blogPost.objects.all()
    paginator = Paginator(post_list, 4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)

    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
        'most_recent': most_recent,
        'category_count': category_count
    }
    return render(request, 'blog.html', context)


def post(request, id):

    category_count = get_category_count()
    most_recent = blogPost.objects.order_by('-timestamp')[0:3]
    post = get_object_or_404(blogPost, id=id)
    if not request.user.is_anonymous:
        PostView.objects.get_or_create(user=request.user, post=post)
    context = {
        'post': post,
        'most_recent': most_recent,
        'category_count': category_count
    }
    return render(request, 'post.html', context)


@login_required
def post_create(request):
    form = blogPostCreationForm(request.POST or None, request.FILES or None)
    author = get_user(request.user)
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect(reverse('post_detail', kwargs={
                'id': form.instance.id
            }))

    context = {
        'form': form
    }

    return render(request, 'create.html', context)


def post_update(request, id):
    pass

def post_delete(request, id):
    pass