
import .BamIO
import .BamAlignment  # p.s. I plan to rename this class/module to "BamRecord"

class MultiBamReader(object):
    #
    # So here you would implement a reader that takes a set of BAMs
    # and treats them as one data store, allowing iteration over
    # BamAlignment objects and a window
    #
    # I guess the only tricky bit is you might need to sort the
    # aggregated BAM records before you return them to the caller.
    #
    # All the functionality you need to enable is that of BamReader
    # and _BamReaderBase--- ignore IndexedBamReader (which refers to a
    # special pacbio index file, not the standard bam.bai)
    #

    # --- BamReaderBase API ---

    # need to override the stuff that gathers metadata (reference info
    # table, read group table, etc.), so that it aggregates it over
    # the sub-BAMs.  you should just need to append the underlying
    # tables, I believe.

    def _loadReferenceInfo(self):
        pass


    def _loadReadGroupInfo(self):
        pass


    def _loadProgramInfo(self):
        pass

    def _checkFileCompatibility(self):
        pass


    # --- BamReader API -----

    def __init__(self, fofnFilename?  listOfBamFnames? your choice;  optionalReferenceFastaFname):
        pass

    def __iter__(self):
        # iterate over each bam in turn.
        pass

    def readsInRange(self, winId, winStart, winEnd, justIndices=False):
        # this is what quiver actually uses.  aggregate over the bams,
        # probably you want to sort them before returning
        pass

    def __getitem__(self, rowNumbers):
        raise UnavailableFeature("Use IndexedBamReader to get row-number based slicing.")
