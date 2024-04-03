"""
任务执行流水日志表（目标表），提取日志时生成
"""

from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, TEXT, FLOAT, VARCHAR, String

from .BaseModel import BaseModel
from sqlite_test.utils.ModelUtil import getUUID, getCurrentTime

__all__ = ['TaskLogModel']


class TaskLogModel(BaseModel):
    __tablename__ = 'tb_task_log'

    id = Column('id', String(36), primary_key=True)
    createTime = Column('create_time', FLOAT, default=getCurrentTime)
    time = Column('time', TEXT)
    timestamp = Column('timestamp', FLOAT)
    userId = Column('user_id', TEXT)
    appType = Column('app_type', Integer)
    sessionId = Column('session_id', Integer)
    pid = Column('pid', Integer)
    thread = Column('thread', TEXT)
    level = Column('level', VARCHAR(7))
    function = Column('function', TEXT)
    tag = Column('tag', TEXT)
    subTag = Column('sub_tag', TEXT)
    # 以下字段为 payload 中的字段信息
    taskId = Column('task_id', TEXT)
    orderId = Column('order_id', TEXT)
    projectName = Column('project_name', TEXT)
    flowName = Column('flow_name', TEXT)
    flowId = Column('flow_id', TEXT)
    workFlowName = Column('work_flow_name', TEXT)
    workFlowId = Column('work_flow_id', TEXT)
    cardName = Column('card_name', TEXT)
    cardId = Column('card_id', TEXT)
    cardExecuteId = Column('card_execute_id', TEXT, index=True)
    cardType = Column('card_type', Integer)
    notes = Column('notes', TEXT)
    action = Column('action', Integer)
    noteType = Column('note_type', Integer)
    inputVariable = Column('input_var', TEXT)  # json
    outputVariable = Column('output_var', TEXT)  # json
    timeCost = Column('time_cost', FLOAT, default=-1)  # 冗余字段，用于存储计算noteType为0的执行时间
    index = Column('index', Integer)  # 用来排序用

    def __repr__(self):
        return f"<TaskLogModel(id={self.id}, index={self.index}')>"
