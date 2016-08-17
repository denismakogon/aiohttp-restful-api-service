#    Author: Denys Makogon
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import contextlib
import uuid
import datetime

from aiomysql import sa as aiosa

from sqlalchemy import orm

from laos.common import utils


class Connection(object, metaclass=utils.Singleton):

    def __init__(self, db_uri, loop=None):
        self.uri = db_uri
        self.engine = loop.run_until_complete(self.get_engine(loop=loop))
        self.loop = loop

    async def get_engine(self, loop=None):
        username, password, host, port, db_name = utils.split_db_uri(self.uri)
        return await aiosa.create_engine(host=host, port=port,
                                         user=username, password=password,
                                         db=db_name, loop=loop)

    @classmethod
    def engine_instance(cls):
        return cls._instance.engine


@contextlib.contextmanager
def session_wrapper():
    session = orm.sessionmaker(
        bind=(yield from Connection.engine_instance()))()
    yield session
    session.commit()


class PersistenceModelAPI(object):

    def __init__(self, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = str(
            datetime.datetime.now())
        for k, v in kwargs.items():
            setattr(self, k, v)

    def create(self):
        with session_wrapper() as session:
            session.add(self)

    def delete(self):
        with session_wrapper() as session:
            session.delete(self)
        del self

    def update(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
        with session_wrapper() as session:
            session.merge(self)

    @classmethod
    def find_by(cls, **kwargs):
        with session_wrapper() as session:
            return session.query(cls).filter(**kwargs).all()
