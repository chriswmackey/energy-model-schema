from app.models.model import Model
from copy import copy
from pydantic import ValidationError
import os
import json
import pytest
from pathlib import Path
from os import listdir


def test_model_multi_zone_single_family_house():
    root = os.path.dirname(os.path.dirname(__file__))
    target_folder = os.path.join(root, 'app', 'models', 'samples', 'json')
    file_path  = os.path.join(target_folder, 'model_multi_zone_single_family_house.json')
    Model.parse_file(file_path)

def test_model_shoe_box():
    root = os.path.dirname(os.path.dirname(__file__))
    target_folder = os.path.join(root, 'app', 'models', 'samples', 'json')
    file_path  = os.path.join(target_folder, 'model_shoe_box.json')
    Model.parse_file(file_path)

def test_model_single_zone_tiny_house():
    root = os.path.dirname(os.path.dirname(__file__))
    target_folder = os.path.join(root, 'app', 'models', 'samples', 'json')
    file_path  = os.path.join(target_folder, 'model_single_zone_tiny_house.json')
    Model.parse_file(file_path)

def test_model_multi_zone_office():
    root = os.path.dirname(os.path.dirname(__file__))
    target_folder = os.path.join(root, 'app', 'models', 'samples', 'json')
    file_path  = os.path.join(target_folder, 'model_multi_zone_office.json')
    Model.parse_file(file_path)

def test_model_single_zone_office():
    root = os.path.dirname(os.path.dirname(__file__))
    target_folder = os.path.join(root, 'app', 'models', 'samples', 'json')
    file_path  = os.path.join(target_folder, 'model_single_zone_office.json')
    Model.parse_file(file_path)