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

import sqlalchemy as sa

from sqlalchemy.ext import declarative

from laos.common.base import persistence_model


class DeploymentPackage(declarative.declarative_base(),
                        persistence_model.PersistenceModelAPI):

    __tablename__ = 'deployment_packages'

    id = sa.Column('id', sa.String(), nullable=False, primary_key=True)
    project_id = sa.Column('project_id', sa.String(), nullable=False)
    description = sa.Column('description', sa.String(), nullable=True)
    created_at = sa.Column('created_at', sa.String())
    updated_at = sa.Column('updated_at', sa.String())
    deployment_package_url = sa.Column('deployment_package_url', sa.String(), nullable=False)
    name = sa.Column('name', sa.String(), nullable=False)
    version = sa.Column('version', sa.String(), nullable=False)
    requirements = sa.Column('requirements', sa.Text(), nullable=True)
    status = sa.Column('status', sa.String(), nullable=False)
