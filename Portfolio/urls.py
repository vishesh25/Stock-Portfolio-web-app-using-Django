from django.urls import path
from . import views

urlpatterns = [
    path('home', views.HomeView, name='portfolio.home'),
    path('add', views.CreateInterfaceView.as_view(), name='portfolio.add'),
    path('<int:pk>/edit', views.UpdateInterfaceView.as_view(), name='portfolio.edit'),
    path('<int:pk>/delete', views.DeleteInterfaceView.as_view(), name='portfolio.delete'),
    path('my_details', views.StockListView.as_view(), name='portfolio.view'),
    path('request_mail', views.SendMail, name='portfolio.request_mail')
]
