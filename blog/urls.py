from django.urls import path
from .views import HomeView, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('blog/', PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('new/', PostCreateView.as_view(), name='post_new'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/delete/', PostDeleteView.as_view(), name='post_delete'),
]
