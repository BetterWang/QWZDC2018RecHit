import FWCore.ParameterSet.Config as cms

# ZDC 2018 PbPb run, gain for Fill7427

gainFill7427 = cms.VPSet(
		cms.PSet(
			object = cms.untracked.string('hZDCP_EM1'),
			calib = cms.untracked.double(0.1)
		),
		cms.PSet(
			object = cms.untracked.string('hZDCP_EM2'),
			calib = cms.untracked.double(0.1)
		),
		cms.PSet(
			object = cms.untracked.string('hZDCP_EM3'),
			calib = cms.untracked.double(0.07)
		),
		cms.PSet(
			object = cms.untracked.string('hZDCP_EM4'),
			calib = cms.untracked.double(0.08)
		),
		cms.PSet(
			object = cms.untracked.string('hZDCP_EM5'),
			calib = cms.untracked.double(0.06)
		),
		cms.PSet(
			object = cms.untracked.string('hZDCP_HAD1'),
			calib = cms.untracked.double(1.)
		),
		cms.PSet(
			object = cms.untracked.string('hZDCP_HAD2'),
			calib = cms.untracked.double(0.81)
		),
		cms.PSet(
			object = cms.untracked.string('hZDCP_HAD3'),
			calib = cms.untracked.double(0.67)
		),
		cms.PSet(
			object = cms.untracked.string('hZDCP_HAD4'),
			calib = cms.untracked.double(0.81)
		),
		cms.PSet(
			object = cms.untracked.string('hZDCM_EM1'),
			calib = cms.untracked.double(0.1)
		),
		cms.PSet(
			object = cms.untracked.string('hZDCM_EM2'),
			calib = cms.untracked.double(0.1)
		),
		cms.PSet(
			object = cms.untracked.string('hZDCM_EM3'),
			calib = cms.untracked.double(0.1)
		),
		cms.PSet(
			object = cms.untracked.string('hZDCM_EM4'),
			calib = cms.untracked.double(0.08)
		),
		cms.PSet(
			object = cms.untracked.string('hZDCM_EM5'),
			calib = cms.untracked.double(0.06)
		),
		cms.PSet(
			object = cms.untracked.string('hZDCM_HAD1'),
			calib = cms.untracked.double(1.)
		),
		cms.PSet(
			object = cms.untracked.string('hZDCM_HAD2'),
			calib = cms.untracked.double(0.62)
		),
		cms.PSet(
			object = cms.untracked.string('hZDCM_HAD3'),
			calib = cms.untracked.double(0.67)
		),
		cms.PSet(
			object = cms.untracked.string('hZDCM_HAD4'),
			calib = cms.untracked.double(0.87)
		),
		cms.PSet(
			object = cms.untracked.string('Pscale'),
			calib = cms.untracked.double(1000)
		),
		cms.PSet(
			object = cms.untracked.string('Mscale'),
			calib = cms.untracked.double(2000)
		),
        )
