import FWCore.ParameterSet.Config as cms

# Update HfRing thresholds to accomodate di-iso tau trigger thresholds
from L1TriggerConfig.L1ScalesProducers.l1CaloScales_cfi import l1CaloScales
l1CaloScales.L1HfRingThresholds = cms.vdouble(0.0, 24.0, 28.0, 32.0, 36.0, 40.0, 44.0, 48.0)

l1CaloScales.L1HtMissThresholds = cms.vdouble(
0.0,	0.00787401574803,	0.0157480314961,	0.0236220472441,	0.0314960629921,	0.0393700787402,	0.0472440944882,	0.0551181102362,	0.0629921259843,	0.0708661417323,	0.0787401574803,
0.0866141732283,	0.0944881889764,	0.102362204724,	0.110236220472,	0.11811023622,	0.125984251969,	0.133858267717,	0.141732283465,	0.149606299213,	0.157480314961,
0.165354330709,	0.173228346457,	0.181102362205,	0.188976377953,	0.196850393701,	0.204724409449,	0.212598425197,	0.220472440945,	0.228346456693,	0.236220472441,
0.244094488189,	0.251968503937,	0.259842519685,	0.267716535433,	0.275590551181,	0.283464566929,	0.291338582677,	0.299212598425,	0.307086614173,	0.314960629921,
0.322834645669,	0.330708661417,	0.338582677165,	0.346456692913,	0.354330708661,	0.362204724409,	0.370078740157,	0.377952755906,	0.385826771654,	0.393700787402,
0.40157480315,	0.409448818898,	0.417322834646,	0.425196850394,	0.433070866142,	0.44094488189,	0.448818897638,	0.456692913386,	0.464566929134,	0.472440944882,
0.48031496063,	0.488188976378,	0.496062992126,	0.503937007874,	0.511811023622,	0.51968503937,	0.527559055118,	0.535433070866,	0.543307086614,	0.551181102362,
0.55905511811,	0.566929133858,	0.574803149606,	0.582677165354,	0.590551181102,	0.59842519685,	0.606299212598,	0.614173228346,	0.622047244094,	0.629921259843,
0.637795275591,	0.645669291339,	0.653543307087,	0.661417322835,	0.669291338583,	0.677165354331,	0.685039370079,	0.692913385827,	0.700787401575,	0.708661417323,
0.716535433071,	0.724409448819,	0.732283464567,	0.740157480315,	0.748031496063,	0.755905511811,	0.763779527559,	0.771653543307,	0.779527559055,	0.787401574803,
0.795275590551,	0.803149606299,	0.811023622047,	0.818897637795,	0.826771653543,	0.834645669291,	0.842519685039,	0.850393700787,	0.858267716535,	0.866141732283,
0.874015748031,	0.88188976378,	0.889763779528,	0.897637795276,	0.905511811024,	0.913385826772,	0.92125984252,	0.929133858268,	0.937007874016,	0.944881889764,
0.952755905512,	0.96062992126,	0.968503937008,	0.976377952756,	0.984251968504,	0.992125984252,	1.0,
)

