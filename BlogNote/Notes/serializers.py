from rest_framework import serializers


from .models import model_Note


class NoteSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    slug = serializers.SlugField(max_length=250)
    body = serializers.CharField()
    publish = serializers.DateTimeField()
    created = serializers.DateTimeField()
    updated = serializers.DateTimeField()
    status = serializers.CharField()
    author_id = serializers.IntegerField()
    latitude = serializers.FloatField()
    longtitude = serializers.FloatField()
    zoom = serializers.IntegerField()

    def create(self, validated_data):
        return model_Note.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.body = validated_data.get('body', instance.body)
        instance.created = validated_data.get('created', instance.created)
        instance.updated = validated_data.get('updated', instance.updated)
        instance.status = validated_data.get('status', instance.status)
        instance.author_id = validated_data.get('author_id', instance.author_id)
        instance.latitude = validated_data.get('latitude', instance.latitude)
        instance.longtitude = validated_data.get('longtitude', instance.longtitude)
        instance.zoom = validated_data.get('zoom', instance.zoom)
        instance.save()
        return instance