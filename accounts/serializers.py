from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # token bilan birga keladigan ma'lumotlar
        token['username'] = user.username
        token['role'] = str(user.role)
        token['email'] = user.email

        return token
    
