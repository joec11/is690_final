"""initial migration

Revision ID: 6b62f34b7189
Revises: 
Create Date: 2024-04-26 20:38:55.377746

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6b62f34b7189'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_queries',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('u_query', sa.String(length=2000), nullable=False),
    sa.Column('query_timestamp', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('response_generated', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_queries')
    # ### end Alembic commands ###
