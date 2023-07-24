from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
        "id",
        "author",
        "title",
        "body",
        "created_at",
        )
        model = Post







from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post  # Add this line to specify the model associated with the serializer
        fields = (
            "id",
            "author",
            "title",
            "body",
            "created_at",
        )
