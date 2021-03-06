from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index$', views.index, name='index'),
    url(r'^anliall$', views.anliall, name='anliall'),
    url(r'^oushi$', views.oushi, name='oushi'),
    url(r'^katong$', views.katong, name='katong'),
    url(r'^zhongshi$', views.zhongshi, name='zhongshi'),
    url(r'^xiandai$', views.xiandai, name='xiandai'),
    url(r'^jianyue$', views.jianyue, name='jianyue'),
    url(r'^about$', views.about, name='about'),
    url(r'^about1$', views.about1, name='about1'),
    url(r'^about2$', views.about2, name='about2'),
    url(r'^about3$', views.about3, name='about3'),
    url(r'^about4$', views.about4, name='about4'),
    url(r'^news$', views.news, name='news'),
    url(r'^news1$', views.news1, name='news1'),
    url(r'^news2$', views.news2, name='news2'),
    url(r'^news3$', views.news3, name='news3'),
    url(r'^jiameng$', views.jiameng, name='jiameng'),
    url(r'^cont$', views.cont, name='cont'),
]