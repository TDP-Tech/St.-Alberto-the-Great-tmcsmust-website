from django.urls import path
from . import views
from .views import gradient, Michezo, Muziki, MipangoNaFedha
from .views import rozary_list, rozary_detail, rozary_create, rozary_update, rozary_delete, rozary_pdf_download
from .views import novena_list, novena_detail, novena_create, novena_update, novena_delete, novena_pdf_download
from .views import MaswaliNaMajibu_create, MaswaliNaMajibu_list, MaswaliNaMajibu_detail, MaswaliNaMajibu_update, MaswaliNaMajibu_delete

urlpatterns = [
    #################################
    path('home/', views.welcome_page, name='welcome_page'),
    path('about-us/', views.about_us, name='about-us'),
    path('contact-us/', views.contact_us, name='contact-us'),
    path('contact/success/', views.contact_success, name='contact-success'),
    
    path('add-leader/', views.leader_add, name='leader-add'),
    path('edit-leader/<int:pk>/', views.leader_edit, name='leader-edit'),
    path('delete-leader/<int:pk>/', views.leader_delete, name='leader-delete'),
    

    #################################
    path('rozaries/create/', rozary_create, name='rozary-create'),
    path('rozaries/', rozary_list, name='rozary-list'),
    path('rozaries/<int:pk>/', rozary_detail, name='rozary-detail'),
    path('rozaries/<int:pk>/update/', rozary_update, name='rozary-update'),
    path('rozaries/<int:pk>/pdf/', rozary_pdf_download, name='rozary-pdf-download'),
    path('rozaries/<int:pk>/delete/', rozary_delete, name='rozary-delete'),
    #################################
    path('novenas/create/', novena_create, name='novena-create'),
    path('novenas/', novena_list, name='novena-list'),
    path('novenas/<int:pk>/', novena_detail, name='novena-detail'),
    path('novenas/<int:pk>/update/', novena_update, name='novena-update'),
    path('novenas/<int:pk>/pdf/', novena_pdf_download, name='novena-pdf-download'),
    path('novenas/<int:pk>/delete/', novena_delete, name='novena-delete'),
    #################################
    path('gradient/', gradient, name='gradient'),
    #################################
    path('masomo-ya-Misa', views.masomoya_dominika_list, name='masomoya-dominika-list'),
    path('masomoya-dominika-create/', views.masomoya_dominika_create, name='masomoya-dominika-create'),
    path('masomoya-dominika-detail/<int:pk>/', views.masomoya_dominika_detail, name='masomoya-dominika-detail'),
    path('masomoya-dominika-update/<int:pk>/update/', views.masomoya_dominika_update, name='masomoya-dominika-update'),
    path('masomoya-dominika-delete/<int:pk>/delete/', views.masomoya_dominika_delete, name='masomoya-dominika-delete'),
    #################################
    path('maswalinamajibu-create/new/', MaswaliNaMajibu_create, name='maswalinamajibu-create'),
    path('maswalinamajibu-list', MaswaliNaMajibu_list, name='maswalinamajibu-list'),
    path('maswalinamajibu/<int:pk>/', MaswaliNaMajibu_detail, name='maswalinamajibu-detail'),
    path('maswalinamajibu/<int:pk>/edit/', MaswaliNaMajibu_update, name='maswalinamajibu-update'),
    path('maswalinamajibu/<int:pk>/delete/', MaswaliNaMajibu_delete, name='maswalinamajibu-delete'),
    #################################
    #################################
    path('michezo/', Michezo, name='michezo'),
    #################################
    path('muziki/', Muziki, name='muziki'),
    #################################
    path('mipango na fedha/', MipangoNaFedha, name='mipango-na-fedha'),
    #################################
    path('create/community/', views.community_create, name='community-create'),
    path('communities/', views.community_list, name='community-list'),
    path('jumuiya/<int:pk>/', views.community_detail, name='community-detail'),
    path('community/update/<int:pk>/', views.community_update, name='community-update'),
    path('community/delete/<int:pk>/', views.community_delete, name='community-delete'),
    #################################
    path('committee/create/', views.committee_create, name='committee-create'),
    path('committee/list/', views.committee_list, name='committee-list'),
    path('committee/<int:pk>/', views.committee_detail, name='committee-detail'),
    path('committee/<int:pk>/update/', views.committee_update, name='committee-update'),
    path('committee/<int:pk>/delete/', views.committee_delete, name='committee-delete'),
    #################################
    path('all-saints/', views.saintlife_list, name='saintlife-list'),
    path('saints/<int:pk>/', views.saintlife_detail, name='saintlife-detail'),
    path('saints/create/', views.saintlife_create, name='saintlife-create'),
    path('saints/<int:pk>/update/', views.saintlife_update, name='saintlife-update'),
    path('saints/<int:pk>/delete/', views.saintlife_delete, name='saintlife-delete'),
    path('saints/<int:pk>/pdf/', views.saintlife_pdf_download, name='saintlife-pdf-download'),
    #################################
    path('tmcs-history/', views.historia_ya_tmcs, name='historia_ya_tmcs'),
    path('imcs-history/', views.historia_ya_imcs, name='historia_ya_imcs'),
    #################################
    path('image/upload/', views.event_image_upload, name='event-image_upload'),
    path('gallery/', views.event_image_gallery, name='event-image-gallery'),
    #################################
    path('news/create', views.news_create, name='news-create'),
    path('news/lists', views.news_list, name='news-list'),
    path('news/<int:pk>/', views.news_detail, name='news-detail'),
    path('news/<int:pk>/update/', views.news_update, name='news-update'),
    path('news/<int:pk>/delete/', views.news_delete, name='news-delete'),
    #################################
    path('calenda-tawi/create', views.upload_calender_ya_tawi_pdf, name='upload-calendar-ya-tawi-tmcs-must'),
    path('calenda-tawi/list', views.calenda_ya_tawi_list, name='calenda-pdf-list'),
    #########################
    path('feedback/', views.feedback, name='feedback'),

]
