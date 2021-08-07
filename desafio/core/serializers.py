from rest_framework import serializers
from django.db.transaction import atomic
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import gettext_lazy as _

from .models import State, City


class StateSerializer(serializers.ModelSerializer):

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

        return super().create(copy_validated_data)

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

        return super().update(instance, copy_validated_data)
