from django.shortcuts import render
from banner.models import  BannerHeader, BannerSidebar, BannerFooter
from article.models import  Post, Category, Tag
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def index(request):
    posts=Post.objects.order_by('-publish_date').filter(is_publish=True)[:4]
    banner_header= BannerHeader.objects.all()
    banner_sidebar= BannerSidebar.objects.all()
    banner_footer= BannerFooter.objects.all()


    social_category=Category.objects.get(title='សង្គម')
    social_posts=social_category.post_set.order_by('-publish_date').filter(is_publish=True)[1:5]
    social_lastest_post=social_category.post_set.order_by('-publish_date').filter(is_publish=True)[0]

    entertainment_category=Category.objects.get(title='កម្សាន្ត')
    entertainment_posts=entertainment_category.post_set.order_by('-publish_date').filter(is_publish=True)[1:5]
    entertainment_lastest_post=entertainment_category.post_set.order_by('-publish_date').filter(is_publish=True)[0]

    sport_category=Category.objects.get(title='កីឡា')
    sport_posts=sport_category.post_set.order_by('-publish_date').filter(is_publish=True)[1:5]
    sport_lastest_post=sport_category.post_set.order_by('-publish_date').filter(is_publish=True)[0]

    technology_category=Category.objects.get(title='បច្ចេកវិទ្យា')
    technology_posts=technology_category.post_set.order_by('-publish_date').filter(is_publish=True)[1:4]
    technology_lastest_post=technology_category.post_set.order_by('-publish_date').filter(is_publish=True)[0]

    health_category=Category.objects.get(title='សុខភាពនិងសម្រស់')
    health_posts=health_category.post_set.order_by('-publish_date').filter(is_publish=True)[1:4]
    health_lastest_post=health_category.post_set.order_by('-publish_date').filter(is_publish=True)[0]

    lifestyle_category=Category.objects.get(title='បែបផែនជីវិត')
    lifestyle_posts=lifestyle_category.post_set.order_by('-publish_date').filter(is_publish=True)[1:4]
    lifestyle_lastest_post=lifestyle_category.post_set.order_by('-publish_date').filter(is_publish=True)[0]
    
    context={
        'banner_header': banner_header,
        'banner_sidebar' : banner_sidebar,
        'banner_footer' : banner_footer,

        'posts' : posts,

        'social_posts':social_posts,
        'social_lastest_post':social_lastest_post,

        'entertainment_posts':entertainment_posts,
        'entertainment_lastest_post':entertainment_lastest_post,

        'sport_posts':sport_posts,
        'sport_lastest_post':sport_lastest_post,
        
        'technology_posts':technology_posts,
        'technology_lastest_post':technology_lastest_post,

        'health_posts':health_posts,
        'health_lastest_post':health_lastest_post,

        'lifestyle_posts':lifestyle_posts,
        'lifestyle_lastest_post':lifestyle_lastest_post,
    }
    return render(request, 'pages/index.html', context)



def social(request):

    banner_header= BannerHeader.objects.all()
    banner_sidebar= BannerSidebar.objects.all()
    banner_footer= BannerFooter.objects.all()
   
    category=Category.objects.get(title='សង្គម')
    posts=category.post_set.order_by('-publish_date').filter(is_publish=True)
    paginator=Paginator(posts, 8)
    page= request.GET.get('page')
    paged_posts=paginator.get_page(page)
    context={
        'banner_header': banner_header,
        'banner_sidebar' : banner_sidebar,
        'banner_footer' : banner_footer,


        'posts':paged_posts
    }
    return render(request, 'pages/social.html', context)



def entertainment(request):
    banner_header= BannerHeader.objects.all()
    banner_sidebar= BannerSidebar.objects.all()
    banner_footer= BannerFooter.objects.all()
   
    category=Category.objects.get(title='កម្សាន្ត')
    posts=category.post_set.order_by('-publish_date').filter(is_publish=True)
    paginator=Paginator(posts, 8)
    page= request.GET.get('page')
    paged_posts=paginator.get_page(page)
    context={
        'banner_header': banner_header,
        'banner_sidebar' : banner_sidebar,
        'banner_footer' : banner_footer,


        'posts':paged_posts
    }

    
    return render(request, 'pages/entertainment.html', context)


def sport(request):
    banner_header= BannerHeader.objects.all()
    banner_sidebar= BannerSidebar.objects.all()
    banner_footer= BannerFooter.objects.all()
   
    category=Category.objects.get(title='កីឡា')
    posts=category.post_set.order_by('-publish_date').filter(is_publish=True)
    paginator=Paginator(posts, 8)
    page= request.GET.get('page')
    paged_posts=paginator.get_page(page)
    context={
        'banner_header': banner_header,
        'banner_sidebar' : banner_sidebar,
        'banner_footer' : banner_footer,


        'posts':paged_posts
    }
    return render(request, 'pages/sport.html', context)


def technology(request):
    banner_header= BannerHeader.objects.all()
    banner_sidebar= BannerSidebar.objects.all()
    banner_footer= BannerFooter.objects.all()
   
    category=Category.objects.get(title='បច្ចេកវិទ្យា')
    posts=category.post_set.order_by('-publish_date').filter(is_publish=True)
    paginator=Paginator(posts, 8)
    page= request.GET.get('page')
    paged_posts=paginator.get_page(page)
    context={
        'banner_header': banner_header,
        'banner_sidebar' : banner_sidebar,
        'banner_footer' : banner_footer,


        'posts':paged_posts
    }
    return render(request, 'pages/technology.html', context)



def health(request):
    banner_header= BannerHeader.objects.all()
    banner_sidebar= BannerSidebar.objects.all()
    banner_footer= BannerFooter.objects.all()
   
    category=Category.objects.get(title='សុខភាពនិងសម្រស់')
    posts=category.post_set.order_by('-publish_date').filter(is_publish=True)
    paginator=Paginator(posts, 8)
    page= request.GET.get('page')
    paged_posts=paginator.get_page(page)
    context={
        'banner_header': banner_header,
        'banner_sidebar' : banner_sidebar,
        'banner_footer' : banner_footer,


        'posts':paged_posts
    }
    return render(request, 'pages/health.html', context)


def lifestyle(request):
    banner_header= BannerHeader.objects.all()
    banner_sidebar= BannerSidebar.objects.all()
    banner_footer= BannerFooter.objects.all()
   
    category=Category.objects.get(title='បែបផែនជីវិត')
    posts=category.post_set.order_by('-publish_date').filter(is_publish=True)
    paginator=Paginator(posts, 8)
    page= request.GET.get('page')
    paged_posts=paginator.get_page(page)
    context={
        'banner_header': banner_header,
        'banner_sidebar' : banner_sidebar,
        'banner_footer' : banner_footer,


        'posts':paged_posts
    }
    return render(request, 'pages/lifestyle.html', context)






def error_404_view(request, exception):
    return render(request, 'pages/404.html')



