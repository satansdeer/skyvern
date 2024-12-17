"""introduce persistent browser sessions

Revision ID: 55cabeeb1590
Revises: 411dd89f3df9
Create Date: 2024-12-17 17:23:53.236841+00:00

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "55cabeeb1590"
down_revision: Union[str, None] = "411dd89f3df9"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "persistent_browser_sessions",
        sa.Column("persistent_browser_session_id", sa.String(), nullable=False),
        sa.Column("organization_id", sa.String(), nullable=False),
        sa.Column("runnable_type", sa.String(), nullable=False),
        sa.Column("runnable_id", sa.String(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("modified_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(
            ["organization_id"],
            ["organizations.organization_id"],
        ),
        sa.PrimaryKeyConstraint("persistent_browser_session_id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("persistent_browser_sessions")
    # ### end Alembic commands ###
