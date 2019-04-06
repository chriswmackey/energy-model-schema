from app.models.schemas import Model, Opaque, Transparent, Plastic, Glass


def test_face_by_face_model(face_by_face_model):
    res = Model.parse_obj(face_by_face_model)


def test_opaque(opaque_material):
    res = Opaque.parse_obj(opaque_material)


def test_transparent(transparent_material):
    res = Transparent.parse_obj(transparent_material)


def test_plastic(plastic_material):
    res = Plastic.parse_obj(plastic_material)


def test_glass(glass_material):
    res = Glass.parse_obj(glass_material)
