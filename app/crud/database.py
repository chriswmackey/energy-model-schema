from typing import List
from fastapi import HTTPException
from app.models.database import Model, Face
from app.db.database import get_db_session
from app.models.security import User


def create_model_db(data, user: User):
    """Store Model in database"""
    new = Model.from_dict(data, user)
    session = get_db_session()
    session.add(new)
    try:
        session.commit()
    except Exception as e:
        session.rollback()
        session.flush()
        print(e)
        # TODO(): Add logging
        raise HTTPException(500, 'Failed to create the model')

    return new.id


def count_models_db(user: User):
    """Return the number of models the user has created"""
    session = get_db_session()
    count = session.query(Model.id).filter_by(user_id=str(user.user_id)).count()
    session.close()
    return count


def get_models_db(page, per_page, user: User):
    """Return paginated list of models"""
    session = get_db_session()
    models = session.query(Model).filter_by(user_id=str(user.user_id)).offset(
        (page - 1) * per_page).limit(per_page)
    session.close()
    return models


def get_model_db(id, user: User):
    """Return a model"""
    session = get_db_session()
    model = session.query(Model).filter_by(
        id=str(id), user_id=str(user.user_id)
    ).first()
    session.close()
    if not model:
        raise HTTPException(404, 'Model not found.')
    return model


def delete_model_db(id, user: User):
    """Delete a model"""
    session = get_db_session()
    session.delete(get_model_db(id, user))
    try:
        session.commit()
    except:
        session.rollback()
        session.flush()
        # TODO(): Add logging
        raise HTTPException(500, 'Failed to delete the model')
    finally:
        session.close()


def count_faces_db(model_id, user: User):
    """Return the number of models the user has created"""
    session = get_db_session()
    count = session.query(Face.id).filter_by(user_id=str(user.user_id), model_id=str(model_id)).count()
    session.close()
    return count

def get_faces_db(model_id, page, per_page, user: User):
    """Return paginated list of faces"""
    face_count = count_faces_db(model_id, user)
    session = get_db_session()
    faces = session.query(Face).filter_by(user_id=str(user.user_id), model_id=str(model_id)).offset(
        (page - 1) * per_page).limit(per_page)
    session.close()
    return faces, face_count

def create_faces_db(model_id, data, user: User):
    """Create faces from a list"""
    session = get_db_session()
    faces = [Face.from_dict(data=datum, model_id=model_id, user=user) for datum in data]
    session.add(faces)
    try:
        session.commit()
    except:
        session.rollback()
        session.flush()
        # TODO(): Add logging
        raise HTTPException(500, 'Failed to create faces')

    return [face.id for face in faces]