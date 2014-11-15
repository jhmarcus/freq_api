from freq_api import db

class rsID(db.Model):
    __tablename__= 'rsIDs'
    chr_pos = db.Column(db.Text)
    rsID = db.Column(db.Text, primary_key=True)

class Freq(db.Model):
    __tablename__= 'freqs'
    chr = db.Column(db.Integer, index=True)
    pos = db.Column(db.Integer, index=True)
    snp = db.Column(db.Text, primary_key=True)
    clst = db.Column(db.Text, primary_key=True)
    ma = db.Column(db.Text)
    maja = db.Column(db.Text)
    maf = db.Column(db.Float)
    mac = db.Column(db.Integer)
    nobs = db.Column(db.Integer)
