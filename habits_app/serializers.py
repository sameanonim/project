import datetime

from rest_framework import serializers

from habits_app.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Habit
        fields = ('id', 'user', 'place', 'time', 'action',
                'is_pleasurable', 'linked_habit', 'frequency',
                'reward', 'execution_time', 'is_public')
        read_only_fields = ('id',)

    def validate(self, data):
        # Проверяем, что указаны только допустимые комбинации полей
        self._validate_fields_combination(data)
        # Проверяем, что значения полей входят в допустимые диапазоны
        self._validate_fields_values(data)
        return data

    def _validate_fields_combination(self, data):
        if data.get('linked_habit') and data.get('reward'):
            raise serializers.ValidationError("Нельзя одновременно указывать связанную привычку и вознаграждение")
        if data.get('is_pleasurable') and (data.get('reward') or data.get('linked_habit')):
            raise serializers.ValidationError("У приятной привычки не может быть вознаграждения или связанной привычки")

    def _validate_fields_values(self, data):
        if data.get('execution_time') is not None and data.get('execution_time') > datetime.time(hour=0, minute=2, second=0):
            raise serializers.ValidationError("Время выполнения не может превышать 120 секунд")
        if data.get('linked_habit') and not data.get('linked_habit').is_pleasurable:
            raise serializers.ValidationError("В связанные привычки можно добавлять только с признаком приятной")
        if data.get('frequency') is not None and data.get('frequency') < 7:
            raise serializers.ValidationError("Периодичность не может быть реже, чем один раз в 7 дней")