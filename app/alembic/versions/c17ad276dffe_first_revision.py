"""first revision

Revision ID: c17ad276dffe
Revises: 
Create Date: 2022-11-21 10:20:32.397492

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'c17ad276dffe'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('reset_token', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('totals',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('totals', sa.Numeric(), nullable=False),
    sa.Column('tax_totals', sa.Numeric(), nullable=False),
    sa.Column('tax_year', sa.String(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_totals_tax_year'), 'totals', ['tax_year'], unique=False)
    op.create_table('receipts',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('merchant_name', sa.String(), nullable=False),
    sa.Column('total', sa.Numeric(), nullable=False),
    sa.Column('tax', sa.Numeric(), nullable=False),
    sa.Column('merchant_address', sa.String(), nullable=False),
    sa.Column('items_services', postgresql.JSON(astext_type=sa.Text()), nullable=False),
    sa.Column('transaction_number', sa.String(), nullable=True),
    sa.Column('card_last_4', sa.String(length=4), nullable=True),
    sa.Column('link', sa.String(), nullable=True),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('time', sa.DateTime(), nullable=True),
    sa.Column('total_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['total_id'], ['totals.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_receipts_id'), 'receipts', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_receipts_id'), table_name='receipts')
    op.drop_table('receipts')
    op.drop_index(op.f('ix_totals_tax_year'), table_name='totals')
    op.drop_table('totals')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
