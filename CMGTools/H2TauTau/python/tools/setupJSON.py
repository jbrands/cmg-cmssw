import os 
from CMGTools.H2TauTau.skims.applyJSON_cff import *
from CMGTools.RootTools.json.jsonPick import *
from CMGTools.H2TauTau.officialJSONS import jsonMap

def setupJSON( process ):

    print 'setting up JSON:'

    fileName = process.source.fileNames[0]
    # in case filename is a local filename, removing CMGLOCALBASEDIR
    #Jose: dont know where this var is set
    #fileName = fileName.replace( os.environ['CMGLOCALBASEDIR'],'' ) 
    json = 'Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON.txt'
    #json = jsonPick( fileName, jsonMap )
    print json
    applyJSON(process, json )
    return json
