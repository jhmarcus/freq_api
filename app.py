import flask
import flask.ext.sqlalchemy
import flask.ext.restless

app = flask.Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/josephmarcus/Desktop/Work/Novembre_Lab/projects/vis/freq_api/test.db'
db = flask.ext.sqlalchemy.SQLAlchemy(app)

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

db.create_all()

reader = open('1000genomes.chr22.phase3.frq.strat.sample')
reader.readline()
for line in reader:
    line = line.strip('\n').split()
    if line[1].count(':') == 1 or line[1][:2] == 'rs':
        freq = Freq(chr=int(line[0]), pos=int(line[1].split(':')[1]), snp=line[1], clst=line[2], a1=line[3], a2=line[4], maf=float(line[5]), mac=int(line[6]), nobs=int(line[7]))
        db.session.add(freq)

db.session.commit()

manager = flask.ext.restless.APIManager(app, flask_sqlalchemy_db=db)
manager.create_api(Freq, methods=['GET'], url_prefix='/api/v1', results_per_page=None)

app.run(use_reloader=False)
