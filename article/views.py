from django.shortcuts import get_object_or_404, render
from .models import Post
from banner.models import BannerHeader, BannerSidebar, BannerFooter



def article(request, post_id):
    
    post=get_object_or_404(Post, pk=post_id)
    related_post=post.tags.similar_objects()
    banner_header= BannerHeader.objects.all()
    banner_sidebar= BannerSidebar.objects.all()
    banner_footer= BannerFooter.objects.all()
    context={
        'post': post, 
        'related_post': related_post, 

        'banner_header': banner_header,
        'banner_sidebar' : banner_sidebar,
        'banner_footer' : banner_footer,


    }
    return render(request, 'pages/article_detail.html', context)
