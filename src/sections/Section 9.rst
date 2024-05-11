=====================================================
Read processing - Bioinformatics (metabarcoding only)
=====================================================

Bioinformatic analysis is typically done using command line, i.e. without graphical user
interfaces (GUIs), and requires several programs (Mathon et al. 2021; Hakimzadeh et. al.
2023). There also exist many pipelines combining the different programs to provide more
user-friendly tools, such as Barque (https://github.com/enormandeau/barque ), Apscale
(https://pypi.org/project/apscale ), Mjolnir (https://github.com/uitmetabarcoding
MJOLNIR), Anapaca (Curd et al. 2019), DADA2 (Callahan et al. 2016) or QIIME2
(Bolyen et al. 2019).

**Here are some examples of pipeline and software tutorials:**

For using different software from read processing to identification of OTUs:
https://learnmetabarcoding.github.io/LearnMetabarcoding/data.html

For using obitools (Boyer et al. 2016)
https://pythonhosted.org/OBITools/wolves.html

For using dada2 (Callahan et al. 2016):
https://benjjneb.github.io/dada2/tutorial.html
https://www.bioconductor.org/packages/devel/bioc/vignettes/dada2/inst/doc/dada2-intro.html

For Find Rapidly OTU with Galaxy Solution (FROGS; Escudié et al. 2018):
http://frogs.toulouse.inra.fr/

**Note:** the list of software and pipelines provided here is far from exhaustive. There is no
consensus on which software nor which settings to use. One should explore which tools and
settings best fit the needs and data for each individual project.

**Merge R1 and R2**

We must merge Read 1 and Read 2 to recover the sequence across the full amplicon. To
do so we usually use the overlap between Read1 and Read2. The overlap can comprise the
full amplicon or be partial. For example, if the amplicon is 400bp and was sequenced using
MiSeq paired-end sequencing 2x250bp, then there is an overlap of 100bp between Read 1 and
Read2 (Figure 22). Merging improves Q scores of the overlap region but if read quality is poor,
erroneous bases could cause chimeras (merging reads that are not the same fragment). Three
parameters must be considered to merge reads: minimum (≥10 bp) and maximum (read
length-minimum overlap length) lengths of acceptable overlap and the maximum rate of
mismatch in the overlap region (e.g. 0.25: 25% mismatches are allowed along the overlapping
region) (Magoč and Salzberg 2011; Mathon et al. 2021). Sequences presenting greater
percentage mismatches will be discarded.

**Note:** If there is no overlap it is possible to concatenate the reads instead of merging them or
to analyse each direction (R1 and R2) separately. Concatenation can be done using the
Cutadapt (Martin 2011) or Pear (Zhang et al. 2014) software packages.
Examples of software: Flash (Magoč and Salzberg 2011), Vsearch (Rognes et al. 2016),
obitools, Pear.

**Examples of software:** Flash (Magoč and Salzberg 2011), Vsearch (Rognes et al. 2016),
obitools, Pear.

Insert Figure 22

**Figure 22.** Calculation of R1 and R2 overlap length.

*Quality and length filtering and primers trimming*

Erroneous sequences from PCR sequencing and merging reads must be filtered out.
Quality-based filtering can be done using different strategies: i) Using a global quality
threshold and filtering out reads below this threshold. However, this is not recommended as
the average Q score is not necessarily a good indicator of the quality of the read; ii) Using a
quality threshold to trim the end of the reads where the quality is generally lower; iii) Using a
number or rate of error. According to the usearch v11 documentation “Quality filtering by
maximum expected errors should be performed as a post-processing step after reads have
been merged in order to take advantage of the re-calculated Phred scores, which should be
better predictions of the true error rates”. We recommend reading the documentation
provided on this website (in the usearch manual) for more information:
`https://www.drive5.com/usearch/manual <https://www.drive5.com/usearch/manual/>`_. The choice of quality threshold is variable
according to the data and should be explored by testing different values (see software
manuals and reference articles). Reads can also be filtered based on their length: usually we
only keep reads that are 20 or 30 bp shorter or longer than the expected size of the amplicon.
The final step is removing primer sequences from the reads.

**Examples of softwares:** Trimmomatic (Bolger, Lohse, and Usadel 2014), usearch (Edgar 2010),
Cutadapt, obitools, Vsearch.

*Dereplication and error removal*

As a single DNA fragment can be sequenced several times, merged reads that passed
the filters must be dereplicated into unique sequences (i.e. identical sequences are grouped).
PCR errors, such as chimeras, must be removed. A chimera is a product of an incomplete
amplicon (aborted elongation during PCR) that was used as a primer for another sequence.
Thus, it contains both forward and reverse primer sequences and is about the same length as
“true” sequences. They can be the product of two incomplete fragments (bimera) or more
(multimera) (Mlaga et al. 2021). The percentage of chimeras (“false” sequences) varies among
datasets (Schloss, Gevers, and Westcott, 2011). They are identified by comparing all
sequences (per sample or using the whole dataset): if it is possible to reconstruct the observed
sequence by combining two more abundant sequences (“parents”), then the sequence is
identified as a chimera.

As errors are likely to occur at low frequencies, it is also possible to filter by read count
(e.g. removing all sequences that occur less than 10 times in the entire dataset). However,
true “sequences” that are rare in the dataset (and potentially at low abundance in the
environment, or at high abundance in the environment but poorly amplified) could be
discarded leading to false negatives (taxa not detected in the final dataset while it was present
in the environment). Thus, depending on the goals of the study and the nature of the data this
step can be relevant or not.

A more advanced method is to use a denoising algorithm which is based on sequence
similarity (composition) and sequence record counts (frequency). For example the obiclean
denoising program (obitools) classifies sequences either as head, internal, or singleton (Box 2)
and only head sequences without any variants with a count greater than 5% of their own count
are kept in the dataset (Mathon et al. 2021). The remaining sequences after denoising are
called Exact Sequence Variants (ESV). ESV can reveal variation in sequences of as little as one
base pair difference.

**BOX 2.** Obiclean (obitools; Boyer et al. 2016) denoising function. A sequence can be tagged
as head, internal or singleton.

Insert Box 2

Some species may be split across several ESVs due to intra-species variation. An
alternative approach to ESV is clustering very similar sequences into a single unit called
Operational Taxonomic Unit (OTU). This way, remaining errors and intra-specific variation are
grouped with true sequences and their influence on the dataset is minimized. The OTU is
represented by the consensus sequence of the cluster whereas the ESV is represented by an
exact sequence. There are multiple clustering algorithms in the literature, but in this manual
we present the most common (1) and the recommended (2) methods (Mathon et al. 2021).

#. Using a global threshold (usually 97 or 98%). The higher the threshold, the lower is the risk of losing diversity by clustering multiple similar species. In addition, the input order changes the OTU construction (Figure 23A).
#. Using a single-linkage clustering approach based on a local clustering threshold (d=1,Mathon et al. 2021) and free of input-order dependency (swarm; Mahé et al. 2015) (Figure 23B).

There is no clear consensus for using the ESV or the OTU approach (Antich et al. 2021);
however, it seems that using ESV is increasingly favoured thanks to improvements in the
denoising algorithms. One can try out different options using positive controls (sample of
known composition) to explore this

**Examples of software:** OBITools, VSEARCH, DADA2, SWARM

Insert Figure 23

**Figure 23.** Clustering methods using A) a global threshold (left), B) a local threshold (right).

*Taxonomic assignment*

The next step in this metabarcoding process is assigning ESV (exact sequence) or OTU
(consensus sequence) to a species name. To do so, ESV/OTU query sequences are compared
to sequences available in reference databases. Reference databases can be public or custom,
global or local (e.g. regional) and must be both accurate (species level) and comprehensive
(cover all species).

*Examples of public reference databases*

- GenBank NCBI (tree of life; all genes) https://www.ncbi.nlm.nih.gov/nuccore/?term=
- BOLD (animal, fungi and plants; COI, ITS, rbcl) http://www.boldsystems.org/index.php/databases
- Silva (Bacteria, Archae, Eukarya; 16S, 18S, 23S, 28S) https://www.arb-silva.de/
- Diat.barcode (diatoms; rbcl) https://www6.inra.fr/carrtel-collection_eng/Barcoding-database
- Midori (eukaryote; multiple genes) http://www.reference-midori.info/index.html
- FROGS Databanks (tree of life; multiple genes) http://genoweb.toulouse.inra.fr/frogs_databanks/assignation/
- EMBL/ENA nucleotide sequence database (tree of life; multiple genes) http://www.ebi.ac.uk/embl/index.html
- PLANiTS (Viridiplantae, ITS) https://github.com/apallavicini/PLANiTS

It is essential to understand that: 1) Available reference data coverage is uneven
among taxa; 2) Reference sequences may have been erroneously identified (misidentification
of the sample, contamination, sequencing error); 3) Incomplete taxonomy and inaccurate
identification (sequences that are identified as 'uncultured', 'environmental', 'sample' in
GenBank NCBI) introduce errors into your dataset; 4) The fewer sequences available for a
group of taxa, the harder it is to spot errors. We recommend reading the following blog post
on best practices to trust species identification
`https://www.ednacollab.org/blog/whats-in-a-name <https://www.ednacollab.org/blog/whats-in-a-name>`_:

#. Barcoding your species of interest makes a world of difference.
#. Curated, regional reference databases outperform global/comprehensive ones.
#. Confidence – Resolution Tradeoffs Abound.
#. Benchmarking your marker of interest is key: one size does not fit all.

That is why it is very important to check unidentified sequences (e.g. ESV/OTU showing a
high number of reads or high frequency of occurrence) and to check taxonomic assignments,
especially unexpected results. Are they false positives (e.g. species not occurring on this
continent), misidentification (e.g. species closely related to one expected in your region or
sample) or true occurrences?

*Basic Local Alignment Search Tool*

Taxonomic identification can be done manually using the online tool Basic Local Alignment
Search Tool (`BLAST <https://blast.ncbi.nlm.nih.gov/Blast.cgi?PROGRAM=blastn&PAGE_TYPE=BlastSearch&LINK_L
OC=blasthome>`_).

- Paste query sequence(s) in the box “Enter accession number(s), gi(s), or FASTA sequence(s)” or upload the FASTA file (multiple sequences)

FASTA format: the first line starts with a “>” and is a comment line containing information on
the sequence (e.g. name, accession number). The second line contains the sequence. Be sure
to use a good text editor so that ‘hidden characters’ do not become embedded in your file.

>Name_for_sequence1
CACCTTATATCTAATCTTCGGTGCTTGAGCTGGCATAGTCGGCACCGCCCTCAGCTTACTCATCCGCGCAGAACT
CGGCCAACCAGGCACACTCCTAGGCGACGACCAAATCTACAACGTAGTCGTCACCGCA
>Name_for_sequence2
CACTCTTTATCTTATTTTTGGTACATGAGCAGGCATAGCCGGTACAGCACTTAGCTTGTTAATCCGCGCAGAACT
AGGACAACCAGGCACCCTCCTAGGAGATGACCAAATTTACAATGTAATTGTCACAGCA
>Name_for_sequence3
CACTCTTTATCTTATTTTTGGTACATGAGCTGGCATAGCCGGTACAGCACTTAGCTTGTTAATCCGCGCAGAACT
AGGATTACCAGGCACCCTCCTACCAGATGACCAAATTTACAATGTAATTGTCACAGCA

- Choose “Nucleotide collection (nr/nt)”
- Click on the “BLAST” button

The BLAST Search Tool provides 100 sequences from the reference database that best
matched the query sequences. The following metrics are provided for each of the matching
sequences: “Description”, “Scientific name”, “Max score”, “Total score”, “Query cover”, “E
value”, “Perc. Ident”, “Acc. Len”, “Accession”. The matching sequences are often called hit
sequences or hits (Figure 24).

Insert Figure 24

**Figure 24.** Example of BLAST output. Sequence is identified as Coturnix sp. (resolution at the
genus level) as both Coturnix japonica and Coturnix coturnix show high query cover (100% and
97%, respectively) and 100% percentage identity.

First check the “Query cover” (QC) value – how much of the query sequence is covered
(i.e. identical) by the hit sequence. For example, a query cover of 90% means that the hit
sequence spans 90% of the query sequence. There is not any threshold value to apply, but a
rule of thumb is QC > 60-80%.

Next, check the “Perc. Ident” (percentage identity), which is how many identical bases the
query and matching sequences share. In other words, it indicates how similar the query and
matching sequences are: the higher Perc. Ident, the higher the similarity between the two
sequences is. However, if “Perc. Ident” is 100% but the QC is low (e.g. 30%), then the hit
sequence is probably wrong and should not be considered. Usually, a percentage identity of
at least 97-98% is used to identify query sequences at the species level. If several species show
high Perc. Ident., then the hit sequence is identified at the nearest shared taxonomic level
(e.g. genus) (Figure 24).

The E value (expected value) indicates the number of expected hits found by chance. The
smaller the E value, the better the hit. E values should not be ≥ 0.01 and an E value < 1e-50
shows very high quality. An E-value of 0.01 means that up to 1% of hits can be expected to be
found by chance.

*Accession* is the unique identifier of the matching sequence. Clicking on the identifier
opens a new window with all information on that sequence (e.g. source, reference, authors,
genes).

*Graphic summary tab*

The query sequence is represented in blue. The length (see Query cover section) and
location of the hit sequences are represented below, each colour indicating the quality of the
alignment (Alignment score; the higher, the better).

*Alignments tab*

This output allows the reader to visualise the alignment between the query sequence
“Query” and the hit sequence “Sbjct”. Select “Pairwise with dots for identities” in the
Alignment view drop-down menu. A dot represents an exact match between “Query” and
“Sbjct”. Sequence ID, Length, E value, Identifier and Gap (%) are also provided above the
alignment.

*Taxonomy tab shows the number of hit sequences per taxonomic identification.*

BLAST is also available as command line software: download a copy of the reference
database and run the software. It is more efficient than the online tool but the reference
database that has been downloaded must be updated frequently as new sequences are added
to the GenBank database every day.

Finally, BLAST of large FASTA files can be done automatically in a friendly graphic
interface using the NCBI BLAST+ tool implemented on the Galaxy server
(`https://usegalaxy.org/ <https://usegalaxy.org/>`_).

On the left sidebar, click:

- Upload Data
- NCBI BLAST +
- NCBI BLAST+ blastn (nucleotide database)

*Final filtering*

Once sequences have been identified, they must be filtered using the no-template
controls, the positive control and the technical replicates. See the “eDNA processing – lab
work: DNA amplification” section above and Glossary for reminders on definitions. There are
several approaches to refine your dataset; we encourage everyone to explore the literature
for more details.

First, we use the no-template controls to assess external and cross-contamination (i.e.
contamination among samples). To do so, we use the maximum number of reads obtained for
an ESV/OTU in the different no-template controls (field, filtration, DNA extraction, PCRs) as a
threshold. A sample is not considered positive for an ESV/OTU if the ESV/OTU shows fewer
reads than its threshold. Note: No-template controls (NTCs) in the same sequencing run are
not considered to be true replicates because we do not expect the same cross-contamination
from one plate to another (sample replicates are on different plates).

We then use the positive control to assess the false-assignment rate of each ESV/OTU.
The false assignment rate is calculated by dividing the maximal number of reads of the nonresident
control in a sample by the total number of reads of the non-resident control. For
example, if we observe a maximum of 4 reads of mole rat (PC non-resident, terrestrial) in a
marine sample and if the total number of reads of mole rat is 20,000 in the run, then the false
assignment rate is 4/20,000=0.0002. The threshold of false assignment rate (Tfa) is assessed
for each ESV/OTU by multiplying the false assignment rate by the total number of reads of the
ESV/OTU.

Finally, we use the technical replicates to filter false positives. We consider a sample to
be positive for an ESV/OTU only if the ESV/OTU is detected in at least two technical replicates
out of three.

Once the data are cleaned, we merge the replicates together.

Example of filtering:

**Table A.** ESV abundance table. Each number represents the number of reads of the ESV in
each sample. The abundance table includes one ESV identified at the species level (ESV_1),
one ESV identified as the non-resident PC species (PC), one sample in triplicates (S1_1,
S1_2, S1_3), two PC samples (PC1, PC2), one NTC for extraction (NTC_ext) and one NTC for
PCR (NTC_PCR).

.. Not a beautiful table

=========  ========  ========  ========  ========  ========  ========  ========
     -       S1_1      S1_2      S1_3       PC1       PC2     NTC_ext   NTC_PCR
=========  ========  ========  ========  ========  ========  ========  ========
  ESV_1      112       7730     48425        0          0        10       100
  ESV_PC      0         1        10         104       73589      0         0
=========  ========  ========  ========  ========  ========  ========  ========

    NTC (no template control): We observe 10 reads of ESV_1 in the NTC of DNA Extraction
    and 100 reads in the NTC of PCR (Table A). Therefore, we subtract 100 reads (max
    number of reads) of ESV_1 in each sample positive to ESV_1 (S1_1, S1_2, S1_3). No
    read of the positive control in the NTCs, so no need to filter the positive control. We
    obtain the Table B below.

*Table B.* ESV abundance table filtered by NTCs.

=========  ========  ========  ========  ========  ========
     -       S1_1      S1_2      S1_3       PC1       PC2
=========  ========  ========  ========  ========  ========
  ESV_1       2         7630    48145        0          0
  ESV_PC      0         1        10         504      73589
=========  ========  ========  ========  ========  ========

- Positive control: We observe 1 read and 10 reads of the positive control in S1_2 and S1_3, respectively. Therefore, the maximum number of reads of the positive control in a sample is 10. The total number of reads of the positive control is 1+10+504+73589 = 74093 reads.

False assignment rate = (max #reads PC) / (total #reads ESV_PC) = 10/74 093 = 0.000135.

Tfa (ESV_1) = (False assignment rate) * (total #reads of ESV_1) = 0.000135 * (2+7630+48145)
= 7 reads. ESV_1 (S1_1) < 7 reads and is therefore considered as 0.

**Table C.** ESV abundance table filtered by NTCs and PC.

=========  ========  ========  ========
     -       S1_1      S1_2      S1_3
=========  ========  ========  ========
  ESV_1       0         7630    48145
=========  ========  ========  ========

- Replicates: ESV_1 shows two positive replicates out of three therefore we consider his detection as true detection in sample 1 (S1).

We can now merge the technical replicates (sum the reads).

**Table D.** Final ESV abundance table (filtered by NTCs, PC and technical replicates).

=========  ========
     -       S1_1
=========  ========
  ESV_1     55775
=========  ========

