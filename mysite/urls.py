from . import views
from django.conf import settings
#from django.conf.urls import url
from django.urls import path
from django.conf.urls.static import static

app_name='mysite'
urlpatterns=[
    path('',views.post_list,name='post_list'),
    path('cate/<cate_slug>/',views.post_list,name='post_list_by_cate'),
    path('tag/<tag_slug>/',views.post_list,name='post_list_by_tag'),
    path('submit-comments/<id>/',views.submit_comments,name='submit_comments'),
    path('submit-messages/',views.submit_message,name='submit_messages'),
    #path('^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[0-9]+)/$',views.post_detail,name='post_detail'),
    path('<int:year>/<int:month>/<day>/<slug>/',views.post_detail,name='post_detail'),
    path('about/',views.about,name='about'),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)