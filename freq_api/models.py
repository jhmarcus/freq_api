from freq_api import db

class Freq(db.Model):
    chr = db.Column(db.Integer)
    pos = db.Column(db.Integer)
    snp = db.Column(db.Text, primary_key=True)
    clst = db.Column(db.Text, primary_key=True)
    a1 = db.Column(db.Text)
    a2 = db.Column(db.Text)
    maf = db.Column(db.Float)
    mac = db.Column(db.Integer)
    nobs = db.Column(db.Integer)
