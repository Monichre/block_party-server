"""empty message

Revision ID: 18f1d056ac5e
Revises: f226666b8429
Create Date: 2018-01-13 19:15:22.290823

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18f1d056ac5e'
down_revision = 'f226666b8429'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('songs', sa.Column('popularity', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('songs', 'popularity')
    # ### end Alembic commands ###
