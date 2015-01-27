from flask import Flask
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
db = SQLAlchemy(app)
api = restful.Api(app)
api.decorators=[cors.crossdomain(origin='*')]

from freq_api import models

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
        '''
        '''
        args=parser.parse_args()
        conn = sqlite3.connect('/var/www/freq_api/freq_api/static/app.db')
        conn.row_factory = utils.dict_factory
        c = conn.cursor()

        if args['pos']:
            pos = args['pos']
            dataset = args['dataset']
            build = dataset_to_build_dict[dataset]
            data = utils.query_by_pos(c, dataset, pos, build)
            conn.close()
            return data
        elif args['rsID']:
            rsID = args['rsID']
            dataset = args['dataset']
            build = dataset_to_build_dict[dataset]
            data = utils.query_by_rsID(c, dataset, rsID, build)
            conn.close()
            return data
        elif args['random']==True:
            data = []
            dataset = args['dataset']
            build = dataset_to_build_dict[dataset]

            # get random row id
            table_res = c.execute('SELECT Count(*) FROM freqs').fetchone()
            table_size = int(table_res['Count(*)'])
            i = random.randint(1, table_size)
            rand_res = c.execute('SELECT * FROM freqs WHERE dataset=? AND i=?', (dataset, i,)).fetchone()
            pos = rand_res['pos']
            data = utils.query_by_pos(c, dataset, pos, build)
            conn.close()
            return data
        else:
            403

api.add_resource(Freq, '/freq')

if __name__ == '__main__':
    app.run(debug=True)
