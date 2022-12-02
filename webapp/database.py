from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, VARCHAR
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
    tree_image_url = Column(VARCHAR, nullable=False)
    leaftype_html_url = Column(VARCHAR, nullable = False)

    def __init__(self, tree_id=None, tree_name=None, leaftype=None, barktype=None, fruittype=None, tree_image_url=None, leaftype_html_url=None):
        self.tree_id = tree_id
        self.tree_name = tree_name
        self.leaftype = leaftype
        self.barktype = barktype
        self.fruittype = fruittype
        self.tree_image_url = tree_image_url
        self.leaftype_html_url = leaftype_html_url


    def __repr__(self):
        return f'<User {self.tree_id, self.tree_name, self.leaftype, self.barktype, self.fruittype, self.tree_image_url, self.leaftype_html_url!r}>'


#my queries to input various things into the tree.db

# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype) VALUES("Red Oak", "Pointed Lobes", "Scaly", "Acorn");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype) VALUES ("White Oak", "Curved Lobes", "Scaly", "Acorn");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype) VALUES ("Swamp White Oak", "Curved Lobes", "Scaly", "Acorn");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype) VALUES ("Scarlet Oak", "Pointed Lobes", "Scaly", "Acorn");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype) VALUES ("Pin Oak", "Pointed Lobes", "Slightly Smooth", "Acorn");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype) VALUES ("Black Oak", "Pointed Lobes", "Scaly", "Acorn");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype) VALUES ("Eastern White Pine", "Needles", "Scaly", "Cone");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype) VALUES ("Swiss Stone Pine", "Needles", "Flaky", "Cone");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype) VALUES ("Austrian Pine", "Needles", "Scaly", "Cone");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype) VALUES ("English Yew", "Needles", "Flaky", "Berry");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype) VALUES ("Cedar of Lebanon", "Needles", "Scaly", "Cone");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype) VALUES ("Dawn Redwood", "Needles", "Flaky", "Cone");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype) VALUES ("Western Larch", "Needles", "Scaly", "Cone");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype) VALUES ("Sweetgum", "Pointed", "Scaly", "Berry");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype) VALUES ("Red Maple", "Pointed", "Slightly Smooth", "Helicopter");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype) VALUES ("American Sycamore", "Pointed", "Flaky", "Berry");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype) VALUES ("Hedge Maple", "Pointed", "Scaly", "Helicopter");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype) VALUES ("Norway Maple", "Pointed", "Scaly", "Helicopter");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype) VALUES ("Sycamore Maple", "Pointed", "Flaky", "Helicopter");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype) VALUES ("Sugar Maple", "Pointed", "Scaly", "Helicopter");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype) VALUES ("Japanese Maple", "Pointed", "Super Smooth", "Helicopter");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype) VALUES ("Tuliptree", "Pointed", "Scaly", "Flower");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype) VALUES ("Honeylocust", "Compound", "Flaky", "Bean Pod");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype) VALUES ("Japanese Pagoda Tree", "Compound", "Scaly", "Bean Pod");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype) VALUES ("Golden Rain Tree", "Compound", "Scaly", "Flower");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype) VALUES ("Black Locust", "Compound", "Flaky", "Bean Pod");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype) VALUES ("Ash Tree", "Compound", "Scaly", "Helicopter");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype) VALUES ("White Ash", "Compound", "Scaly", "Helicopter");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype) VALUES ("Black Walnut", "Compound", "Scaly", "Nut");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype) VALUES ("Kentucky Coffee Tree", "Compound", "Flaky", "Bean Pod");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype) VALUES ("Yellowwood", "Compound", "Super Smooth", "Bean Pod");