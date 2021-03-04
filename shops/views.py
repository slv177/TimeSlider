from django.shortcuts import render
from django.views import generic
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from .models import Shop, Link, Link5
from django.views.generic.base import TemplateView
from shapely.geometry import LineString as ShLineString, mapping
from .forms import ContactForm
import json
from django.http import JsonResponse
from django.core.serializers import serialize
from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User



longitude = 17.166573
latitude = 48.172558

user_location = Point(longitude, latitude, srid=4326)

class Home(generic.ListView):
    model = Shop
    context_object_name = 'shops'
    queryset = Shop.objects.annotate(distance=Distance('location', user_location)).order_by('distance')[0:6]
    template_name = 'shops/index.html'


class MapView(TemplateView):
    template_name = "shops/map.html"

    def get_context_data(self, **kwargs):
        """Return the view context data."""
        context = super().get_context_data(**kwargs)
        context["points"] = json.loads(serialize("geojson", Shop.objects.all()))
        print(context)
        return context

def contactPage(request):
    form = ContactForm()
    return render(request, "shops/contact.html", {"contactForm": form})

def postContact(request):
    if request.method == "POST" and request.is_ajax():
        form = ContactForm(request.POST)
        form.save()
        return JsonResponse({"success":True}, status=200)
    return JsonResponse({"success":False}, status=400)

def userPanel(request):
    usernames = User.objects.all().values("username")
    return render(request, "shops/user.html", {"usernames": usernames})

def getUserInfo(request):
    if request.method == "GET" and request.is_ajax():
        username = request.GET.get("username")
        try:
            user = User.objects.get(username = username)
        except:
            return JsonResponse({"success":False}, status=400)
        user_info = {
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "is_active": user.is_active,
            "joined": user.date_joined
        }
        return JsonResponse({"user_info":user_info}, status=200)
    return JsonResponse({"success":False}, status=400)


