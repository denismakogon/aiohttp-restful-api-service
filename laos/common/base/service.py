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

import asyncio
import os

from aiohttp import web


class AbstractWebServer(object):

    def __init__(self, host: str = '127.0.0.1', port: int = '9999',
                 controllers: list = None, db_uri='sqlite:////laos.db',
                 event_loop: asyncio.AbstractEventLoop = None):
        self.host = host
        self.port = port
        self.controllers = controllers
        self.event_loop = event_loop
        self.service = web.Application(loop=self.event_loop,
                                       debug=os.environ.get('PYTHONASYNCIODEBUG', 0))
        self.service_handler = None
        self.server = None

    def _apply_routers(self):
        if self.controllers:
            for controller in self.controllers:
                controller(self.service)

    def shutdown(self):
        self.server.close()
        self.event_loop.run_until_complete(self.server.wait_closed())
        self.event_loop.run_until_complete(self.service_handler.finish_connections(1.0))
        self.event_loop.run_until_complete(self.service.cleanup())

    def initialize(self):
        self._apply_routers()
        web.run_app(self.service, host=self.host, port=self.port, shutdown_timeout=10)
