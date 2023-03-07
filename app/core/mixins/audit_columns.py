import datetime

from sqlalchemy.ext.declarative import declared_attr

from flask import request

# from ...utils.timezone_helpers import get_formatted_local_time
# from app.constants import constants

from app.database.base import db


class AuditColumnsMixin:
    @declared_attr
    def created_by(self):
        return db.Column(
            db.String(20), nullable=False, default="system", server_default="system"
        )

    @declared_attr
    def created_at(self):
        return db.Column(
            db.DateTime,
            nullable=False,
            default=datetime.datetime.utcnow,
            server_default=db.text("NOW()"),
        )

    @declared_attr
    def updated_by(self):
        return db.Column(
            db.String(20), nullable=False, default="system", server_default="system"
        )

    @declared_attr
    def updated_at(self):
        return db.Column(
            db.DateTime,
            nullable=False,
            default=datetime.datetime.utcnow,
            server_default=db.text("NOW()"),
            onupdate=datetime.datetime.utcnow,
            server_onupdate=db.text("NOW()"),
        )
    
