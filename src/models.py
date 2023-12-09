import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
 __tablename__ = 'user'
id = Column(Integer, primary_key=True)
first_name = Column(String(250), nullable=False)
last_name = Column(String(250), nullable=False)
email = Column(String(250), nullable=False)
age = Column(Integer, nullable=False)


class Post(Base):
 __tablename__ = 'post'
id = Column(Integer, primary_key=True)
user_id = Column(Integer, ForeignKey >- ('user.id')) 
user = relationship(User)



class Comments(Base):
 __tablename__ = 'comments'
id  = Column(Integer, primary_key=True)  
date = Column(Integer, nullable=False)
text = Column(String(500))
post_id = Column(Integer, ForeignKey >- ('post.id'))
post = relationship(Post)
user_id = Column(Integer, ForeignKey >- ('user.id'))
user = relationship(User)


class Followers(Base):
 __tablename__ = 'fallowers'
user_id = Column(Integer, ForeignKey >-- ('user.id'))
user = relationship(User)



def to_dict(self):
 return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
