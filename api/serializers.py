from rest_framework import serializers
from .models import ContentUpload, MagazineContent

class ContentUploadSerializer(serializers.ModelSerializer):
    # file = serializers.SerializerMethodField()
    file = serializers.FileField(write_only=True)
    # …but expose it back as a URL in “file_url”
    file_url = serializers.SerializerMethodField(read_only=True)
    

    class Meta:
        model = ContentUpload
        fields = '__all__'

    def get_file_url(self, obj):
        request = self.context.get('request')
        if obj.file and request:
            return request.build_absolute_uri(obj.file.url)
        return None


class MagazineContentSerializer(serializers.ModelSerializer):
    cover_image = serializers.ImageField(write_only=True)

    cover_image_url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = MagazineContent
        fields = '__all__'


    def get_cover_image_url(self, obj):
            """Build an absolute URL to the image for read operations."""
            request = self.context.get('request')
            if obj.cover_image and request:
                return request.build_absolute_uri(obj.cover_image.url)
            return None
        
    # def get_cover_image(self, obj):
    #     request = self.context.get('request')
    #     if obj.cover_image and request:
    #         return request.build_absolute_uri(obj.cover_image.url)
    #     return None

