"""Diet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path
from django.urls import path
from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    
 
    url(r'^student_register/', views.student, name='student_register'),
    # url(r'^adolescent_girl_registration/', views.adolescent_girl_register, name='adolescent_girl_registration'),
    url(r'^anemic_pregnant_woman_register/', views.anemic_pregnant_woman_register, name='anemic_pregnant_woman_register'),
    url(r'^anemic_lactating_mother_resgiter/', views.anemic_lactating_mother_resgiter, name='anemic_lactating_mother_resgiter'),
    
    url(r'^sam_mam_child_register/$',views.sam_mam_child_register, name='sam_mam_child_register'),
    url(r'^sam_mam_child_parents_register/$',views.SMChildParentsRegister, name='sam_mam_child_parents_register'),
    url(r'^nutri_garden_expert_register/$', views.nutri_garden_expert, name='nutri_garden_expert_register'),
    url(r'^nutri_garden_expert_bulk/', views.nutri_garden_expert_bulk, name='nutri_garden_expert_bulk'),
    url(r'^concentform/$', views.concentform, name='concentform'),
    url(r'^school_coordinator_register/', views.school_coordinator_register, name='school_coordinator_register'),
    url(r'^school_student_parent_register/', views.school_student_parent_register, name='school_student_parent_register'),
    url(r'^mukhya_sevika_register/', views.mukhya_sevika_register, name='mukhya_sevika_register'),
    url(r'^anganwadi_workers_register/', views.anganwadi_workers_register, name='anganwadi_workers_register'),

    url(r'^mentor_register/', views.mentor_registration, name='mentor_register'),
    url(r'^school_coordinator_bulk/', views.sc_bulk, name='school_coordinator_bulk'),
    # url(r'^school_bulk/', views.school_bulk, name='school_bulk'),
    url(r'^student_bulk/', views.student_bulk, name='student_bulk'),
    url(r'^anganwadi_bulk/', views.anganwadi_bulk, name='anganwadi_bulk'),
    url(r'^mukhyasevika_bulk/', views.mukhyasevika_bulk, name='mukhyasevika_bulk'),
    url(r'^mentor_bulk/', views.mentor_bulk, name='headmentor_bulk'),
    # url(r'^anemicwoman_bulk/', views.anemicwoman_bulk, name='anemicwoman_bulk'),
    url(r'^adolescent_bulk/', views.adolescent_bulk, name='adolescent_bulk'),
    url(r'^sam_mam_parent_bulk/', views.sm_parent_bulk, name='parent_bulk'),
    url(r'^school_parent_bulk/', views.school_parent_bulk, name='parent_bulk'),

    url(r'^lactatingwoman_bulk/', views.lactatingwoman_bulk, name='lactatingwoman_bulk'),
    url(r'^pregnantwoman_bulk/', views.anemicwoman_bulk, name='pregnantwoman_bulk'),

    url(r'^nutri_infotainment_survey/', views.nutri_info_views, name='nutri_infotainment_survey'),
    url(r'^nutri_socio_demographic/', views.nutri_socio_demo_views, name='nutri_socio_demographic'),
    url(r'^nutri_anthropometric_parameters/', views.nutri_anthro_para_views, name='nutri_anthropometric_parameters'),   
    url(r'^food_habits/', views.food_habits_views, name='food_habits'),   


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
