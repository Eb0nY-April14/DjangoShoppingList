from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from shoppinglist import views
from shoppinglist.views import DeleteView, CustomLoginView, RegisterView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('admin/', admin.site.urls),
    path('', views.get_shopping_list, name='get_shopping_list'),
    path('add', views.add_item, name='add_item'),
    path('edit/<item_id>', views.edit_item, name='edit_item'),
    path(
        'shoppinglistitem-delete/<int:pk>/',
        DeleteView.as_view(),
        name='shoppinglistitem-delete'
        ),
    path('delete_list', views.delete_list, name='delete_list'),
    path('bought/<item_id>', views.bought_item, name='bought_item'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
