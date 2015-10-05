import PhysicsTools.HeppyCore.framework.config as cfg
import os


#####COMPONENT CREATOR

from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator
kreator = ComponentCreator()


SUSYGluGluToHToTauTau_M160 = kreator.makeComponentHEPHY("SUSYGluGluToHToTauTau_M-160_TuneCUETP8M1_13TeV-pythia8", "/SUSYGluGluToHToTauTau_M-160_TuneCUETP8M1_13TeV-pythia8/jbrandst-Spring15_SUSYGluGlu_0309-29caa5e890ff30de023f0d90640e7759/USER", "PRIVATE", ".*root", "phys03", 1.0)
WJetsToLNu_TuneCUETP8M1 = kreator.makeComponentHEPHY("WJetsToLNu_TuneCUETP8M1","/WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/jbrandst-Spring15_WJetsToLNu_Asympt25ns_2109-944f06e45b67adf54f7518dd64f83326/USER","PRIVATE",".*root","phys03",1.0)
QCD_Pt15TTo7000_TuneZ2starFlat = kreator.makeComponentHEPHY("QCD_Pt15TTo7000_TuneZ2starFlat","/QCD_Pt-15TTo7000_TuneZ2star-Flat_13TeV_pythia6/jbrandst-Spring15_QCD_Asympt25ns_2209-944f06e45b67adf54f7518dd64f83326/USER","PRIVATE",".*root","phys03",1.0)
TT_TuneCUETP8M1 = kreator.makeComponentHEPHY("TT_TuneCUETP8M1","/TT_TuneCUETP8M1_13TeV-powheg-pythia8/jbrandst-Spring15_TT_Asympt25ns_2109-944f06e45b67adf54f7518dd64f83326/USER","PRIVATE","*.root","phys03",1.0)
DYJetsToLL_M50 = kreator.makeComponentHEPHY("DYJetsToLL_M50","/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/jbrandst-Spring15_DYJets_Asympt25ns_2109-944f06e45b67adf54f7518dd64f83326/USER","PRIVATE","*.root","phys03",1.0)

HiggsSignalSamples = [
    SUSYGluGluToHToTauTau_M160,
#    hephytest,
]

