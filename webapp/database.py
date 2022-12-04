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
    image = Column(String, nullable=False)
    html = Column(String, nullable = False)

    def __init__(self, tree_id=None, tree_name=None, leaftype=None, barktype=None, fruittype=None, image=None, html=None):
        self.tree_id = tree_id
        self.tree_name = tree_name
        self.leaftype = leaftype
        self.barktype = barktype
        self.fruittype = fruittype
        self.image = image
        self.html = html


    def __repr__(self):
        return f'<User {self.tree_id, self.tree_name, self.leaftype, self.barktype, self.fruittype, self.image, self.html!r}>'


# our queries to input various things into tree.db

# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype, image, html) VALUES("Red Oak", "Pointed Lobes", "Scaly", "Acorn", "static/img/lobed/red-oak.jpg", "lobed.html");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype, image, html) VALUES ("White Oak", "Curved Lobes", "Scaly", "Acorn", "static/img/lobed/white-oak.jpg", "lobed.html");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype, image, html) VALUES ("Swamp White Oak", "Curved Lobes", "Scaly", "Acorn", "static/img/lobed/swamp-white-oak.jpg", "lobed.html");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype, image, html) VALUES ("Scarlet Oak", "Pointed Lobes", "Scaly", "Acorn", "static/img/lobed/scarlet-oak.jpg", "lobed.html");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype, image, html) VALUES ("Pin Oak", "Pointed Lobes", "Slightly Smooth", "Acorn", "static/img/lobed/pin-oak.jpg", "lobed.html");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype, image, html) VALUES ("Black Oak", "Pointed Lobes", "Scaly", "Acorn", "static/img/lobed/black-oak.jpeg", "lobed.html");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype, image, html) VALUES ("Eastern White Pine", "Needles", "Scaly", "Cone", "static/img/needles/eastern-white-pine.jpg", "needles.html");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype, image, html) VALUES ("Swiss Stone Pine", "Needles", "Flaky", "Cone", "static/img/needles/swiss-stone-pine.jpeg", "needles.html");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype, image, html) VALUES ("Austrian Pine", "Needles", "Scaly", "Cone", "static/img/needles/austrian-pine.jpg", "needles.html");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype, image, html) VALUES ("English Yew", "Needles", "Flaky", "Berry", "static/img/needles/english-yew.jpg", "needles.html");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype, image, html) VALUES ("Cedar of Lebanon", "Needles", "Scaly", "Cone", "static/img/needles/ceder-lebanon.jpg", "needles.html");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype, image, html) VALUES ("Dawn Redwood", "Needles", "Flaky", "Cone", "static/img/needles/dawn-redwood.jpg", "needles.html");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype, image, html) VALUES ("Western Larch", "Needles", "Scaly", "Cone", "static/img/needles/western-larch.jpg", "needles.html");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype, image, html) VALUES ("Sweetgum", "Pointed", "Scaly", "Berry", "static/img/pointed/sweetgum.jpg", "pointed.html");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype, image, html) VALUES ("Red Maple", "Pointed", "Slightly Smooth", "Helicopter", "static/img/pointed/red-maple.jpg", "pointed.html");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype, image, html) VALUES ("American Sycamore", "Pointed", "Flaky", "Berry", "static/img/pointed/american-sycamore.jpg", "pointed.html");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype, image, html) VALUES ("Hedge Maple", "Pointed", "Scaly", "Helicopter", "static/img/pointed/hedge-maple.jpg", "pointed.html");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype, image, html) VALUES ("Norway Maple", "Pointed", "Scaly", "Helicopter", "static/img/pointed/norway-maple.jpg", "pointed.html");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype, image, html) VALUES ("Sugar Maple", "Pointed", "Scaly", "Helicopter", "static/img/pointed/sugar-maple.jpg", "pointed.html");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype, image, html) VALUES ("Japanese Maple", "Pointed", "Super Smooth", "Helicopter", "static/img/pointed/japanese-maple.jpg", "pointed.html");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype, image, html) VALUES ("Tuliptree", "Pointed", "Scaly", "Flower", "static/img/pointed/tuliptree.jpg", "pointed.html");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype, image, html) VALUES ("Honeylocust", "Compound", "Flaky", "Bean Pod", "static/img/compound/honeylocust.jpg", "string.html");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype, image, html) VALUES ("Japanese Pagoda Tree", "Compound", "Scaly", "Bean Pod", "static/img/compound/japanese-pagoda-tree.jpg", "string.html");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype, image, html) VALUES ("Golden Rain Tree", "Compound", "Scaly", "Flower", "static/img/compound/golden-rain-tree.jpg", "string.html");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype, image, html) VALUES ("Black Locust", "Compound", "Flaky", "Bean Pod", "static/img/compound/black-locust.jpg", "string.html");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype, image, html) VALUES ("Ash Tree", "Compound", "Scaly", "Helicopter", "static/img/compound/ash-tree.jpg", "string.html");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype, image, html) VALUES ("White Ash", "Compound", "Scaly", "Helicopter", "static/img/compound/white-ash.jpg", "string.html");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype, image, html) VALUES ("Black Walnut", "Compound", "Scaly", "Nut", "static/img/compound/black-walnut.jpg", "string.html");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype, image, html) VALUES ("Kentucky Coffee Tree", "Compound", "Flaky", "Bean Pod", "static/img/compound/kentucky-coffee-tree.jpg", "string.html");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype, image, html) VALUES ("Yellowwood", "Compound", "Super Smooth", "Bean Pod", "static/img/compound/yellowwood.jpg", "string.html");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype, image, html) VALUES ("American Elm", "Ridged Teardrop", "Scaly", "Helicopter", "static/img/teardrop/american-elm.jpg", "teardrop.html");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype, image, html) VALUES ("English Elm", "Ridged Teardrop", "Scaly", "Helicopter", "static/img/teardrop/english-elm.jpg", "teardrop.html");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype, image, html) VALUES ("Beech Tree", "Ridged Teardrop", "Super Smooth", "Nut", "static/img/teardrop/beech-tree.jpg", "teardrop.html");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype, image, html) VALUES ("Hackberry", "Ridged Teardrop", "Scaly", "Berry", "static/img/teardrop/hackberry.jpg", "teardrop.html");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype, image, html) VALUES ("Birch Tree", "Ridged Teardrop", "Flaky", "Cone", "static/img/teardrop/birch.jpg", "teardrop.html");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype, image, html) VALUES ("Hornbeam", "Ridged Teardrop", "Slightly Smooth", "Helicopter", "static/img/teardrop/hornbeam.jpg", "teardrop.html");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype, image, html) VALUES ("Zelkova", "Ridged Teardrop", "Slightly Smooth", "Berry", "static/img/teardrop/zelkova.jpg", "teardrop.html");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype, image, html) VALUES ("Crabapple", "Ridged Teardrop", "Flaky", "Berry", "static/img/teardrop/crabapple.jpg", "teardrop.html");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype, image, html) VALUES ("Saucer Magnolia", "Long Teardrop", "Super Smooth", "Flower", "static/img/teardrop/saucer-magnolia.jpg", "teardrop.html");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype, image, html) VALUES ("White Fringe Tree", "Long Teardrop", "Slightly Smooth", "Berry", "static/img/teardrop/white-fringe.jpg", "teardrop.html");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype, image, html) VALUES ("Magnolia Tree", "Long Teardrop", "Slightly Smooth", "Flower", "static/img/teardrop/magnolia.jpg", "teardrop.html");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype, image, html) VALUES ("Shingle Oak", "Long Teardrop", "Scaly", "Acorn", "static/img/teardrop/shingle-oak.jpg", "teardrop.html");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype, image, html) VALUES ("Black Gum", "Long Teardrop", "Scaly", "Berry", "static/img/teardrop/black-gum.jpg", "teardrop.html");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype, image, html) VALUES ("Gingko", "Misc", "Scaly", "Berry", "static/img/gingko.jpg", "misc.html");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype, image, html) VALUES ("Holly", "Pointed", "Super Smooth", "Berry", "static/img/pointed/holly.jpg", "pointed.html");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype, image, html) VALUES ("European Beech", "Misc", "Super Smooth", "Nut", "static/img/european-beech.jpg", "misc.html");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype, image, html) VALUES ("Hawthorn Tree", "Misc", "Flaky", "Berry", "static/img/hawthorn.jpg", "misc.html");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype, image, html) VALUES ("Little-Leaf Linden", "Misc", "Scaly", "Flower", "static/img/little-leaf-linden.jpg", "misc.html");
# INSERT INTO Tree(tree_name, leaftype, barktype, fruittype, image, html) VALUES ("Redbud", "Misc", "Flaky", "Flower", "static/img/redbud.jpeg", "misc.html");