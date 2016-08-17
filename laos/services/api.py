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
import click

from laos.api.controllers import deployment_packages
from laos.api.controllers import events
from laos.api.controllers import triggers
from laos.common.base import service
from laos.common.base import persistence_model


class API(service.AbstractWebServer):

    def __init__(self, host='0.0.0.0', port=10001, loop=None):
        super(API, self).__init__(
            host=host,
            port=port,
            controllers=[
                deployment_packages.DeploymentPackagesController,
                events.EventsController,
                triggers.TriggersController,
            ],
            event_loop=loop)


@click.command(name='laos-api-server')
@click.option('--host', default='0.0.0.0', help='API service bind host.')
@click.option('--port', default=10001, help='API service bind port.')
@click.option('--db-uri', default='sqlite:////tmp/laos.sqlite.db',
              help='LaOS persistence storage URI.')
def server(host, port, db_uri):
    loop = asyncio.get_event_loop()
    persistence_model.Connection(db_uri, loop=loop)
    API(host=host, port=port, loop=loop).initialize()


if __name__ == "__main__":
    server()
