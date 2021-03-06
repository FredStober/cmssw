import FWCore.ParameterSet.Config as cms

#
# $Id: multi5x5PreshowerClusteringSequence_cff.py,v 1.1 2008/05/22 11:13:25 hegner Exp $
#
#------------------
#Preshower clustering:
#------------------
from RecoEcal.EgammaClusterProducers.multi5x5SuperClustersWithPreshower_cfi import *
# producer for endcap SuperClusters including preshower energy
from RecoEcal.EgammaClusterProducers.correctedMulti5x5SuperClustersWithPreshower_cfi import *
# producer for preshower cluster shapes
from RecoEcal.EgammaClusterProducers.multi5x5PreshowerClusterShape_cfi import *
# create sequence for preshower clustering
multi5x5PreshowerClusteringSequence = cms.Sequence(correctedMulti5x5SuperClustersWithPreshower*
                                                   multi5x5PreshowerClusterShape*
                                                   uncleanedOnlyMulti5x5SuperClustersWithPreshower*
                                                   uncleanedOnlyCorrectedMulti5x5SuperClustersWithPreshower)

