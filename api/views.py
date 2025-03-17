# api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import ContentUploadSerializer, MagazineContentSerializer
from .models import ContentUpload,MagazineContent 
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import AllowAny
from rest_framework.serializers import ModelSerializer
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.conf import settings

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'message': 'This is a protected view accessible only with a valid token.'})

class ContentUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, format=None):
        section = request.query_params.get('section', None)
        if section:
            uploads = ContentUpload.objects.filter(section=section)
        else:
            uploads = ContentUpload.objects.all()
        serializer = ContentUploadSerializer(uploads, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request, format=None):
        serializer = ContentUploadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Content uploaded successfully!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MagazineUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, format=None):
        serializer = MagazineContentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Magazine content uploaded successfully!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class MagazineListView(APIView):
    def get(self, request, format=None):
        magazines = MagazineContent.objects.all()
        serializer = MagazineContentSerializer(magazines, many=True , context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserSignupSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

class SignupView(APIView):
    permission_classes = [AllowAny]  # Allow unauthenticated users to sign up

    def post(self, request, format=None):
        serializer = UserSignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Signup successful.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class SendEmailView(APIView):
    def post(self, request, format=None):
        data = request.data
        name = data.get('name')
        email = data.get('email')
        subject = data.get('subject')
        message = data.get('message')

        # Validate required fields
        if not name or not email or not subject or not message:
            return Response({'error': 'All fields are required.'}, status=status.HTTP_400_BAD_REQUEST)

        # Construct the full message
        full_message = f"Message from {name} ({email}):\n\n{message}"
        try:
            send_mail(
                subject=subject,
                message=full_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_EMAIL],
                fail_silently=False,
            )
            return Response({'message': 'Email sent successfully.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)    


class DeleteContentView(APIView):
    def delete(self, request, pk, format=None):
        try:
            content = ContentUpload.objects.get(pk=pk)
        except ContentUpload.DoesNotExist:
            return Response({'error': 'Content not found.'}, status=status.HTTP_404_NOT_FOUND)  
        
        content.delete()
        return Response({'Content deleted successfully'}, status=status.HTTP_200_OK)

class DeleteMagazineView(APIView):
    def delete(self, request, pk, format=None ):
        try:
            magazine = MagazineContent.objects.get(pk=pk)
        except MagazineContent.DoesNotExist:
            return Response({'error': 'Magazine content not found.'}, status=status.HTTP_404_NOT_FOUND)
        
        magazine.delete()
        return Response({'message': 'Magazine content deleted successfully.'}, status=status.HTTP_200_OK)



