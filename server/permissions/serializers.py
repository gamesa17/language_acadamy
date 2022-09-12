from rest_framework import serializers

from permissions.models import Permission


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ("key", )
