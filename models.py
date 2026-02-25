from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey, DateTime
from sqlalchemy.sql import func
from database import Base

# from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, unique=True, index=True)

    full_name = Column(String, unique=False, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, nullable=False)

    hashed_password = Column(String, nullable=False)

    is_active = Column(Boolean, default=True, nullable=True)  # User isn't banned
    last_seen = Column(DateTime, onupdate=func.now())  # When user's info changes in db
    join_time = Column(DateTime, server_default=func.now())  # When user signed up

    # messages_sent = relationship(
    #     "Message", backref="sender", foreign_keys="Message.sender_id"
    # )


# * Might be useful in future
class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    content = Column(Text)
    timestamp = Column(DateTime, server_default=func.now())

    sender_id = Column(Integer, ForeignKey("users.id"))
    reciever_id = Column(Integer, ForeignKey("users.id"))


# TODO: Create model for chats
