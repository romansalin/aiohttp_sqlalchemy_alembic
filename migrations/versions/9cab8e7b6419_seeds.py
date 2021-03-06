"""seeds

Revision ID: 9cab8e7b6419
Revises: aed52717ac26
Create Date: 2018-12-02 16:28:03.602945

"""
from alembic import op

# revision identifiers, used by Alembic.
from models.chat import sa_chat

revision = '9cab8e7b6419'
down_revision = 'aed52717ac26'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.bulk_insert(sa_chat, [{}])
    op.execute("""
    INSERT INTO "public"."chats_permission" ("id", "chat_id", "user_id", "permission", "created_at", "updated_at", "chat_image", "chat_name")
    VALUES (DEFAULT, 1, NULL, 'user', '2018-10-18 17:39:26.026000', '2018-10-18 17:39:27.866000', '/media/avatars/default_group.png', 'General');
    """)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute('TRUNCATE chats_permission CASCADE ;')
    op.execute('TRUNCATE chats CASCADE ;')
    # ### end Alembic commands ###
