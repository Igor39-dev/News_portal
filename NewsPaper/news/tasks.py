from celery import shared_task
from django.utils import timezone
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from news.models import Post, Category


@shared_task
def weekly_newsletter():
    today = timezone.now()
    last_week = today - timezone.timedelta(days=7)
    posts = Post.objects.filter(time_create__gte=last_week)

    categories = Category.objects.all()
    for category in categories:
        subscribers = category.subscribers.all()
        if not subscribers:
            continue

        posts_in_category = posts.filter(categories=category)
        if not posts_in_category.exists():
            continue

        html_content = render_to_string(
            'weekly_newsletter.html',
            {
                'category': category,
                'posts': posts_in_category,
                'link': settings.SITE_URL,
            }
        )

        msg = EmailMultiAlternatives(
            subject=f'Еженедельная рассылка — {category.name}',
            body='',
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[s.email for s in subscribers],
        )
        msg.attach_alternative(html_content, 'text/html')
        msg.send()
