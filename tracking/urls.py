from django.urls import path

from tracking.views import (
    dashboard,
    visitor_overview,
    visitor_detail,
    visitor_page_detail,
    visitor_pageview_detail,
    page_overview,
    page_detail,
)

urlpatterns = [
    path('', dashboard, name='tracking-dashboard'),
    path('visitors/<user_id>)/page/', visitor_page_detail, name='tracking-visitor-page-detail'),
    path('visitors/<user_id>)/pageview/<pageview_id>/', visitor_pageview_detail, name='tracking-pageview-detail'),
    path('visitors/<user_id>)/', visitor_overview, name='tracking-visitor-overview'),
    path('visits/<visit_id>/', visitor_detail, name='tracking-visitor-detail'),
    path('pages/', page_overview, name='tracking-page-overview'),
    path('page/', page_detail, name='tracking-page-detail'),
]
