from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from app.models import Plate, Bid
from app.serializers import PlateSerializer, BidSerializer, UserSerializer
from .forms import RegisterForm

def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('home/')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def home(request):
    bids = Bid.objects.order_by('-id')[:10]
    return render(request, 'home.html', {'bids': bids})
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save(password=serializer.validated_data['password'])

    def get_permissions(self):
        if self.action in ['create']:  # Allow anyone to register
            return [AllowAny()]
        return [IsAuthenticated()]

class PlateViewSet(viewsets.ModelViewSet):
    queryset = Plate.objects.all()
    serializer_class = PlateSerializer
    renderer_classes = (TemplateHTMLRenderer, )

    def list(self, request, *args, **kwargs):
        plates = Plate.objects.all()
        return Response({'plates': plates}, template_name = 'plates.html')


class BidViewSet(viewsets.ModelViewSet):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer
    renderer_classes = (TemplateHTMLRenderer, )

    def list(self, request, *args, **kwargs):
        bids = Bid.objects.all()
        return Response({'bids': bids, }, template_name = 'bids.html')


