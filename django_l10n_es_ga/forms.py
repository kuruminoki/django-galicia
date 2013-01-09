# -*- coding: utf-8 -*-
"""
ES-GA-specific Form helpers
"""

from __future__ import absolute_import, unicode_literals

from django.forms.fields import Select
from .es_ga_municipalities import MUNICIPALITY_CHOICES
from .es_ga_comarcas import COMARCA_CHOICES


class ESGAMunicipalitySelect(Select):
    """
    A Select widget that uses a list of Galician municipalities as its choices.
    """
    def __init__(self, attrs=None):
        super(ESGAMunicipalitySelect, self).__init__(attrs, choices=MUNICIPALITY_CHOICES)


class ESGAComarcaSelect(Select):
    """
    A Select widget that uses a list of Galician comarcas as its choices.
    """
    def __init__(self, attrs=None):
        super(ESGAComarcaSelect, self).__init__(attrs, choices=COMARCA_CHOICES)
