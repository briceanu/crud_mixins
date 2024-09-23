from rest_framework import serializers
from .models import Book



class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
    
 

    def validate_year_of_publish(slef,value):
        if value < 1950:
            raise serializers.ValidationError('year can not be less than 1950')
        return value