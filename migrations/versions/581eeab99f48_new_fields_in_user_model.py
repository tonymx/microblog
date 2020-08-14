"""new fields in user model

Revision ID: 581eeab99f48
Revises: 3c087b08171b
Create Date: 2020-08-14 00:34:47.565445

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '581eeab99f48'
down_revision = '3c087b08171b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
