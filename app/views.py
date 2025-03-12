from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .forms import BidForm, LoginForm, PlateForm


from app.models import Plate, Bid
from app.serializers import PlateSerializer, BidSerializer, UserSerializer
from .forms import RegisterForm


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # Password is already hashed in form.save()
            login(request, user)# Log the user in after registration
            if request.user.is_staff:
                return redirect('/home/plates/')
            else:
                return redirect('/home/bids')  # Send success response
        else:
            return HttpResponse({"success": False, "errors": form.errors}, status=400)  # Return errors

    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)  # Verify credentials

            if user is not None:
                login(request, user)  # Log in the user
                if user.is_staff:
                    return redirect('/home/plates/')
                else:
                    return redirect('/home/bids/')  # Redirect after login
            else:
                form.add_error(None, "Invalid username or password")  # Show error if login fails
    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect('login')

def home(request):
    plates = Plate.objects.all
    return render(request, 'home.html', {'plates': plates})

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
        plates = Plate.objects.filter(created_by=request.user).order_by('-id')
        form = PlateForm()  # Add this
        return Response({'plates': plates, 'form': form}, template_name='plates.html')

    def create(self, request, *args, **kwargs):
        form = PlateForm(request.POST)
        if form.is_valid():
            plate = form.save(commit=False)
            plate.created_by = request.user
            plate.save()
            return self.list(request)  # Re-render the page with updated plates

        plates = Plate.objects.filter(created_by=request.user).order_by('-id')
        return Response({'plates': plates, 'form': form}, template_name='plates.html')  # Show errors


class BidViewSet(viewsets.ModelViewSet):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer
    renderer_classes = (TemplateHTMLRenderer, )

    def list(self, request, *args, **kwargs):
        bids = Bid.objects.filter(user=request.user).order_by('-id')
        return Response({'bids': bids}, template_name = 'bids.html')

@login_required
def place_bid(request, plate_id):
    plate = get_object_or_404(Plate, id=plate_id)
    existing_bid = Bid.objects.filter(plate=plate, user=request.user).first()

    if existing_bid:
        return redirect('update_bid', bid_id=existing_bid.id)

    if request.method == "POST":
        form = BidForm(request.POST)
        if form.is_valid() and form.cleaned_data["amount"] > (plate.highest_bid or 0):
            bid = form.save(commit=False)
            bid.user = request.user
            bid.plate = plate
            bid.save()

            # Update the highest bid
            highest_bid = plate.bids.order_by('-amount').first()
            if highest_bid:
                plate.highest_bid = highest_bid.amount
                plate.save()

            return redirect('/home/bids/')  # Redirect to the bidding page

    else:
        form = BidForm()

    return render(request, "place_bid.html", {"form": form, "plate": plate})

@login_required
def update_bid(request, bid_id):
    bid = get_object_or_404(Bid, id=bid_id, user=request.user)
    plate = bid.plate  # Get the related plate


    if request.method == "POST":
        form = BidForm(request.POST, instance=bid)
        if form.is_valid() and form.cleaned_data["amount"] > (plate.highest_bid or 0):
            form.save()

            # Update the highest bid
            highest_bid = plate.bids.order_by('-amount').first()
            if highest_bid:
                plate.highest_bid = highest_bid.amount
                plate.save()

            return redirect('/home/bids/')  # Redirect after updating

    else:
        form = BidForm(instance=bid)

    return render(request, "update_bid.html", {"form": form, "plate": plate})

@login_required
def delete_bid(request, bid_id):
    bid = get_object_or_404(Bid, id=bid_id, user=request.user)
    plate = bid.plate  # Get the related plate

    if request.method == "POST":
        bid.delete()

        # Update highest bid after deletion
        highest_bid = plate.bids.order_by('-amount').first()
        plate.highest_bid = highest_bid.amount if highest_bid else None
        plate.save()

        return redirect('/home/bids/')  # Redirect after deleting

    return render(request, "delete_bid.html", {"bid": bid})