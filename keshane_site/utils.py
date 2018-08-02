import base64
from django.core.signing import Signer
from django.urls import reverse

from keshane_com import settings


def generate_unsubscribe_link(value):
    signer = Signer(salt="unsubscribe")
    token = base64.b64encode(signer.sign(value).encode("UTF-8")).decode("UTF-8")
    unsubscribe_link = settings.DOMAIN + reverse("blog_unsubscribe", args=[token])
    return unsubscribe_link
