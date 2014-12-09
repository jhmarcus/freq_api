from flask import Flask
from flask import jsonify
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext import restful
from flask.ext.restful import reqparse
from flask.ext.restful.utils import cors
from sqlalchemy.sql.expression import func, select
from freq_api import utils
import random

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
parser.add_argument('random', type=bool)
parser.add_argument('dataset', type=str, required=True)

dataset_to_bulid_dict = {
                            '1000genomes_phase3':'GRCh37'
                        }

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
            build = dataset_to_bulid_dict[args['dataset']]
            freq_response = models.Freq.query.filter_by(dataset=args['dataset'], chr=args['chr'], pos=args['pos'])
            rsID_response = models.rsID.query.filter_by(build=build, snp=str(args['chr'])+':'+str(args['pos']))
            rsID = rsID_response.first()
            if rsID != None:
                rsID = rsID.rsID
            for res in freq_response:
                data.append({'chr':res.chr, 'pos':res.pos, 'snp':res.snp, 'rsID':rsID, 'clst':res.clst,
                             'dataset':res.dataset, 'minAllele':res.ma, 'majAllele':res.maja, 'maf':res.maf, 'mac':res.mac,
                             'nobs':res.nobs})
            data = utils.define_freqscale(data)
            return jsonify(results=data)
        elif args['rsID']:
            data = []
            build = dataset_to_bulid_dict[args['dataset']]
            rsID_response = models.rsID.query.filter_by(build=build, rsID=args['rsID'])
            rsID = rsID_response.first()
            snp = rsID.snp
            rsID = rsID.rsID
            freq_response = models.Freq.query.filter_by(dataset=args['dataset'], snp=snp)
            for res in freq_response:
                data.append({'chr':res.chr, 'pos':res.pos, 'snp':res.snp, 'rsID':rsID, 'clst':res.clst,
                             'dataset':res.dataset, 'minAllele':res.ma, 'majAllele':res.maja, 'maf':res.maf, 'mac':res.mac,
                             'nobs':res.nobs})
            data = utils.define_freqscale(data)
            return jsonify(results=data)
        elif args['random']==True:
            data = []
            build = dataset_to_bulid_dict[args['dataset']]
            #row_count = int(models.Freq.query.count())
            row_count = 186697368
            random_row = models.Freq.query.offset(random.randint(0, row_count - 1)).limit(1).first()
            chr = random_row.chr
            pos = random_row.pos
            freq_response = models.Freq.query.filter_by(dataset=args['dataset'], chr=chr, pos=pos)
            rsID_response = models.rsID.query.filter_by(build=build, snp=str(chr)+':'+str(pos))
            rsID = rsID_response.first()
            if rsID != None:
                rsID = rsID.rsID
            for res in freq_response:
                data.append({'chr':res.chr, 'pos':res.pos, 'snp':res.snp, 'rsID':rsID, 'clst':res.clst,
                             'dataset':res.dataset, 'minAllele':res.ma, 'majAllele':res.maja, 'maf':res.maf, 'mac':res.mac,
                             'nobs':res.nobs})
            data = utils.define_freqscale(data)
            return jsonify(results=data)
        else:
            return 403

api.add_resource(Freq, '/freq')

if __name__ == '__main__':
    app.run(debug=True)
