from rest_framework.decorators import action
from rest_framework.response import Response
from apps.badges.models import Badge, EmployeeBadge, GroupBadges
from serializers.badges import BadgeSerializer, EmployeeBadgeSerializer, GroupBadgesSerializer, \
    ShortGroupBadgesSerializer, EmployeeBadgeListSerializer
from rest_framework import viewsets, status, generics
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from apps.badges.permissions import IsManagerOrReadOnly


class BadgeView(viewsets.ModelViewSet):
    queryset = Badge.objects.all()
    serializer_class = BadgeSerializer
    permission_classes = [IsManagerOrReadOnly]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ['group']
    search_fields = ['title']


class EmployeeBadgeView(generics.ListCreateAPIView):
    serializer_class = EmployeeBadgeListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['badge__title']

    def get_queryset(self):
        pk = self.kwargs['pk']
        return EmployeeBadge.objects. \
            filter(employee_guid=pk).select_related('badge')

    def create(self, request, pk):
        serializer = EmployeeBadgeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(employee_guid=pk, giver_guid=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GroupBadgesViewSet(viewsets.ModelViewSet):
    permission_classes = [IsManagerOrReadOnly]
    serializer_class = GroupBadgesSerializer
    queryset = GroupBadges.objects.prefetch_related('badges').all()
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ['is_manager']

    @action(detail=False, methods=['get'])
    def retrieve_short(self, request):
        serializer = ShortGroupBadgesSerializer(self.queryset, many=True)
        return Response(data=serializer.data)
