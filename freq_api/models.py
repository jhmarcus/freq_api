from freq_api import db

class rsID(db.Model):
    __tablename__= 'rsIDs'
    chr_pos = db.Column(db.Text)
    rsID = db.Column(db.Text,  primary_key=True)
    freqs = db.relationship('Freq', backref='rsID', lazy='dynamic')

class Freq(db.Model):
    __tablename__= 'freqs'
    chr = db.Column(db.Integer)
    pos = db.Column(db.Integer)
    snp = db.Column(db.Text, db.ForeignKey('rsIDs.chr_pos'), primary_key=True)
    clst = db.Column(db.Text, primary_key=True)
    a1 = db.Column(db.Text)
    a2 = db.Column(db.Text)
    maf = db.Column(db.Float)
    mac = db.Column(db.Integer)
    nobs = db.Column(db.Integer)
