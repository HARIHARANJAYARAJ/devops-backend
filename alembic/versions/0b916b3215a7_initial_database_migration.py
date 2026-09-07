"""Initial database migration

Revision ID: 0b916b3215a7
Revises:
Create Date: 2026-08-31 13:47:08.041086
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "0b916b3215a7"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "students",

        sa.Column(
            "id",
            sa.Integer(),
            primary_key=True,
            nullable=False
        ),

        sa.Column(
            "full_name",
            sa.String(length=100),
            nullable=False
        ),

        sa.Column(
            "roll_number",
            sa.String(length=50),
            nullable=False
        ),

        sa.Column(
            "email",
            sa.String(length=100),
            nullable=False
        ),

        sa.Column(
            "phone",
            sa.String(length=20),
            nullable=False
        ),

        sa.Column(
            "date_of_birth",
            sa.Date(),
            nullable=True
        ),

        sa.Column(
            "department",
            sa.String(length=100),
            nullable=False
        ),

        sa.Column(
            "year",
            sa.Integer(),
            nullable=False
        ),

        sa.Column(
            "address",
            sa.String(length=255),
            nullable=True
        ),

        sa.Column(
            "city",
            sa.String(length=100),
            nullable=True
        ),

        sa.Column(
            "nativeplace",
            sa.String(length=100),
            nullable=True
        ),

        sa.Column(
            "tenth_mark",
            sa.Integer(),
            nullable=True
        ),

        sa.Column(
            "twelfth_mark",
            sa.Integer(),
            nullable=True
        ),

        sa.UniqueConstraint(
            "email",
            name="uq_students_email"
        ),

        sa.UniqueConstraint(
            "roll_number",
            name="uq_students_roll_number"
        ),
    )


def downgrade() -> None:
    op.drop_table("students")