import base64
import json
import os
from collections.abc import Mapping
from contextlib import contextmanager
from copy import deepcopy
from dataclasses import dataclass, field
from enum import Enum
from glob import glob
from json import JSONEncoder, dumps, loads
from json.decoder import JSONDecodeError
from pathlib import Path
from sys import argv, stderr
from time import time
from typing import Any
from urllib.parse import urlparse

import yaml
from django.conf import ImproperlyConfigured

