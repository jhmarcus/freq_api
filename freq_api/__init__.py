# still in the works

from flask import Flask
from flask import jsonify
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext import restful
from flask.ext.restful import reqparse
from flask.ext.restful.utils import cors
from sqlalchemy.sql.expression import func, select, exists
from freq_api import utils
import sqlite3
import random

app = Flask(__name__)
app.config.from_object('config')
# db = SQLAlchemy(app)
api = restful.Api(app)
api.decorators=[cors.crossdomain(origin='*')]

# from freq_api import models

parser = reqparse.RequestParser()
parser.add_argument('pos',type=str)
parser.add_argument('rsID',type=str)
parser.add_argument('random', type=bool)
parser.add_argument('dataset', type=str, required=True)

dataset_to_build_dict = {
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
        conn = sqlite3.connect('freq_api/static/app.db')
        conn.row_factory = utils.dict_factory
        c = conn.cursor()

        if args['pos']:
            data = []
            pos = args['pos']
            dataset = args['dataset']
            build = dataset_to_build_dict[dataset]
            t = (pos, )
            rsID_res = c.execute('SELECT * FROM rsIDs WHERE pos=?', t).fetchone()
            if rsID_res:
                rsID = rsID_res['rsID']
            else:
                rsID = 'NA'
            t = (dataset,)
            coords_res = c.execute('SELECT * FROM coordinates WHERE dataset=?', t).fetchall()
            coords = {}
            for row in coords_res:
                coords[row['clst']] = [row['lon'], row['lat']]
            t = (dataset, pos,)
            for row in c.execute('SELECT * FROM freqs WHERE dataset=? AND pos=?', t):
                data.append({'pos':row['pos'], 'rsID':rsID, 'clst':row['clst'], 'dataset':dataset, 'coordinates':coords[row['clst']],
                             'minAllele':row['ma'], 'majAllele':row['maja'], 'maf':row['maf'], 'mac':row['mac'], 'nobs':row['nobs']})

            data = utils.define_freqscale(data)
            conn.close()
            return jsonify(results=data)
        elif args['rsID']:
            data = []
            rsID = args['rsID']
            dataset = args['dataset']
            t = (rsID,)
            rsID_res = c.execute('SELECT * FROM rsIDs WHERE rsID=?', t).fetchone()
            pos = rsID_res['pos']
            t = (dataset,)
            coords_res = c.execute('SELECT * FROM coordinates WHERE dataset=?', t).fetchall()
            coords = {}
            for row in coords_res:
                coords[row['clst']] = [row['lon'], row['lat']]
            t = (dataset, pos,)
            for row in c.execute('SELECT * FROM freqs WHERE dataset=? AND pos=?', t):
                data.append({'pos':row['pos'], 'rsID':rsID, 'clst':row['clst'], 'dataset':dataset, 'coordinates':coords[row['clst']],
                             'minAllele':row['ma'], 'majAllele':row['maja'], 'maf':row['maf'], 'mac':row['mac'], 'nobs':row['nobs']})

            data = utils.define_freqscale(data)
            conn.close()
            return jsonify(results=data)
        # implement random snp
        else:
            403
        '''
        if args['pos']:
            data = []
            pos = args['pos']
            dataset = args['dataset']
            build = dataset_to_build_dict[dataset]
            freq_response = models.Freq.query.filter_by(dataset=dataset, pos=pos)
            rsID_response = models.rsID.query.filter_by(build=build, pos=pos)
            rsID = rsID_response.first()
            if rsID != None:
                rsID = rsID.rsID
            for res in freq_response:
                clst = res.clst
                coordinate_response = models.Coordinate.query.filter_by(clst=clst, dataset=dataset).first()
                lon = coordinate_response.lon
                lat = coordinate_response.lat
                data.append({'pos':res.pos, 'rsID':rsID, 'clst':clst, 'dataset':dataset, 'coordinates':[lon, lat],
                             'minAllele':res.ma, 'majAllele':res.maja, 'maf':res.maf, 'mac':res.mac, 'nobs':res.nobs})
            data = utils.define_freqscale(data)
            return jsonify(results=data)
        elif args['rsID']:
            data = []
            rsID = args['rsID']
            dataset = args['dataset']
            build = dataset_to_build_dict[dataset]
            rsID_response = models.rsID.query.filter_by(build=build, rsID=rsID).first()
            pos = rsID_response.pos
            rsID = rsID_response.rsID
            freq_response = models.Freq.query.filter_by(dataset=dataset, pos=pos)
            for res in freq_response:
                clst = res.clst
                coordinate_response = models.Coordinate.query.filter_by(clst=clst, dataset=dataset).first()
                lon = coordinate_response.lon
                lat = coordinate_response.lat
                data.append({'pos':res.pos, 'rsID':rsID, 'clst':res.clst, 'dataset':res.dataset, 'coordinates':[lon,lat],
                             'minAllele':res.ma, 'majAllele':res.maja, 'maf':res.maf, 'mac':res.mac, 'nobs':res.nobs})
            data = utils.define_freqscale(data)
            return jsonify(results=data)
        elif args['random']==True:
            data = []
            dataset = args['dataset']
            build = dataset_to_build_dict[dataset]
            row_count = int(models.Freq.query.count())
            #row_count = 186697368
            random_row = models.Freq.query.offset(random.randint(0, row_count - 1)).limit(1).first()
            pos = random_row.pos
            freq_response = models.Freq.query.filter_by(dataset=dataset, pos=pos)
            rsID_response = models.rsID.query.filter_by(build=build, pos=pos)
            rsID = rsID_response.first()
            if rsID != None:
                rsID = rsID.rsID
            for res in freq_response:
                clst = res.clst
                coordinate_response = models.Coordinate.query.filter_by(clst=clst, dataset=dataset).first()
                lon = coordinate_response.lon
                lat = coordinate_response.lat
                data.append({'pos':res.pos, 'rsID':rsID, 'clst':res.clst, 'dataset':res.dataset, 'coordinates':[lon,lat],
                             'minAllele':res.ma, 'majAllele':res.maja, 'maf':res.maf, 'mac':res.mac, 'nobs':res.nobs})
            data = utils.define_freqscale(data)
            return jsonify(results=data)
        else:
            return 403
        '''
api.add_resource(Freq, '/freq')

if __name__ == '__main__':
    app.run(debug=True)
