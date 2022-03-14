import pytest
from django.urls import reverse
from model_mommy import mommy

from cursodjango.django_assertions import assert_contains
from modulos.models import Modulo, Aula


@pytest.fixture
def modulo(db):
    return mommy.make(Modulo)


@pytest.fixture
def aulas(modulo):
    return mommy.make(Aula, 3, modulo=modulo)


@pytest.fixture
def resp(client, modulo, aulas):
    resp = client.get(reverse('modulos:detalhe', kwargs={'slug': modulo.slug}))
    return resp


def test_titulo(resp, modulo: Modulo):
    assert_contains(resp, modulo.titulo)


def test_youtube(resp, aula: Aula):
    assert_contains(resp, f'<iframe width="560" height="315" src="{{aula.youtube_link}}" title="YouTube video player" '
                          f'frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; '
                          f'gyroscope; picture-in-picture" allowfullscreen></iframe>')


def test_descricao(resp, modulo: Modulo):
    assert_contains(resp, modulo.descricao)


def test_publico(resp, modulo: Modulo):
    assert_contains(resp, modulo.publico)


def test_aulas_titulos(resp, aulas):
    for aula in aulas:
        assert_contains(resp, aula.titulo)


def test_aulas_links(resp, aulas):
    for aula in aulas:
        assert_contains(resp, aula.get_absolute_url())
