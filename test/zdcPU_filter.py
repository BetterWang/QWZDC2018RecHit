import FWCore.ParameterSet.Config as cms
from Configuration.StandardSequences.Eras import eras

process = cms.Process('MyTree',eras.Run2_2018_pp_on_AA)

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff")
process.GlobalTag.globaltag = "103X_dataRun2_Prompt_v2"
process.GlobalTag.snapshotTime = cms.string("9999-12-31 23:59:59.000")
process.GlobalTag.toGet.extend([
    cms.PSet(record = cms.string("HeavyIonRcd"),
        tag = cms.string("CentralityTable_HFtowers200_DataPbPb_periHYDJETshape_run2v1033p1x01_offline"),
        connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS"),
        label = cms.untracked.string("HFtowers")
        ),
    ])

process.load("RecoHI.HiCentralityAlgos.CentralityBin_cfi")
process.centralityBin.Centrality = cms.InputTag("hiCentrality")
process.centralityBin.centralityVariable = cms.string("HFtowers")

#-----------------------------------
# Input source
#-----------------------------------
process.source = cms.Source('PoolSource',
        fileNames = cms.untracked.vstring('file:/afs/cern.ch/user/q/qwang/work/cleanroomRun2/Ana/data/PbPb2018_MB.root')
    )

#-----------
# Log output
#-----------
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.threshold = ''
process.MessageLogger.cerr.FwkReport.reportEvery = 1000
process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True),
    SkipEvent = cms.untracked.vstring('ProductNotFound')
    )

#-----------------
# Files to process
#-----------------
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
    )

#-----------------------------------------
# HLT selection -- MB
#-----------------------------------------

import HLTrigger.HLTfilters.hltHighLevel_cfi

process.hltSelect = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
process.hltSelect.HLTPaths = [
    "HLT_HIMinimumBias_*",
]
process.hltSelect.andOr = cms.bool(True)
process.hltSelect.throw = cms.bool(False)

#-----------------------------------------
# CMSSW Event Selection
#-----------------------------------------
process.load('HeavyIonsAnalysis.Configuration.hfCoincFilter_cff')
process.load('HeavyIonsAnalysis.Configuration.collisionEventSelection_cff')

process.eventSelection = cms.Sequence(
    process.primaryVertexFilter
    * process.hfCoincFilter2Th4
    * process.clusterCompatibilityFilter
)

# ZDC rechit
process.load('QWAna.QWZDC2018RecHit.QWZDC2018Producer_cfi')
process.load('QWAna.QWZDC2018RecHit.QWZDC2018RecHit_cfi')

#-----------------------
# new centrality object with ZDC
#-----------------------
process.newCent = cms.EDProducer("CentralityProducer",
    produceHFhits = cms.bool(False),
    produceHFtowers = cms.bool(False),
    produceEcalhits = cms.bool(False),
    produceZDChits = cms.bool(True),
    produceETmidRapidity = cms.bool(False),
    producePixelhits = cms.bool(False),
    produceTracks = cms.bool(False),
    producePixelTracks = cms.bool(False),
    reUseCentrality = cms.bool(True),
    srcZDChits = cms.InputTag("QWzdcreco"),
    lowGainZDC = cms.bool(True),

    doPixelCut = cms.bool(True),
    UseQuality = cms.bool(True),
    TrackQuality = cms.string('highPurity'),
    trackEtaCut = cms.double(2),
    trackPtCut = cms.double(1),
    hfEtaCut = cms.double(4), #hf above the absolute value of this cut is used
    midRapidityRange = cms.double(1),
    srcReUse = cms.InputTag("hiCentrality")
    )

#--------------------------------
# ZDC PU filter
# mode
#   0: pos AND neg
#   1: pos
#   2: neg
#   3: pos OR neg (default)
#--------------------------------
process.zdcPUfilter = cms.EDFilter('QWZDCPUFilter',
    src = cms.untracked.InputTag("newCent"),
    posPars = cms.untracked.vdouble(1098914.0, -174.),
    negPars = cms.untracked.vdouble(1322071.0, -193.),
    mode = cms.untracked.int32(3)
)

process.p = cms.Path(
    process.hltSelect *
    process.eventSelection *
    process.zdcdigi *
    process.QWzdcreco *
    process.newCent *
    process.zdcPUfilter
    )


