import pytest  # NOQA
from django.urls import reverse


def test_hello_index(client):
    response = client.get(reverse("hello:index"))
    assert response.status_code == 200
