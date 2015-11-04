import PhysicsTools.HeppyCore.framework.config as cfg
import os


#####COMPONENT CREATOR

from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator
kreator = ComponentCreator()


SUSYGluGluToHToTauTau_M160 = kreator.makeComponentHEPHY("SUSYGluGluToHToTauTau_M-160_TuneCUETP8M1_13TeV-pythia8", "/SUSYGluGluToHToTauTau_M-160_TuneCUETP8M1_13TeV-pythia8/jbrandst-Spring15_SUSYGluGlu_0309-29caa5e890ff30de023f0d90640e7759/USER", "PRIVATE", ".*root", "phys03", 1.0)

WJetsToLNu_TuneCUETP8M1 = kreator.makeComponentHEPHY("WJetsToLNu_TuneCUETP8M1","/WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/jbrandst-Spring15_WJetsToLNu_Asympt25ns_2109-944f06e45b67adf54f7518dd64f83326/USER","PRIVATE",".*root","phys03",1.0)
WJetsToLNu_TuneCUETP8M1_2 = kreator.makeComponentHEPHY("WJetsToLNu_TuneCUETP8M1_2","/WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/jbrandst-Wjets_MC2-a521298c1f16775ea1cf7ade8c6f81c7/USER","PRIVATE",".*root","phys03",1.0)

QCD_Pt15TTo7000_TuneZ2starFlat = kreator.makeComponentHEPHY("QCD_Pt15TTo7000_TuneZ2starFlat","/QCD_Pt-15TTo7000_TuneZ2star-Flat_13TeV_pythia6/jbrandst-Spring15_QCD_Asympt25ns_2209-944f06e45b67adf54f7518dd64f83326/USER","PRIVATE",".*root","phys03",1.0)

TT_TuneCUETP8M1 = kreator.makeComponentHEPHY("TT_TuneCUETP8M1","/TT_TuneCUETP8M1_13TeV-powheg-pythia8/jbrandst-Spring15_TT_Asympt25ns_2109-944f06e45b67adf54f7518dd64f83326/USER","PRIVATE","*.root","phys03",1.0)
TT_TuneCUETP8M1_small = kreator.makeComponentHEPHY("TT_TuneCUETP8M1_small","/TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/jbrandst-TTbar_MC2-a521298c1f16775ea1cf7ade8c6f81c7/USER","PRIVATE","*.root","phys03",1.0)

DYJetsToLL_M50 = kreator.makeComponentHEPHY("DYJetsToLL_M50","/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/jbrandst-Spring15_DYJets_Asympt25ns_2109-944f06e45b67adf54f7518dd64f83326/USER","PRIVATE","*.root","phys03",1.0)

DYJetsToLL_M50_2 = kreator.makeComponentHEPHY("DYJetsToLL_M50","/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/jbrandst-DYJetsToLL_MC2-a521298c1f16775ea1cf7ade8c6f81c7/USER","PRIVATE","*.root","phys03",1.0)

Run2015D_PromptReco_v3 = kreator.makeDataComponentHEPHY("Run2015D_PromptReco_v3","/SingleMuon/jbrandst-Run2015D-PromptReco-v3-c83e672fc034baa1893ed04e7be76a51/USER", "PRIVATE", "*.root","phys03","/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/Cert_246908-258159_13TeV_PromptReco_Collisions15_25ns_JSON.txt")

Run2015D_05Oct2015_v1 = kreator.makeDataComponentHEPHY("Run2015D_05Oct2015_v1","/SingleMuon/jbrandst-Run2015D-05Oct2015-v1-c83e672fc034baa1893ed04e7be76a51/USER", "PRIVATE", "*.root","phys03","/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/Cert_246908-258159_13TeV_PromptReco_Collisions15_25ns_JSON.txt")

Run2015D_05Oct2015_v1_2 = kreator.makeDataComponentHEPHY("Run2015D_05Oct2015_v1","/SingleMuon/jbrandst-Run2015D-05Oct2015-v1_2-3988b50fefc4fac1ce2afd98d7c19ed6/USER", "PRIVATE", "*.root","phys03","/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/Cert_246908-258159_13TeV_PromptReco_Collisions15_25ns_JSON.txt")


#################################################################################
SUSYGluGlu_miniAOD2 = kreator.makeComponentHEPHY("SUSYGluGlu_miniAOD2","/SUSYGluGluToHToTauTau_M-160_TuneCUETP8M1_13TeV-pythia8/jbrandst-SUSYGluGlu_miniAOD2-a4c76ddf8463ab427a155ae017238a46/USER","PRIVATE","*.root","phys03",1.0)

################################################################################

HiggsSignalSamples = [
    SUSYGluGluToHToTauTau_M160,
#    hephytest,
]

