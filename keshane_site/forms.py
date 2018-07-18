from django.forms import ModelForm
from keshane_site.models import Subscriber


class SubscriberForm(ModelForm):
    """Defines the form for readers to subscribe to the blog"""
    class Meta:
        model = Subscriber
        fields = ["first_name", "email_address"]