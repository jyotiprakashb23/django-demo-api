from rest_framework import serializers
from .models import Recipe, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']
        read_only_fields = ['id']


class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for Recipe model."""

    tags = TagSerializer(many=True, required=False)

    class Meta:
        model = Recipe
        fields = [
            'id','title','description','ingredients','instructions','tags','created_at','updated_at',
        ]
        read_only_fields = ['id']

    def create(self, validated_data):
        tags_data = validated_data.pop('tags', [])
        recipe = Recipe.objects.create(**validated_data)

        user = self.context['request'].user

        for tag_data in tags_data:
            tag, created = Tag.objects.get_or_create(
                name=tag_data['name'],
                user=user
            )
            recipe.tags.add(tag)

        return recipe
    
    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags', None)

        if tags_data is not None:
            instance.tags.clear()
            user = self.context['request'].user
            for tag_data in tags_data:
                tag, created = Tag.objects.get_or_create(
                    name=tag_data['name'],
                    user=user
                )
                instance.tags.add(tag)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance

