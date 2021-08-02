from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, CharField, RegexField
from rest_framework.validators import UniqueValidator


class AbstractUserSerializer(ModelSerializer):
    username = RegexField('^[\w.@+-]+$', max_length=150, min_length=1, allow_blank=False,
                          validators=[UniqueValidator(queryset=User.objects.all())])
    first_name = CharField(max_length=30)
    last_name = CharField(max_length=150)


class ReadOnlyUserSerializer(AbstractUserSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'is_active', 'last_login', 'is_superuser']
        read_only_fields = ['id', 'last_login', 'is_superuser']


class WriteOnlyUserSerializer(AbstractUserSerializer):
    password = RegexField('^(?=.*[A-Z])(?=.*\d).{8,}$', max_length=128, min_length=1)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password', 'is_active']
        read_only_fields = ['id', 'last_login', 'is_superuser']
