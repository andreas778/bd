from sqlalchemy import Table, Column, create_engine, insert, delete, text, select, update
from sqlalchemy.orm import relationship
from sqlalchemy import Integer, ForeignKey, String, Unicode, Numeric, Boolean, DateTime, TIMESTAMP, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref#, relation
from sqlalchemy.exc import ArgumentError
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
import json
import random
import string
import datetime
import ast

DeclarativeBase = declarative_base()
metadata = DeclarativeBase.metadata


class Freelancer(DeclarativeBase):
    __tablename__ = 'freelancer'
    
    freelancer_id = Column('freelancer_id', Integer, primary_key=True)
    name = Column('name', String(30))
    specialization = Column('specialization', String(30))


class Client(DeclarativeBase):
    __tablename__ = 'client'

    client_id = Column('client_id', Integer, primary_key=True)
    name = Column('name', String(30))
    contacts = Column('contacts', String(30))


class Project(DeclarativeBase):
    __tablename__ = "project"

    project_id = Column('project_id', Integer, primary_key=True)
    name = Column('name', String(30))
    description = Column('description', String)
    freelancer_id = Column('freelancer_id', Integer, ForeignKey("freelancer.freelancer_id"))
    client_id = Column('client_id', Integer, ForeignKey("client.client_id"))


class Task(DeclarativeBase):
    __tablename__ = "task"

    task_id = Column('task_id', Integer, primary_key=True)
    description = Column('description', String)
    state = Column('state', Boolean)
    project_id = Column('project_id', Integer, ForeignKey("project.project_id"))



def output(filename, data):
        with open(filename, 'w+') as f:
            f.writelines("%s\n" % place for place in data)


class Database:

    def __init__(self):
        try:
            self.engine = create_engine('postgresql://postgres:4545@localhost:5432/postgres')
            self.metadata = MetaData() #DeclarativeBase.metadata
            self.metadata.reflect(self.engine)
            self.base = automap_base(metadata=self.metadata)
            self.base.prepare()
            session_class = sessionmaker(bind=self.engine)

            self.session = session_class()


        except ArgumentError:
            print('Argument error')

    def create_tables(self):
        metadata.create_all(bind=self.engine)

    def delete_all(self):
        """
        It deletes all items and all lists
        """
        self.session.query(self.base.classes['client']).delete()
        self.session.query(self.base.classes['cargo']).delete()
        self.session.query(self.base.classes['department']).delete()
        self.session.query(self.base.classes['packing']).delete()
        self.session.query(self.base.classes['worker']).delete()
        self.session.query(self.base.classes['ref_worker_cargo']).delete()
        self.session.query(self.base.classes['ref_client_worker']).delete()
        self.session.commit()

    def save_all(self, objects):
        """
        It commits objects created by outer scope
        :param objects: a list of objects to save
        """
        self.session.add_all(objects)
        self.session.commit()

    def delete_request(self, table, where):
        '''
        deletes the row with condition where
        :param table: name of the table
        :param where: condition to delete
        :return:
        '''
        temp = Table(table, self.metadata, autoload=True, autoload_with=self.engine)
        query = delete(temp).where(text(str(where)))
        results = self.session.execute(query)
        results = self.session.execute(select([temp])).fetchall()
        output('output.txt', results)
        self.session.commit()

    def insert_request(self, table, condition):
        temp = Table(table, self.metadata, autoload=True, autoload_with=self.engine)
        res = eval('dict(' + condition + ')')
        query = insert(temp)
        ResultProxy = self.session.execute(query, res)
        results = self.session.execute(select([temp])).fetchall()
        output('output.txt', results)
        self.session.commit()

    def update_request(self, table, condition):
        temp = Table(table, self.metadata, autoload=True, autoload_with=self.engine)
        where, what = condition.split(',')
        res = eval('dict(' + what + ')')
        query = update(temp).values(res).where(text(where))
        results = self.session.execute(query)
        results = self.session.execute(select([temp])).fetchall()
        output('output.txt', results)
        self.session.commit()

    def requestFormat(self, comboTable, comboAction, textAction, Controller):
        Controller.gen_label.setText('')

        if comboAction == 'delete':
            try:
                self.delete_request(comboTable, textAction)
                Controller.error.setText('Done')

            except Exception as error:
                session_class = sessionmaker(bind=self.engine)
                self.session = session_class()
                Controller.error.setText(str(error))
        elif comboAction == 'insert':
            try:
                self.insert_request(comboTable, textAction)
                Controller.error.setText('Done')

            except Exception as error:
                session_class = sessionmaker(bind=self.engine)
                self.session = session_class()
                Controller.error.setText(str(error))
        elif comboAction == 'update':
            try:
                self.update_request(comboTable, textAction)
                Controller.error.setText('Done')

            except Exception as error:
                session_class = sessionmaker(bind=self.engine)
                self.session = session_class()
                Controller.error.setText(str(error))

