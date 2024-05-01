from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from django.views.generic import ListView

class PostListView(ListView):
    """
    Alternative post list view
    """
    queryset= Post.published.all()
    context_object_name = 'posts'
    paginate_by

def post_list(request):
    post_list = Post.published.all()
    paginator= Paginator(post_list, 3)
    """ Vous récupérez le numéro de la page demandée à partir de la requête GET 
    avec request.GET.get('page', 1). 
    Si le paramètre 'page' n'est pas présent dans la requête, 
    vous utilisez 1 comme valeur par défaut, 
    ce qui signifie que vous chargez la première page de résultats."""

    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
# If page_number is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page_number is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/post/list.html', {'posts' : posts})


def post_detail(request,year, month, day, post):

    post = get_object_or_404(Post,status=Post.Status.PUBLISHED, slug=post,publish__year=year,publish__month=month,publish__day=day)
    
    return render(request,'blog/post/detail.html',{'post' : post})