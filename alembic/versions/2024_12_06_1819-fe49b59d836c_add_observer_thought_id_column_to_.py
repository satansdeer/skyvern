"""Add observer_thought_id column to artifacts table. Add user_input, observation to ObserverThoughts

Revision ID: fe49b59d836c
Revises: 4d51ed4719d5
Create Date: 2024-12-06 18:19:23.286827+00:00

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "fe49b59d836c"
down_revision: Union[str, None] = "4d51ed4719d5"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("artifacts", sa.Column("observer_thought_id", sa.String(), nullable=True))
    op.create_foreign_key(
        "artifacts_observer_thought_id_fkey",
        "artifacts",
        "observer_thoughts",
        ["observer_thought_id"],
        ["observer_thought_id"],
    )
    op.add_column("observer_thoughts", sa.Column("user_input", sa.UnicodeText(), nullable=True))
    op.add_column("observer_thoughts", sa.Column("observation", sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("observer_thoughts", "observation")
    op.drop_column("observer_thoughts", "user_input")
    op.drop_constraint("artifacts_observer_thought_id_fkey", "artifacts", type_="foreignkey")
    op.drop_column("artifacts", "observer_thought_id")
    # ### end Alembic commands ###