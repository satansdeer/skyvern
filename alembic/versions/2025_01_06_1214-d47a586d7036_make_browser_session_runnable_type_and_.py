"""make browser session runnable type and id nullable

Revision ID: d47a586d7036
Revises: 32e2f138f7fd
Create Date: 2025-01-06 12:14:00.216039+00:00

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd47a586d7036'
down_revision: Union[str, None] = '32e2f138f7fd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('persistent_browser_sessions', sa.Column('browser_id', sa.String(), nullable=True))
    op.alter_column('persistent_browser_sessions', 'runnable_type',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('persistent_browser_sessions', 'runnable_id',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('persistent_browser_sessions', 'runnable_id',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('persistent_browser_sessions', 'runnable_type',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.drop_column('persistent_browser_sessions', 'browser_id')
    # ### end Alembic commands ###
