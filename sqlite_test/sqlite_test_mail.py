import json
import time

import requests
from sqlalchemy import create_engine, Column, Integer, String, and_, or_, inspect, MetaData, Table, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

from sqlite_test.models.BaseModel import BaseModel
from sqlite_test.models.TaskLogModel import TaskLogModel
from sqlite_test.models.VariableModel import VariableModel
from sqlite_test.utils.ModelUtil import getUUID, getCurrentTime

dbFile = r'E:\新建文件夹\test.db'


def createTaskLogModel(uuid, nCount):
    taskModel = TaskLogModel(id=uuid, time='2020-02-02 12:03:33', timestamp=1711501955.22403, cardId=uuid,
                             cardExecuteId=uuid, flowName='ddccbbaa', index=nCount, noteType=nCount % 4,
                             notes=r'主-RPA回归测试-770版本/主工作流/主流程ccbbaa')
    return taskModel


def createVariableModel(uuid, nCount):
    output = {
        "aaa": "aaaaaaaaaaaaaaaaaaaaaaaaaddaaaaaaaaaaaaaaaaaaaaccaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        "bbbbbbbb": "a", "cc": 1, "daad": 33}

    # if nCount % 5 == 0:
    variableModel = VariableModel(id=uuid, content=json.dumps(output))
    # else:
    #     variableModel = VariableModel(id=uuid, content=json.dumps({"aaaa": "bbb", "bbbbbbbb": "a", "cc": 1, "dd": 33}))
    return variableModel


def initDB():
    engine = create_engine(f'sqlite:///{dbFile}', echo=True)
    BaseModel.metadata.create_all(engine)
    with Session(engine) as session:
        nCount = 0
        while nCount < 200000:
            uuid = getUUID()
            session.add(createTaskLogModel(uuid, nCount))
            session.add(createVariableModel(uuid, nCount))
            if nCount % 5000 == 0:
                session.commit()
            nCount = nCount + 1
        session.commit()


def searchDB():
    start = getCurrentTime()
    print('-------------------------------- 1')
    engine = create_engine(f'sqlite:///{dbFile}', echo=True)
    with Session(engine) as session:
        # q = session.query(TaskLogModel).join(VariableModel,TaskLogModel.id == VariableModel.id).filter(
        #     and_(TaskLogModel.time >= '2020-02-02 12:02:33', TaskLogModel.time <= '2020-02-02 12:02:33',
        #          or_(TaskLogModel.cardId.like('%cc%'), TaskLogModel.cardName.like('%cc%'),
        #              TaskLogModel.flowName.like('%cc%'), TaskLogModel.notes.like('%cc%'),
        #              VariableModel.content.like('%cc%'))))

        # q = session.query(TaskLogModel, VariableModel).join(VariableModel, TaskLogModel.id == VariableModel.id).filter(
        #     and_(TaskLogModel.time >= '2020-02-02 12:03:33', TaskLogModel.time <= '2020-02-02 12:03:33',
        #          or_(TaskLogModel.cardId.like('%qqqq%'), TaskLogModel.cardName.like('%qqqq%'),
        #              TaskLogModel.flowName.like('%qqqq%'), TaskLogModel.notes.like('%qqqq%'),
        #              VariableModel.content.like('%dd%')))).slice(99, 200)

        # q = session.query(TaskLogModel, VariableModel).join(VariableModel, TaskLogModel.id == VariableModel.id).filter(
        #     and_(TaskLogModel.time >= '2020-02-02 12:03:33', TaskLogModel.time <= '2020-02-02 12:03:33',
        #          TaskLogModel.noteType == 0,
        #          or_(TaskLogModel.cardId.like('%qqqq%'), TaskLogModel.cardName.like('%qqqq%'),
        #              TaskLogModel.flowName.like('%qqqq%'), TaskLogModel.notes.like('%qqqq%'),
        #              VariableModel.content.like('%aaaccaaa%'))))

        # q = session.query(TaskLogModel, VariableModel).join(VariableModel, TaskLogModel.id == VariableModel.id).filter(
        #     and_(TaskLogModel.time >= '2020-02-02 12:03:33', TaskLogModel.time <= '2020-02-02 12:03:33',
        #          or_(TaskLogModel.cardId.like('%aa%'), TaskLogModel.cardName.like('%qqqq%'),
        #              TaskLogModel.flowName.like('%qqqq%'), TaskLogModel.notes.like('%qqqq%'),
        #              VariableModel.content.like('%aaaccaaa%'))))

        q = session.execute(text("select * from new_table_name where id = '5adcde50-ed6f-11ee-a63c-18c04df9d05b'")).one_or_none()
        print(q.flow_name, q.id)


        # pass
        # print(f'{result=}')
        # for r in result:
        #     print(f'{r.flow_name}')
    print(f'-------------------------------- 2  {getCurrentTime() - start}')
    url:str = ""
    headers: dict = {}
    payload: bytes = b""
    response = requests.request("GET", url, headers=headers, data=payload, timeout=1)

if __name__ == "__main__":
    # initDB()
    searchDB()
    # s = time.time()
    # engine = create_engine(f'sqlite:///{dbFile}', echo=True)

    # with Session(engine) as con:
    #     con.execute("select * from aa")
    #     con.commit()
    #
    # e = time.time()
    # print('-------------------')
    # print(e - s)
    #
    # inspect = inspect(engine)
    # has = inspect.has_table('tb_task_log')
    # # print(has)
    # a = {}
    # a['a'] = (1, 2)
    # print(a['a'][0], a['a'][1])
