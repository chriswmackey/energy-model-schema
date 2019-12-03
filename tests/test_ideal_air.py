from app.models.energy.idealair import IdealAirSystem
from copy import copy
from pydantic import ValidationError
import pytest
import os
import json
import pytest
from pathlib import Path
from os import listdir


def test_detailed_air():
    root = os.path.dirname(os.path.dirname(__file__))
    target_folder = os.path.join(root, 'app', 'models', 'samples', 'json')
    file_path = os.path.join(
        target_folder, 'detailed_ideal_air.json')
    IdealAirSystem.parse_file(file_path)
