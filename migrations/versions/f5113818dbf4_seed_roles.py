"""empty message

Revision ID: f5113818dbf4
Revises: 2e8df848f6cf
Create Date: 2018-08-09 14:55:41.204721

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from model import sa_role

revision = 'f5113818dbf4'
down_revision = '2e8df848f6cf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.bulk_insert(sa_role,
        [
            {'id': 1, 'name': 'admin'},
            {'id': 2, 'name': 'user'},
        ]
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute('TRUNCATE roles CASCADE ;')
    # ### end Alembic commands ###
