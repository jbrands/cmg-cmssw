#include "CMGTools/TTHAnalysis/interface/PdfWeightProducerTool.h"
#include <cassert>

namespace LHAPDF {
      void initPDFSet(int nset, const std::string& filename, int member=0);
      int numberPDF(int nset);
      void usePDFMember(int nset, int member);
      double xfx(int nset, double x, double Q, int fl);
      double getXmin(int nset, int member);
      double getXmax(int nset, int member);
      double getQ2min(int nset, int member);
      double getQ2max(int nset, int member);
      void extrapolate(bool extrapolate=true);
}

void PdfWeightProducerTool::addPdfSet(const std::string &name) {
    pdfs_.push_back(name);
    weights_[name] = std::vector<double>();
}

void PdfWeightProducerTool::beginJob() {
    for (unsigned int i = 0, n = pdfs_.size(); i < n; ++i) {
        LHAPDF::initPDFSet(i+1, pdfs_[i]);
    }
}

void PdfWeightProducerTool::processEvent(const GenEventInfoProduct & pdfstuff) {
    float Q = pdfstuff.pdf()->scalePDF;

    int id1 = pdfstuff.pdf()->id.first;
    if(std::abs(id1)==21) id1=0;
    double x1 = pdfstuff.pdf()->x.first;
    //    double pdf1 = pdfstuff.pdf()->xPDF.first;

    int id2 = pdfstuff.pdf()->id.second;
    if(std::abs(id2)==21) id2=0;
    double x2 = pdfstuff.pdf()->x.second;
    //double pdf2 = pdfstuff.pdf()->xPDF.second;

    LHAPDF::usePDFMember(1,0);
    double pdf1 = LHAPDF::xfx(1, x1, Q, id1);
    double pdf2 = LHAPDF::xfx(1, x2, Q, id2);
    
    /*printf("pdf1: (%+8.4f), pdf2: (%+8.4f)\n",pdf1, pdf2);
    printf("Q: (%+8.4f)\n",Q);
    printf("id1: (%i)\n",id1);
    printf("x1: (%+8.4f)\n",x1);
    printf("id2: (%i)\n",id2);
    printf("x2: (%+8.4f)\n",x2);*/

    for (unsigned int i = 0, n = pdfs_.size(); i < n; ++i) {
        std::vector<double> & weights = weights_[pdfs_[i]];
        unsigned int nweights = 1;
        if (LHAPDF::numberPDF(i+1)>1) nweights += LHAPDF::numberPDF(i+1);
        weights.resize(nweights);

        for (unsigned int j = 0; j < nweights; ++j) { 
            LHAPDF::usePDFMember(i+1,j);
            double newpdf1 = LHAPDF::xfx(i+1, x1, Q, id1);
            double newpdf2 = LHAPDF::xfx(i+1, x2, Q, id2);
	    //printf("newpdf1: (%+8.4f), newpdf2: (%+8.4f)\n", newpdf1, newpdf2);
            weights[j] = (newpdf1/pdf1)*(newpdf2/pdf2);
	    //printf("weight: (%+8.4f)\n", weights[j]);
        }
    }
}

const std::vector<double> & PdfWeightProducerTool::getWeights(const std::string &name) const {
    std::map<std::string, std::vector<double> >::const_iterator match = weights_.find(name);
    assert(match != weights_.end()); 
    return match->second;   
}
