import os
from collections import OrderedDict

from django.apps import apps
from django.contrib.staticfiles.finders import get_finders
from django.contrib.staticfiles.storage import staticfiles_storage
from django.core.files.storage import FileSystemStorage
from django.core.management.base import BaseCommand, CommandError
from django.core.management.color import no_style
from django.utils.functional import cached_property
from django_brfied.django_brfied.models import UnidadeFederativa, Municipio
from ...migrations import UNIDADE_FEDERATIVA_ROWS, MUNICIPIO_ROWS


class Command(BaseCommand):
    help = "Importa as UFs e os Municípios para a base"
    # requires_system_checks = False

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.ignore_patterns = []
    #
    # def add_arguments(self, parser):
    #     parser.add_argument(
    #         '--no-default-ignore', action='store_false', dest='use_default_ignore_patterns',
    #         help="Don't ignore the common private glob-style patterns (defaults to 'CVS', '.*' and '*~').",
    #     )
    #
    # def set_options(self, **options):
    #     """
    #     Set instance variables based on an options dict
    #     """
    #     if options['use_default_ignore_patterns']:
    #         ignore_patterns += apps.get_app_config('staticfiles').ignore_patterns

    def handle(self, **options):
        print('Importando UF')
        for uf in UNIDADE_FEDERATIVA_ROWS:
            UnidadeFederativa.objects.\
                update_or_create(sigla=uf[0], defaults={'nome': uf[1], 'codigo': uf[2], 'regiao': uf[3]})
        print('UF importadas\n')

        print('Importando municípios')
        i = 1
        q = len(MUNICIPIO_ROWS)
        for m in MUNICIPIO_ROWS:
            if i%500 == 0:
                print('\tImportados %3.2f%%' % ((i / q) * 100))
            Municipio.objects.update_or_create(codigo=m[0], defaults={'nome': m[1], 'uf_id': m[2]})
            i += 1
        print('Municípios importados')
