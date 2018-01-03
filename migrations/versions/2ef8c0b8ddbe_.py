"""empty message

Revision ID: 2ef8c0b8ddbe
Revises: 97cafad2a91c
Create Date: 2018-01-03 05:56:39.505854

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ef8c0b8ddbe'
down_revision = '97cafad2a91c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('followers', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'followers')
    # ### end Alembic commands ###
