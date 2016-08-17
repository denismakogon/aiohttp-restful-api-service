"""empty message

Revision ID: 7a2dcf8ac8bf
Revises: 
Create Date: 2016-05-18 16:24:27.886139

"""

# revision identifiers, used by Alembic.
revision = '7a2dcf8ac8bf'
down_revision = None
branch_labels = None
depends_on = None

import sqlalchemy as sa

from alembic import op


def upgrade():
    op.create_table(
        'deployment_packages',
        sa.Column('id', sa.String(), nullable=False),
        sa.Column('project_id', sa.String(), nullable=False),
        sa.Column('description', sa.String(), nullable=True),
        sa.Column('created_at', sa.String()),
        sa.Column('updated_at', sa.String()),
        sa.Column('deployment_package_url', sa.String(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('version', sa.String(), nullable=False),
        sa.Column('requirements', sa.Text(), nullable=True),
        sa.Column('status', sa.String(), nullable=False)
    )

    op.create_table(
        'lambdas',
        sa.Column('id', sa.String(), nullable=False),
        sa.Column('project_id', sa.String(), nullable=False),
        sa.Column('description', sa.String(), nullable=True),
        sa.Column('created_at', sa.String()),
        sa.Column('updated_at', sa.String()),
        sa.Column('deployment_package_url', sa.String(),
                  sa.ForeignKey('deployment_package.'
                                'deployment_package_url'),
                  nullable=False,),
        sa.Column('trigger', sa.String(),
                  sa.ForeignKey('triggers.id'),
                  nullable=False,),
    )

    op.create_table(
        'triggers',
        sa.Column('id', sa.String(), nullable=False),
        sa.Column('project_id', sa.String(), nullable=False),
        sa.Column('description', sa.String(), nullable=True),
        sa.Column('created_at', sa.String()),
        sa.Column('updated_at', sa.String()),
        sa.Column('event', sa.String(), nullable=False),
        sa.Column('lambda_id', sa.String(),
                  sa.ForeignKey('lambdas.id'),
                  nullable=False,),
        sa.UniqueConstraint('event'),
        sa.PrimaryKeyConstraint('event'),
    )


def downgrade():
    op.drop_table('lambdas')
    op.drop_table('triggers')
    op.drop_table('deployment_packages')
