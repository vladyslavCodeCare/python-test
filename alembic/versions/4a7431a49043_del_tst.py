"""del tst

Revision ID: 4a7431a49043
Revises: 1e4fea11df4a
Create Date: 2024-01-20 15:47:01.533062

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4a7431a49043'
down_revision: Union[str, None] = '1e4fea11df4a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_tasks_test', table_name='tasks')
    op.drop_column('tasks', 'test')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('test', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.create_index('ix_tasks_test', 'tasks', ['test'], unique=False)
    # ### end Alembic commands ###