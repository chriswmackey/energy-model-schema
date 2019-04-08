"""Database Schemas"""
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import relationship

import datetime
import uuid
import json

from app.core.config import HOST_NAME

Base = declarative_base()

class Model(Base):
    """Pollination model schema."""
    __tablename__ = 'model'
    id = sa.Column(sa.String, primary_key=True)
    name = sa.Column(sa.String, nullable=False)
    type = sa.Column(sa.String, nullable=False)
    convert_to_meters = sa.Column(sa.Numeric, default=1.0)
    user_id = sa.Column(sa.String, nullable=False, default=False)
    created_at = sa.Column(sa.DateTime, nullable=False,
        default=datetime.datetime.utcnow())
    face_count = sa.Column(sa.Integer, nullable=False)
    faces = relationship("Face", back_populates='model', cascade='all, delete, delete-orphan')

    def __rep__(self):
        return "<Model: '{}'>".format(self.name)

    @classmethod
    def from_dict(cls, data, user):
        """Create a Model from a dictionary."""
        faces = data.faces
        model = cls(
            id=str(uuid.uuid4()),
            type=data.type.value,
            user_id=str(user.user_id),
            name=data.name,
            convert_to_meters=data.convert_to_meters,
            face_count=len(data.faces)
        )
        faces_db = [
            Face.from_dict(face, model.id, user)
            for face in faces
        ]
        model.faces = faces_db
        return model

    def to_model_out(self):
        return {
            "type": self.type,
            "id": self.id,
            "name": self.name,
            "convert_to_meters": float(self.convert_to_meters),
            "face_count": self.face_count,
            "created_at": str(self.created_at),
            "url": "{}/models/{}".format(HOST_NAME, self.id),
            "faces_url": "{}/models/{}/faces".format(HOST_NAME, self.id)
        }

class Face(Base):
    """Face Model for storing faces."""
    __tablename__ = 'face'
    id = sa.Column(sa.String, primary_key=True)
    model_id = sa.Column(sa.String, sa.ForeignKey('model.id'))
    user_id = sa.Column(sa.String, nullable=False, default=False)
    created_at = sa.Column(sa.DateTime, nullable=False,
        default=datetime.datetime.utcnow())
    # FACE, APERTURE, SHADE
    type = sa.Column(sa.String, nullable=False, default=False) 
    face = sa.Column(sa.JSON)

    model = relationship("Model", back_populates="faces")

    def __rep__(self):
        return "<Face: '{}-{}'>".format(self.model_id, self.id)

    @classmethod
    def from_dict(cls, data, model_id, user):
        return cls(
            id=str(uuid.uuid4()),
            model_id=model_id,
            user_id=str(user.user_id),
            type=data.type.value,
            face=data.json()
            )

    def to_face_out(self):
        face = json.loads(self.face)
        face['id'] = self.id
        return face