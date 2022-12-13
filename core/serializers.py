from djoser.serializers import UserCreateSerializer as BaseUserCreateSeriazlier
from djoser.serializers import UserSerializer as BaseUserSerializer

class UserCreateSerializer(BaseUserCreateSeriazlier):
    class Meta(BaseUserCreateSeriazlier.Meta):
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name']
        
class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
