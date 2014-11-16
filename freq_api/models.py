from freq_api import db

class rsID(db.Model):
    __tablename__= 'rsIDs'
    snp = db.Column(db.Text, index=True)
    rsID = db.Column(db.Text, primary_key=True, index=True)
    build = db.Column(db.Text)

class Freq(db.Model):
    __tablename__= 'freqs'
    chr = db.Column(db.Integer, index=True)
    pos = db.Column(db.Integer, index=True)
    snp = db.Column(db.Text, primary_key=True)
    clst = db.Column(db.Text, primary_key=True)
    dataset = db.Column(db.Text)
    ma = db.Column(db.Text)
    maja = db.Column(db.Text)
    maf = db.Column(db.Float)
    mac = db.Column(db.Integer)
    nobs = db.Column(db.Integer)
