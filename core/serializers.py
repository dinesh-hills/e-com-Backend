from djoser.serializers import UserCreateSerializer as BaseUserCreateSeriazlier

class UserCreateSerializer(BaseUserCreateSeriazlier):
    class Meta(BaseUserCreateSeriazlier.Meta):
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name']