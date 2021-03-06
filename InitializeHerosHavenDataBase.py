from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class User(Base):
    __tablename__ = 'User'
    # Define columns for the table User
    userid = Column(String(250), primary_key=True)  # Discord ids tend to be long save as a string to avoid overflow
    dtd = Column(Integer)  # Downtime Days
#    user = relationship("Character", backref="parent")  # Establish a 1-Many relationship


# class Character(Base):
#     __tablename__ = 'Character'
#     # Define columns for the table Character
#     userid = Column(String(250), ForeignKey('User.userid'))  # Link a character to a user
#     charid = Column(Integer, primary_key=True)  # Unique character id. Will autoincrement and doesn't need to be defined
#     charname = Column(String(250))  # Character name
#     charExp = Column(Integer)  # Character experience
#     charGold = Column(Integer)  # Character gold
#     charResidium = Column(Integer)  # Character residium
#     charRace = Column(String(250))  # Character race
#     charSTR = Column(Integer)  # Character Strength Score
#     charCON = Column(Integer)  # Character Constitution Score
#     charDEX = Column(Integer)  # Character Dexterity Score
#     charINT = Column(Integer)  # Character Intelligence Score
#     charWIS = Column(Integer)  # Character Wisdom Score
#     charCHA = Column(Integer)  # Character Charisma Score
#     charSKILLS = Column(String(250))  # String that indicates proficiency. 0 = NonProf; 1 = Prof; 2 = Expertise

# class Vote(Base):
#     __tablename__ = 'docket'
#     voteid = Column(Integer, primary_key=True)
#     voteComplete = Column(Integer, nullable=True)
#     voteCategory = Column(Integer)
#     voteOptions = Column(String(2500))


# Create an engine that stores data in memory
# sqlalchemy_example.db file.

# Create an engine that stores data in the local directory's
# HeroHavenDatabase.db file.
engine = create_engine('sqlite:///HeroHavenDatabase.db')

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)
