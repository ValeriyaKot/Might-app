from rest_framework import serializers
from apps.badges.models import Badge, EmployeeBadge, GroupBadges


class BadgeSerializer(serializers.ModelSerializer):
    group = serializers.PrimaryKeyRelatedField(
        queryset=GroupBadges.objects.all())

    class Meta:
        model = Badge
        fields = '__all__'


class EmployeeBadgeSerializer(serializers.ModelSerializer):
    giver_guid = serializers.CharField(max_length=40, read_only=True)

    class Meta:
        model = EmployeeBadge
        exclude = ['employee_guid']


class GroupBadgesSerializer(serializers.ModelSerializer):
    badges = BadgeSerializer(read_only=True, many=True)

    class Meta:
        model = GroupBadges
        fields = ['id', 'name', 'description', 'icon', 'is_manager', 'badges']


class ShortGroupBadgesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupBadges
        fields = ['id', 'name']


class EmployeeBadgeListSerializer(serializers.ModelSerializer):
    badge = BadgeSerializer(read_only=False)
    giver_guid = serializers.CharField(max_length=40, read_only=True)

    class Meta:
        model = EmployeeBadge
        exclude = ['employee_guid']

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        if ret['isAnonymous']:
            ret.pop('giver_guid')
        return ret
