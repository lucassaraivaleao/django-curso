import pytest
from django.urls import reverse

from cursodjango.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('aperitivos:video', args=('motivacao',)))

def test_status_code(resp):
    assert resp.status_code == 200

def test_titulo_video(resp):
    assert_contains(resp, '<h1>Video Aperitivo: Motivacional</h1>')

def test_conteudo_video(resp):
    assert_contains(resp, '<iframe width="560" height="315" src="https://www.youtube.com/embed/JybIt0wUqi4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>')

