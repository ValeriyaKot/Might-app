from rest_framework import routers
from django.urls import path
from views.badges import BadgeView, EmployeeBadgeView, GroupBadgesViewSet
from django.conf.urls.static import static
from recognition_platform.settings import base

router = routers.SimpleRouter()
router.register('badges', BadgeView, basename='badges')
router.register('group-badges', GroupBadgesViewSet, basename='group-badges')

urlpatterns = router.urls + [
    path('employee-badges/<str:pk>/', EmployeeBadgeView.as_view(), name='employee-badges'),
]

urlpatterns += static(base.MEDIA_URL, document_root=base.MEDIA_ROOT)
