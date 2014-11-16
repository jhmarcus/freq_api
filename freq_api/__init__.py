from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext import restful
from flask.ext.restful import reqparse
from flask.ext.restful.utils import cors

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
api = restful.Api(app)
api.decorators=[cors.crossdomain(origin='*')]

from freq_api import models

parser = reqparse.RequestParser()
parser.add_argument('chr',type=int)
parser.add_argument('pos',type=int)
parser.add_argument('rsID',type=str)

@app.route('/')
def index():
    return "API for accessing population frequency data from Novembre Lab."

class Freq(restful.Resource):
    '''
    '''
    def get(self):
        args=parser.parse_args()
        if args['chr'] and args['pos']:
            data = []
            freq_response = models.Freq.query.filter_by(chr=args['chr'], pos=args['pos'])
            rsID_response = models.rsID.query.filter_by(snp=str(args['chr'])+':'+str(args['pos']))
            rsID = rsID_response.first()
            if rsID != None:
                rsID = rsID.rsID
            for res in freq_response:
                data.append({'chr':res.chr, 'pos':res.pos, 'snp':res.snp, 'rsID':rsID, 'clst':res.clst,
                             'dataset':res.dataset, 'ma':res.ma, 'maja':res.maja, 'maf':res.maf, 'mac':res.mac,
                             'nobs':res.nobs})
            return data
        elif args['rsID']:
            data = []
            rsID_response = models.rsID.query.filter_by(rsID=args['rsID'])
            rsID = rsID_response.first()
            snp = rsID.snp
            rsID = rsID.rsID
            freq_response = models.Freq.query.filter_by(snp=snp)
            for res in freq_response:
                data.append({'chr':res.chr, 'pos':res.pos, 'snp':res.snp, 'rsID':rsID, 'clst':res.clst,
                             'dataset':res.dataset, 'ma':res.ma, 'maja':res.maja, 'maf':res.maf, 'mac':res.mac,
                             'nobs':res.nobs})
            return data
        else:
            return 403

api.add_resource(Freq, '/freq')

if __name__ == '__main__':
    app.run(debug=True)
