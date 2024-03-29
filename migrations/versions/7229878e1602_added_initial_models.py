"""Added Initial Models

Revision ID: 7229878e1602
Revises: 
Create Date: 2024-01-05 19:24:47.131632

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7229878e1602'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('is_deleted', sa.Boolean(), server_default='f', nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('first_name', sa.String(length=25), nullable=False),
    sa.Column('last_name', sa.String(length=25), nullable=False),
    sa.Column('password', sa.String(length=256), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('date_joined', sa.DateTime(timezone=True), nullable=True),
    sa.Column('date_of_leaving', sa.DateTime(timezone=True), nullable=True),
    sa.Column('last_login_at', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_locations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('is_deleted', sa.Boolean(), server_default='f', nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('location_name', sa.TEXT(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_rate_limits',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('is_deleted', sa.Boolean(), server_default='f', nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('requested_date', sa.Date(), nullable=False),
    sa.Column('api_hit_count', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_rate_limits')
    op.drop_table('user_locations')
    op.drop_table('users')
    # ### end Alembic commands ###
