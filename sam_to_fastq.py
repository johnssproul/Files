#!

### Examples of FASTQ and SAM formats

##FASTQ
#		@GWNJ-7957:357:GW1901181790:2:1204:7578:37...
#		CGATTAATTTCGTGCCCTGTCCTGGACACGAAAACACGGAAA...
#		+
#		AAF7FJJJFFJJJJJJJJJAFJJJJJJFFFJFAJ7JJJJJJJ...

##SAM
#      GWNJ-7...   120    chrom_1    32    44    111M   =   280    360    CGAT..  AAF7..   

##SAM Fields
# COL   FIELD   TYPE      EXPLANATION
# 1     QNAME   String    Query template NAME
# 2     FLAG    Int       bitwise FLAG
# 3     RNAME   String    References sequence NAME
# 4     POS     Int       1- based leftmost mapping POSition
# 5     MAPQ    Int       MAPping Quality
# 6     CIGAR   String    CIGAR String
# 7     RNEXT   String    Ref. name of the mate/next read
# 8     PNEXT   Int       Position of the mate/next read
# 9     TLEN    Int       observed Template LENgth
# 10    SEQ     String    segment SEQuence
# 11    QUAL    String    ASCII of Phred-scaled base QUALity+33

### End examples




