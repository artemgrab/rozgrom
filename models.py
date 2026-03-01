from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Text, Boolean
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    full_name = Column(String, unique=False, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, nullable=False)

    hashed_password = Column(String, nullable=False)

    is_active = Column(Boolean, default=True, nullable=True)        # Whether user is banned
    last_seen = Column(DateTime, onupdate=func.now())               # When user's info changes in db
    join_time = Column(DateTime, server_default=func.now())         # When user signed up

    messages_sent = relationship("Message", back_populates="sender", foreign_keys="[Message.sender_id]")


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    content = Column(Text)
    timestamp = Column(DateTime, server_default=func.now())

    sender_id = Column(Integer, ForeignKey("users.id"))
    receiver_id = Column(Integer, ForeignKey("users.id")) 
    chat_id = Column(Integer, ForeignKey("chats.id"))    

    sender = relationship("User", back_populates="messages_sent", foreign_keys=[sender_id])
    chat = relationship("Chat", back_populates="messages")


class Chat(Base):
    __tablename__ = "chats"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    chat_name = Column(String, nullable=True) # Назва (для груп)
    is_group = Column(Boolean, default=False) # Це приват чи група?
    created_at = Column(DateTime, server_default=func.now())

    # Зв'язок з повідомленнями
    messages = relationship("Message", back_populates="chat")