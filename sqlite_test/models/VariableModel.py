from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, TEXT, FLOAT, VARCHAR, String

from .BaseModel import BaseModel
from sqlite_test.utils.ModelUtil import getUUID, getCurrentTime

__all__ = ['VariableModel']


class VariableModel(BaseModel):
    __tablename__ = 'variable_model'

    id = Column('id', String(36), primary_key=True)
    content = Column('output', TEXT)

    def __repr__(self):
        return f"<VariableModel(id={self.id}, content={self.content}')>"
