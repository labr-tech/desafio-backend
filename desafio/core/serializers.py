from rest_framework import serializers
from django.db.transaction import atomic
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from rest_framework.validators import UniqueValidator

from .models import State, City


class StateSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField()
    code = serializers.CharField(
        max_length=2,
        validators=[UniqueValidator(queryset=State.objects.all())]
    )

    class Meta:
        model = State
        fields = ('id', 'code', 'name')


class CitySerializer(serializers.ModelSerializer):
    state = serializers.CharField(max_length=2)

    class Meta:
        model = City
        fields = '__all__'

    @atomic
    def create(self, validated_data):
        state_code = validated_data.pop('state')
        copy_validated_data = validated_data.copy()

        try:
            state = State.objects.get(code=state_code)
        except ObjectDoesNotExist:
            raise serializers.ValidationError(
                _('Estado não localizado ' + state_code)
            )

        copy_validated_data['state'] = state
        copy_validated_data['slug'] = slugify(validated_data['name'])

        try:
            return super().create(copy_validated_data)
        except ValidationError:
            raise serializers.ValidationError(
                _(
                    'Registro já existente. Estado: ' + self.data['state'] +
                    ', Cidade: ' + self.data['name']
                )
            )

    @atomic
    def update(self, instance, validated_data):
        state_code = validated_data.pop('state')
        copy_validated_data = validated_data.copy()

        try:
            state = State.objects.get(code=state_code)
        except ObjectDoesNotExist:
            raise serializers.ValidationError(
                _('Estado não localizado ' + state_code)
            )

        copy_validated_data['state'] = state
        copy_validated_data['slug'] = slugify(validated_data['name'])

        return super().update(instance, copy_validated_data)
