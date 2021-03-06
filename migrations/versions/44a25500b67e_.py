"""empty message

Revision ID: 44a25500b67e
Revises: 89e20b69f737
Create Date: 2016-03-03 05:35:13.937238

"""

# revision identifiers, used by Alembic.
revision = '44a25500b67e'
down_revision = '89e20b69f737'

import sqlalchemy as sa
from alembic import op


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('myprofile', sa.Column('username', sa.String(length=80), nullable=True))
    op.create_unique_constraint(None, 'myprofile', ['username'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'myprofile', type_='unique')
    op.drop_column('myprofile', 'username')
    ### end Alembic commands ###
