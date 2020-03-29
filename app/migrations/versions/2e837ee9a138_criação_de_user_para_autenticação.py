"""Criação de user para autenticação

Revision ID: 2e837ee9a138
Revises: ea30b2f1c392
Create Date: 2020-03-29 15:32:35.816214

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e837ee9a138'
down_revision = 'ea30b2f1c392'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('login', sa.String(length=40), nullable=True),
    sa.Column('password', sa.String(length=40), nullable=True),
    sa.PrimaryKeyConstraint('user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
