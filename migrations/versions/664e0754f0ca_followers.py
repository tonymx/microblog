"""followers

Revision ID: 664e0754f0ca
Revises: 581eeab99f48
Create Date: 2020-08-17 12:01:21.638644

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '664e0754f0ca'
down_revision = '581eeab99f48'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
