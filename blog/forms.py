from django import forms
from blog.models import Subscriber


class SubscriberForm(forms.ModelForm):
    """Defines the form for readers to subscribe to the blog"""
    class Meta:
        model = Subscriber
        fields = ["first_name", "email_address"]


class UnsubscribeForm(forms.Form):
    """Defines the form for subscribers to unsubscribe from the blog"""
    email_address = forms.EmailField()