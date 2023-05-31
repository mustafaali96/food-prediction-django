from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as st
from rest_framework.permissions import IsAuthenticated
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from revoke_app.constants import CONTACT_US_TO_EMAIL
from revoke_app.serializers import ContactUsSerializer


class ContactUsAPIView(APIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = ContactUsSerializer
    email_template = ""

    def post(self, request, *args, **kwargs):
        
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            html_message = render_to_string(template_name="email_templates/contact_us.html", context=serializer.validated_data, request=request)

            email_sent = EmailMultiAlternatives(subject="Response from User", body="A response from user", from_email='developerpro12346@gmail.com', to=[request.data['email'], CONTACT_US_TO_EMAIL])
            email_sent.attach_alternative(html_message, 'text/html')
            try:
                email_sent = email_sent.send()
            except Exception:
                pass
            return Response({"detail": "Reponse submited successfully"}, status=st.HTTP_200_OK)

        return Response(serializer.errors, status=st.HTTP_400_BAD_REQUEST)