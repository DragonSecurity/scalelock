#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from django.utils.autoreload import DJANGO_AUTORELOAD_ENV
from scalelock.root.setup import setup
setup()