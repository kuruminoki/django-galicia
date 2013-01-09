========================
django_localflavor_es_ga
========================

Country-specific Django helpers for Galicia (Spain).

What's in the Galicia localflavor?
==================================

* ESGAMunicipalitySelect: A ``Select`` widget that uses a list of Galician
  municipalities as its choices.

* ESGAComarcaSelect: ``A Select`` widget that uses a list of Galician comarcas
  as its choices.

See the source code for full details.

About localflavors
==================

Django's "localflavor" packages offer additional functionality for particular
countries or cultures.

For example, these might include form fields for your country's postal codes,
phone number formats or government ID numbers.

This code used to live in Django proper -- in django.contrib.localflavor -- but
was separated into standalone packages in Django 1.5 to keep the framework's
core clean.

For a full list of available localflavors, see https://github.com/django/