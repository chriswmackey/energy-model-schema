"""initial model and faces tables

Revision ID: 75f6362b514b
Revises: 
Create Date: 2019-04-06 22:03:09.440134

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '75f6362b514b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('model',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('type', sa.String(), nullable=False),
    sa.Column('convert_to_meters', sa.Numeric(), nullable=True),
    sa.Column('user_id', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('face_count', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('face',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('model_id', sa.String(), nullable=True),
    sa.Column('user_id', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('type', sa.String(), nullable=False),
    sa.Column('face', sa.JSON(), nullable=True),
    sa.ForeignKeyConstraint(['model_id'], ['model.id'], ),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('face')
    op.drop_table('model')
