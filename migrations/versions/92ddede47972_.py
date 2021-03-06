"""empty message

Revision ID: 92ddede47972
Revises: 2cf7de52d9de
Create Date: 2018-01-13 18:51:31.047662

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92ddede47972'
down_revision = '2cf7de52d9de'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('artists', sa.Column('spotify_id', sa.Integer(), nullable=True))
    op.add_column('songs', sa.Column('duration', sa.Integer(), nullable=True))
    op.add_column('songs', sa.Column('played_at', sa.DateTime(), nullable=True))
    op.add_column('songs', sa.Column('song_id', sa.Integer(), nullable=True))
    op.add_column('songs', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'songs', 'songs', ['song_id'], ['id'])
    op.create_foreign_key(None, 'songs', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'songs', type_='foreignkey')
    op.drop_constraint(None, 'songs', type_='foreignkey')
    op.drop_column('songs', 'user_id')
    op.drop_column('songs', 'song_id')
    op.drop_column('songs', 'played_at')
    op.drop_column('songs', 'duration')
    op.drop_column('artists', 'spotify_id')
    # ### end Alembic commands ###
