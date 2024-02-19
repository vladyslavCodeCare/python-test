"""type model

Revision ID: d31c953796f4
Revises: 4a7431a49043
Create Date: 2024-01-26 16:42:09.167680

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd31c953796f4'
down_revision: Union[str, None] = '4a7431a49043'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('type_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'tasks', 'types', ['type_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tasks', type_='foreignkey')
    op.drop_column('tasks', 'type_id')
    # ### end Alembic commands ###