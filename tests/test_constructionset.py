from app.models.energy.constructionset import ConstructionSet
from app.models.samples.energyconstructionset import construction_set
from copy import copy
from pydantic import ValidationError
import pytest


def test_construction_set():
    ConstructionSet.parse_obj(construction_set)