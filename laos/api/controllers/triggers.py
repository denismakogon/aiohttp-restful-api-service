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

from aiohttp import web

from laos.common.base import controllers


class TriggersController(controllers.ServiceControllerBase):

    controller_name = 'triggers'

    @controllers.api_action(method='GET', route='/triggers')
    async def list(self, request, **kwargs):
        return web.Response(body=b'{}', status=200)

    @controllers.api_action(method='GET', route='/triggers/{name}')
    async def get(self, requst, **kwargs):
        return web.Response(body=b'{}', status=200)

    @controllers.api_action(method='POST', route='/triggers')
    async def create(self, request, **kwargs):
        return web.Response(body=b'{}', status=201)

    @controllers.api_action(method='DELETE', route='/triggers/{name}')
    async def delete(self, request, **kwargs):
        return web.Response(body=b'{}', status=202)
