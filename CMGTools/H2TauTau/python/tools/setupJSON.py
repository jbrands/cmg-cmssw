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
    
    #json = jsonPick( fileName, jsonMap )
    json = "Cert_246908-251883_13TeV_PromptReco_Collisions15_JSON_v2.txt"
    print json
    applyJSON(process, json )
    return json
