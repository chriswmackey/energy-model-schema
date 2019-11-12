from app.models.energy.simulationparameter import SimulationParameter
from copy import copy
from pydantic import ValidationError
import os
import json
import pytest
from pathlib import Path
from os import listdir

def test_detailed_simulation_par():
    root = os.path.dirname(os.path.dirname(__file__))
    target_folder = os.path.join(root, 'app', 'models', 'samples', 'json')
    file_path = os.path.join(
        target_folder, 'detailed_simulatiion_par.json')
    SimulationParameter.parse_file(file_path)


def test_simple_simulatiion_par():
    root = os.path.dirname(os.path.dirname(__file__))
    target_folder = os.path.join(root, 'app', 'models', 'samples', 'json')
    file_path = os.path.join(
        target_folder, 'simple_simulatiion_par.json')
    SimulationParameter.parse_file(file_path)