from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName   = 'Spring15_SUSYGluGlu_2507'
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName  = 'Analysis'
# Name of the CMSSW configuration file
config.JobType.psetName    = 'h2TauTauMiniAOD_cfg.py'

config.section_("Data")
config.Data.inputDataset = '/SUSYGluGluToHToTauTau_M-160_TuneCUETP8M1_13TeV-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = True
#config.Data.publication = False
# This string is used to construct the output dataset name
config.Data.publishDataName = 'Spring15_SUSYGluGlu_2507'
#!!!
config.Data.ignoreLocality = True

# These values only make sense for processing data
#    Select input data based on a lumi mask
#config.Data.lumiMask = 'Cert_190456-208686_8TeV_PromptReco_Collisions12_JSON.txt'
#    Select input data based on run-ranges
#config.Data.runRange = '190456-194076'

config.section_("Site")
# Where the output files will be transmitted to
config.Site.storageSite = 'T2_AT_Vienna'
config.Site.whitelist = ["T2_AT_Vienna"]
#config.Site.whitelist = ["T2_DE_DESY"]
#config.Site.blacklist = ['T2_AT_Vienna']
