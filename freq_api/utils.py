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
