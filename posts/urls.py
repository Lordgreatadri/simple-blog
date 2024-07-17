from django.urls import path


from. import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('word-count', views.sentence, name='sentence'),
    path('counter', views.counter, name='counter'),
    path('blog', views.blog, name='blog'),
    path('post/<int:pk>', views.post, name='single-blog'),
]

