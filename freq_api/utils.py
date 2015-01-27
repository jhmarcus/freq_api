from flask import jsonify

def dict_factory(cursor, row):
    '''
    '''
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def define_freqscale(json_data):
    '''
    helper function to add freqscale to json
    '''
    maxfreq = 0
    for i in range(0,len(json_data)):
        if json_data[i]['maf']>maxfreq:
            maxfreq=json_data[i]['maf']
    if maxfreq<0.001:
        for i in range(0,len(json_data)):
            json_data[i]['freqs']=[json_data[i]['maf']*1000,1-json_data[i]['maf']*1000]
            json_data[i]['freqScale']=0.001
    elif maxfreq<0.01:
        for i in range(0,len(json_data)):
            json_data[i]['freqs']=[json_data[i]['maf']*100,1-json_data[i]['maf']*100]
            json_data[i]['freqScale']=0.01
    elif maxfreq<0.1:
        for i in range(0,len(json_data)):
            json_data[i]['freqs']=[json_data[i]['maf']*10,1-json_data[i]['maf']*10]
            json_data[i]['freqScale']=0.1
    else:
        for i in range(0,len(json_data)):
            json_data[i]['freqs']=[json_data[i]['maf'],1-json_data[i]['maf']]
            json_data[i]['freqScale']=1

    return json_data

def query_by_pos(c, dataset, pos, build):
    '''
    '''
    data = []
    rsID_res = c.execute('SELECT * FROM rsIDs WHERE pos=?', (pos,)).fetchone()
    if rsID_res:
        rsID = rsID_res['rsID']
    else:
        rsID = 'NA'

    coords_res = c.execute('SELECT * FROM coordinates WHERE dataset=?', (dataset,)).fetchall()
    coords = {}
    for row in coords_res:
        coords[row['clst']] = [row['lon'], row['lat']]

    for row in c.execute('SELECT * FROM freqs WHERE dataset=? AND pos=?', (dataset, pos,)):
        clst = row['clst']
        data.append({'pos':row['pos'], 'rsID':rsID, 'clst':clst, 'dataset':dataset,
                     'coordinates':coords[clst], 'minAllele':row['ma'], 'majAllele':row['maja'],
                     'maf':row['maf'], 'mac':row['mac'], 'nobs':row['nobs']})

    data = define_freqscale(data)
    return jsonify(results=data)

def query_by_rsID(c, dataset, rsID, build):
    '''
    '''
    data = []
    rsID_res = c.execute('SELECT * FROM rsIDs WHERE rsID=?', (rsID,)).fetchone()
    pos = rsID_res['pos']

    coords_res = c.execute('SELECT * FROM coordinates WHERE dataset=?', (dataset,)).fetchall()
    coords = {}
    for row in coords_res:
        coords[row['clst']] = [row['lon'], row['lat']]

    for row in c.execute('SELECT * FROM freqs WHERE dataset=? AND pos=?', (dataset, pos,)):
        clst = row['clst']
        data.append({'pos':row['pos'], 'rsID':rsID, 'clst':clst, 'dataset':dataset,
                     'coordinates':coords[clst], 'minAllele':row['ma'], 'majAllele':row['maja'],
                     'maf':row['maf'], 'mac':row['mac'], 'nobs':row['nobs']})

    data = define_freqscale(data)
    return jsonify(results=data)
