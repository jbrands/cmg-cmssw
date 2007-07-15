#ifndef PhysicsTools_MVAComputer_MVAComputer_h
#define PhysicsTools_MVAComputer_MVAComputer_h
// -*- C++ -*-
//
// Package:     MVAComputer
// Class  :     MVAComputer
//

//
// Author:	Christophe Saout <christophe.saout@cern.ch>
// Created:     Sat Apr 24 15:18 CEST 2007
// $Id: MVAComputer.h,v 1.2 2007/05/25 16:37:58 saout Exp $
//

#include <vector>
#include <memory>

#include "PhysicsTools/MVAComputer/interface/Calibration.h"
#include "PhysicsTools/MVAComputer/interface/VarProcessor.h"
#include "PhysicsTools/MVAComputer/interface/Variable.h"
#include "PhysicsTools/MVAComputer/interface/AtomicId.h"

namespace PhysicsTools {

/** \class MVAComputer
 *
 * \short Main interface class to the generic discriminator computer framework.
 *
 * The MVAComputer class represents an instance of the modular
 * discriminator computer. It is constructed from a "calibration" object
 * which contains all the required histograms, matrices and other trainina
 * data required for computing the discriminator. The calibration data also
 * defines the names and properties of variables that can passed to that
 * instance of the discriminator computer. The evaluation methods then
 * calculates the discriminator from a applicable set of input variables,
 * i.e. vector of key-value pairs.
 *
 ************************************************************/
class MVAComputer {
    public:
	/// construct a discriminator computer from a calibation object
	MVAComputer(const Calibration::MVAComputer *calib);
	~MVAComputer();

	/// evaluate variables given by a range of iterators given by \a first and \a last
	template<typename Iterator_t>
	double eval(Iterator_t first, Iterator_t last) const;

	/// evaluate variables in iterable container \a values
	template<typename Container_t>
	inline double eval(const Container_t &values) const
	{
		typedef typename Container_t::const_iterator Iterator_t;
		return this->template eval<Iterator_t>(
						values.begin(), values.end());
	}

    private:
	/** \class InputVar
	 * \short input variable configuration object
	 */
	struct InputVar {
		/// generic variable information (name, ...)
		Variable	var; 

		/// variable index in fixed-position evaluation array
		unsigned int	index;

		/// number of times each appearance of that variable can appear while computing the discriminator
		unsigned int	multiplicity;

		bool operator < (AtomicId id) const
		{ return var.getName() < id; }

		bool operator < (const InputVar &other) const
		{ return var.getName() < other.var.getName(); }
	};

	/** \class Processor
	 * \short variable processor container
	 */
	struct Processor {
		inline Processor(VarProcessor *processor,
		                 unsigned int nOutput) :
			processor(processor), nOutput(nOutput) {}

		inline Processor(const Processor &orig)
		{ processor = orig.processor; nOutput = orig.nOutput; }

		/// owned variable processor instance
		mutable std::auto_ptr<VarProcessor>	processor;

		/// number of output variables
		unsigned int				nOutput;
	};

	/// construct processors from calibration and setup variables
	void setup(const Calibration::MVAComputer *calib);

	/// map variable identifier \a name to the numerical position in the array
	unsigned int getVariableId(AtomicId name) const;

	/// evaluate discriminator from flattened variable array
	void eval(double *values, int *conf, unsigned int n) const;

	/// vector of input variables
	std::vector<InputVar>	inputVariables;

	/// vector of variable processors
	std::vector<Processor>	varProcessors;

	/// total number of variables to expect while computing discriminator
	unsigned int		nVars;

	/// index of the variable in the "conf" array to return as result
	unsigned int		output;
};

} // namespace PhysicsTools

#include "PhysicsTools/MVAComputer/interface/MVAComputer.icc"

#endif // PhysicsTools_MVAComputer_MVAComputer_h
