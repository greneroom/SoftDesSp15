class DNASequence(object):
    """ Represents a sequence of DNA """
<<<<<<< HEAD

=======
>>>>>>> 263d331044a840a5f2191e608e4cffca553b9e67
    def __init__(self, nucleotides):
        """ constructs a DNASequence with the specified nucleotides.
             nucleotides: the nucleotides represented as a string of
                          capital letters consisting of A's, C's, G's, and T's """
<<<<<<< HEAD
        self.nucleotides = nucleotides

=======
        pass
 
>>>>>>> 263d331044a840a5f2191e608e4cffca553b9e67
    def __str__(self):
        """ Returns a string containing the nucleotides in the DNASequence
        >>> seq = DNASequence("TTTGCC")
        >>> print seq
        TTTGCC
        """
<<<<<<< HEAD
        return self.nucleotides
=======
        pass
>>>>>>> 263d331044a840a5f2191e608e4cffca553b9e67

    def get_reverse_complement(self):
        """ Returns the reverse complement DNA sequence represented
            as an object of type DNASequence

            >>> seq = DNASequence("ATGC")
            >>> rev = seq.get_reverse_complement()
            >>> print rev
            GCAT
            >>> print type(rev)
            <class '__main__.DNASequence'>
<<<<<<< HEAD

        """
        comps = {'C': 'G', 'G': 'C', 'T': 'A', 'A': 'T'}
        rev_comp = ''
        for c in reversed(self.nucleotides):
            rev_comp += comps[c]
        return DNASequence(rev_comp)
=======
        """
        pass
>>>>>>> 263d331044a840a5f2191e608e4cffca553b9e67

    def get_proportion_ACGT(self):
        """ Computes the proportion of nucleotides in the DNA sequence
            that are 'A', 'C', 'G', and 'T'
            returns: a dictionary where each key is a nucleotide and the
                corresponding value is the proportion of nucleotides in the
            DNA sequence that are that nucleotide.
            (NOTE: this doctest will not necessarily always pass due to key
                    re-ordering don't worry about matching the order)
        >>> seq = DNASequence("AAGAGCGCTA")
        >>> d = seq.get_proportion_ACGT()
        >>> print (d['A'], d['C'], d['G'], d['T'])
        (0.4, 0.2, 0.3, 0.1)
        """
<<<<<<< HEAD
        return {c:(self.nucleotides.count(c) / float(len(self.nucleotides))) for c in ['A', 'C', 'G', 'T']}

if __name__ == '__main__':
    import doctest

=======
        pass

if __name__ == '__main__':
    import doctest
>>>>>>> 263d331044a840a5f2191e608e4cffca553b9e67
    doctest.testmod()
