from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail

class EmailAPIView(APIView):
    def post(self, request):
        try:
            to_email = "nanda_4fernanda@hotmail.com"
            subject = "Prueba"
            message = request.data.get('message')
            send_mail(subject, message, None, [to_email])
            return Response({'message': 'enviado'})
        except Exception as e:
            error_message = str(e)
            return Response({'error_message': error_message})