from app.models.energy.idealair import IdealAirSystem
import os

# target folder where all of the samples live
root = os.path.dirname(os.path.dirname(__file__))
target_folder = os.path.join(root, 'app', 'models', 'samples')


def test_detailed_air():
    file_path = os.path.join(target_folder, 'ideal_air_detailed.json')
    IdealAirSystem.parse_file(file_path)
