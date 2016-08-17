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

from laos.db import deployment_package


class DeploymentPackageModel(object):

    def list(self):
        pass

    def create(self):
        pass

    def get(self, dp_id):
        a = deployment_package.DeploymentPackage(project_id='a',
                                                 description='a',
                                                 deployment_package_url='a',
                                                 name='a',
                                                 version='a',
                                                 requirements='a', status='a')

        a.create()
        return a

    def delete(self, dp_id):
        pass
