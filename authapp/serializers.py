from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, CharField, RegexField
from rest_framework.validators import UniqueValidator


class UserSerializer(ModelSerializer):
    username = RegexField('^[\w.@+-]+$', max_length=150, min_length=1, allow_blank=False,
                          validators=[UniqueValidator(queryset=User.objects.all(),
                                                      message="Already taken.")])
    first_name = CharField(max_length=30)
    last_name = CharField(max_length=150)
    password = RegexField('^(?=.*[A-Z])(?=.*\d).{8,}$', max_length=128, min_length=1, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'password', 'is_active', 'last_login', 'is_superuser')

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        try:
            user.set_password(validated_data['password'])
            user.save()
        except KeyError:
            pass
        return user
