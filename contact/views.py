from rest_framework import generics, permissions
from .models import Contact
from .serializers import ContactSerializer


class ContactList(generics.ListCreateAPIView):
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Contact.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ContactDetail(generics.RetrieveAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()