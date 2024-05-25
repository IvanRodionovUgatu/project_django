from rest_framework import serializers

from core.models import Subject, Teacher


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

    def validate(self, attrs: dict):
        if attrs['count_lecture'] < 1:
            raise serializers.ValidationError('Количество лекций не может быть равно 0!')
        return attrs


class TeacherSerializer(serializers.ModelSerializer):
    fi = serializers.SerializerMethodField()

    class Meta:
        model = Teacher
        fields = '__all__'

    def get_fi(self, obj: Teacher):
        return obj.get_full_name()
