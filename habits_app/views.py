from rest_framework import generics

from habits_app.models import Habit
from habits_app.pagination import HabitPagination
from habits_app.serializers import HabitSerializer
from habits_app.tasks import send_habit_reminders


class HabitListView(generics.ListCreateAPIView):
    serializer_class = HabitSerializer
    pagination_class = HabitPagination
    queryset = Habit.objects.all()

    def get_queryset(self):
        if self.queryset is None:
            self.queryset = Habit.objects.filter(user=self.request.user)
        return self.queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        send_habit_reminders.delay()


class HabitDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class PublicHabitListView(generics.ListAPIView):
    queryset = Habit.objects.filter(is_public=True)
    serializer_class = HabitSerializer
    pagination_class = HabitPagination
