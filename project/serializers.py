from rest_framework import serializers

from project.models import Project
from rest_framework.validators import ValidationError


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        read_only_fields = 'owner',

    def validate(self, data):
        start_date = self.initial_data.get('start_date')
        end_date = self.initial_data.get('end_date')
        if start_date > end_date:
            raise ValidationError({"detail": "End Date should be grater than Start Date"})
        return data
