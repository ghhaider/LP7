from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('events/', views.EventListView.as_view(), name='events'),
    path('event/<slug:slug>', views.EventDetailView.as_view(), name='events-detail'),
    path('promotions/', views.PromotionListView.as_view(), name='promotions'),
    path('promotion/<slug:slug>', views.PromotionDetailView.as_view(), name='promotions-detail'),
    path('locations', views.locations, name='locations'),
    path('location/<slug:slug>', views.LocationDetailView.as_view(), name='locations-detail'),
    path('contact', views.contact, name='contact'),
    path('pricingrawalpindi/<int:pk>', views.pricingrawalpindiDetailView.as_view(), name='packagerwp-detail'),
    path('pricingislamabad/<int:pk>', views.pricingislamabadDetailView.as_view(), name='packageisd-detail'),
    path('about/', views.aboutListView.as_view(), name='about'),
    path('packages', views.packages, name='packages'),
    path('gallery', views.gallery, name='gallery'),
    path('galleryISD/', views.GalleryISDListView.as_view(), name='galleryListISD'),
    path('galleryRWP/', views.GalleryRWPListView.as_view(), name='galleryListRWP'),
    path('BookEvent', views.BookEvent, name='BookEvent'),
    path('PackageSpace', views.PackageSpace, name='PackageSpace'),
]
