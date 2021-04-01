#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDFilter.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/HeavyIonEvent/interface/Centrality.h"
#include "iostream"

class QWZDCPUFilter : public edm::EDFilter {
    public:
        explicit QWZDCPUFilter(const edm::ParameterSet&);
        ~QWZDCPUFilter() {return;}
    private:
        virtual bool filter(edm::Event&, const edm::EventSetup&);

        edm::InputTag	    src_;
        std::vector<double> posPars_, negPars_;
        int                 mode_;
        bool                debug_;
};

QWZDCPUFilter::QWZDCPUFilter(const edm::ParameterSet& pset) :
    src_(pset.getUntrackedParameter<edm::InputTag>("src")),
    posPars_(pset.getUntrackedParameter<std::vector<double>>("posPars")),
    negPars_(pset.getUntrackedParameter<std::vector<double>>("negPars")),
    mode_(pset.getUntrackedParameter<int>("mode", 3)),
    debug_(pset.getUntrackedParameter<bool>("debug", false))
{
    consumes<reco::Centrality>(src_);
    return;
}

bool QWZDCPUFilter::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
    edm::Handle<reco::Centrality> pCent;
    iEvent.getByLabel( src_, pCent );

    double etHFtowerSum = pCent->EtHFtowerSum();
    double zdcSumPlus = pCent->zdcSumPlus();
    double zdcSumMinus = pCent->zdcSumMinus();

    double pcut= 0;
    double ncut= 0;
    for ( unsigned int i = 0; i < posPars_.size(); i++ ) {
        pcut += posPars_[i] * std::pow( etHFtowerSum, int(i) );
    }
    for ( unsigned int i = 0; i < negPars_.size(); i++ ) {
        ncut += negPars_[i] * std::pow( etHFtowerSum, int(i) );
    }

    if ( debug_ ) {
        std::cout << " !! QW debug --> etHFtowerSum = " << etHFtowerSum << "\t zdcSumPlus = " << zdcSumPlus << "\t zdcSumMinus = " << zdcSumMinus << "\t pcut = " << pcut << "\t ncut = " << ncut << std::endl;
    }

    if ( mode_ == 0 ) {
        if ( (zdcSumPlus>pcut) and (zdcSumMinus>pcut) ) return false;
        else return true;
    } else if ( mode_ == 1 ) {
        if ( (zdcSumPlus>pcut) ) return false;
        else return true;
    } else if ( mode_ == 2 ) {
        if ( (zdcSumMinus>ncut) ) return false;
        else return true;
    } else if ( mode_ == 3 ) {
        if ( (zdcSumPlus>pcut) or (zdcSumMinus>pcut) ) return false;
        else return true;
    }

    return true;
}

DEFINE_FWK_MODULE(QWZDCPUFilter);
