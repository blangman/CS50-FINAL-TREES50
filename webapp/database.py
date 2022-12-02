from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///tree.db')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    Base.metadata.create_all(bind=engine)
    db_session.commit()

# sql-alchemy table 
class Tree(Base):
    __tablename__ = 'Tree'
    __table_args__ = {'extend_existing': True} 

    tree_id = Column(Integer, primary_key=True, autoincrement=True)
    tree_name = Column(String, nullable = True)
    leaftype = Column(String, nullable = False)
    barktype = Column(String, nullable=False)
    fruittype = Column(String, nullable=False)

    def __init__(self, tree_id=None, tree_name=None, leaftype=None, barktype=None, fruittype=None):
        self.tree_id = tree_id
        self.tree_name = tree_name
        self.leaftype = leaftype
        self.barktype = barktype
        self.fruittype = fruittype

    def __repr__(self):
        return f'<User {self.tree_id, self.tree_name, self.leaftype, self.barktype, self.fruittype!r}>'


#my queries to input various things into the tree.db

# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype) VALUES("Red Oak", "Pointed Lobes", "Scaly", "Acorn");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype) VALUES ("White Oak", "Curved Lobes", "Scaly", "Acorn");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype) VALUES ("Swamp White Oak", "Curved Lobes", "Scaly", "Acorn");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype) VALUES ("Scarlet Oak", "Pointed Lobes", "Scaly", "Acorn");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype) VALUES ("Pin Oak", "Pointed Lobes", "Slightly Smooth", "Acorn");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype) VALUES ("Black Oak", "Pointed Lobes", "Scaly", "Acorn");