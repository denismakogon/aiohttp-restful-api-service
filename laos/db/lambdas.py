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


class LambdaFunction(declarative.declarative_base(),
                     persistence_model.PersistenceModelAPI):

    __tablename__ = 'lambdas'

    id = sa.Column('id', sa.String(), nullable=False)
    project_id = sa.Column('project_id', sa.String(), nullable=False)
    description = sa.Column('description', sa.String(), nullable=True)
    created_at = sa.Column('created_at', sa.String())
    updated_at = sa.Column('updated_at', sa.String())
    deployment_package_url = sa.Column(
        'deployment_package_url', sa.String(),
        sa.ForeignKey('deployment_package.deployment_package_url'),
        nullable=False, )
    trigger = sa.Column('trigger', sa.String(),
                        sa.ForeignKey('triggers.id'),
                        nullable=False, )
