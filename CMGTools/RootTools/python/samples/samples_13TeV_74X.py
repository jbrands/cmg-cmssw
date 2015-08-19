import PhysicsTools.HeppyCore.framework.config as cfg
import os

#####COMPONENT CREATOR

from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator
kreator = ComponentCreator()

#testfile = kreator.makeMCComponent("testfile", "/data/jbrandstetter/ntuplesForSynchro/tauMu_fullsel_tree_CMG.root", "CMS", "*.root")
testfile = kreator.makeMCComponent("testfile", "/data/jbrandstetter/ntuplesForSynchro/tauMu_fullsel_tree_CMG.root", "CMS", ".*root")

### ==== SPRING15 =====
SUSYGluGlu = kreator.makeMCComponent("SUSYGluGlu", " /SUSYGluGluToHToTauTau_M-160_TuneCUETP8M1_13TeV-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM", "CMS", ".*root")

