"""user table is_active column changed from profile to user table

Revision ID: d7df1be73193
Revises: 1f5f503adde9
Create Date: 2023-09-06 19:54:38.582617

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd7df1be73193'
down_revision: Union[str, None] = '1f5f503adde9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
