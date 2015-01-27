from freq_api import db

class Freq(db.Model):
    __tablename__= 'freqs'
    pos = db.Column(db.Text, primary_key=True, index=True)
    i = db.Column(db.Integer, index=True)
    clst = db.Column(db.Text, primary_key=True)
    dataset = db.Column(db.Text)
    ma = db.Column(db.Text)
    maja = db.Column(db.Text)
    maf = db.Column(db.Float)
    mac = db.Column(db.Integer)
    nobs = db.Column(db.Integer)

class rsID(db.Model):
    __tablename__= 'rsIDs'
    pos = db.Column(db.Text, index=True)
    rsID = db.Column(db.Text, primary_key=True)
    build = db.Column(db.Text, primary_key=True, index=True)

class Coordinate(db.Model):
    __tablename__= 'coordinates'
    clst = db.Column(db.Text, primary_key=True, index=True)
    dataset = db.Column(db.Text, primary_key=True, index=True)
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)
