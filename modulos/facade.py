from typing import List

from modulos.models import Modulo, Aula


def listar_modulos_ordenados() -> List[Modulo]:
    """
    lista módulos ordenados por titulos
    :return:
    """
    return list(Modulo.objects.order_by('order').all())


def encontrar_modulo(slug: str) -> Modulo:
    return Modulo.objects.get(slug=slug)


def listar_aulas_de_modulo_ordenadas(modulo: Modulo):
    return list(modulo.aula_set.order_by('order').all())


def encontar_aula(slug):
    return Aula.objects.get(slug=slug)