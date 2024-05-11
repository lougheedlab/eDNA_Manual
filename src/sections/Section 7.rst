================================================
Overview of eDNA multi-species detection methods
================================================

Simultaneous multispecies detection from isolated DNA emerged from traditional
methods for DNA barcoding single species and from the use of DNA sequences for
phylogenetic reconstruction, phylogeography, and population genetics. Though it has been
known that species can be distinguished using DNA sequences (for animals primarily
mitochondrial genes) since the 1980s, the simultaneously identification of multiple species
using single variable region of the genome really can be traced to the influential 2003
Proceedings of the Royal Society paper by Paul Herbert and colleagues (Hebert et al. 2003 -
cited over 15,000 times as of April 2024), although the notion of conserved primers dates to
at least 1997 (Zhang and Hewitt 1997). For animals, mitochondrial DNA has remained the
focus for multispecies detection methods because of typically much higher copy number per
cell than nuclear DNA, usually uniparental inheritance (although some taxa like bivalves have
biparental inheritance), and limited recombination with high interspecific variation and
reasonably low intraspecific variation enabling species level identification. DNA barcoding
originally focused on cytochrome oxidase 1 (COI) gene for species detection and was the
foundation for global efforts to barcode all life (e.g. the International Barcode of Life
Consortium); however, the COI gene has proved insufficiently variable for some animal
groups, and for non-animal taxa and other genes are used for these taxa; rcbl and matK for
plants, inter-transcribed spacer (ITS) for fungi, 12S ribosomal gene for fish (Hollingsworth et
al., 2009; Miya et al., 2015). After Taberlet’s publication in 2012, the application of conserved
primers in environmental samples became an increasingly sought-after technique, with over
1000 articles published using the term “eDNA metabarcoding” in 2023 alone (Taberlet et al.,
2012; Figure 10). Advances in sequencing technologies facilitated the emergence of the
simultaneous detection of multiple species within a single assay and the ability to screen
hundreds of samples simultaneously using High Throughput Sequencing (HTS) (Slatko et al.,
2018; Garlapati et al., 2019) - note that Next Generation Sequencing (NGS) is a phrase that is
sometimes used but has fallen out of favour as the field is moving so quickly. We discuss two
classes of HTS tools that are often applied to eDNA, DNA metabarcoding and metagenomics.
These approaches generate billions of individual sequences, called ‘reads’. We focus on
metabarcoding for multispecies detection in this manual but will first briefly touch on
metagenomics and its applications to provide some context.

Metagenomics and shotgun sequencing
===================================

Metagenomics allows the analysis of all genomic material within an environmental or
clinical sample, capable of providing taxonomic and functional characterization of entire biotic
communities - typically of microorganisms. Most microorganisms simply cannot be cultured
using current protocols and the ability to identify microbial taxa using DNA sequences really
has revolutionised our understanding of biology including community and functional diversity
in nature. Broadly there are two classes of metagenomic sequencing: targeted sequencing of
a single genic region (usually 16S rRNA) and metagenomic shotgun sequencing (Mendoza et
al., 2015). 16S rRNA gene sequencing is favoured for analyses of bacterial communities
exploiting the evolutionary stability of the 16S gene over vast spans of time, its ubiquity, and
its relatively large size (1,500bp) that provides sufficient sequence data to differentiate among
species within a sample (Janda and Abbott, 2007; Mishra et al., 2021). In shotgun sequencing
all genomic material in a sample, irrespective of taxon or locus, is sequenced. Shotgun
sequencing has been widely applied to assessing microbial diversity and eDNA of
microorganisms is typically abundant in nature or in clinical samples (e.g. gut); however,
challenges do emerge of taxa of interest are rare and the signature of their presence more
difficult to detect. With ever increasing sequencing depth available from HTS technologies,
this is becoming less of an issue (Garlapati et al., 2019). There are a few key benefits to eDNA
metagenomics, notably no need for targeting primers and PCR amplification, and thus no need
to find conserved regions for focal groups nor the biases that can occur with primer binding.
Further, as this approach sequences environmental samples directly, PCR amplification biases
and the resulting skew in number(s) of read counts is less of an issue, meaning that number
of reads for a given taxon may be closer in proportion to its actual presence in the original
sample. Though shotgun sequencing removes PCR biases common to DNA metabarcoding, the
taxonomic identification and resolution remains challenged by incomplete reference
databases and intraspecies variation in genomic and organellar DNA (Singer et al., 2020).

Insert Figure 10

**Figure 10.** Bar chart depicting the number of publications using the terms “eDNA
Metabarcoding” found in Google scholar each year since the term was introduced in 2012.
Data accessed on April 18, 2024.

DNA Metabarcoding
=================

manual are mostly focused on single species/taxon detections with the caveat that one can
multiplex multiple primer pairs to assay a relatively limited number of taxa simultaneously.
The detection and identification of multiple species using eDNA extracted from an
environmental sample can be done using DNA metabarcoding (Deiner et al. 2017).
Metabarcoding can also be used for other scenarios including bulk specimens collected
together (e.g. using Malaise trap) ('community DNA'; Kirse et al. 2021). Metabarcoding has
been successfully used for diet analysis of carnivores, insectivores, omnivores and herbivores
(Ando et al. 2020), as well as surveys of plant and animal richness in freshwater, marine, and
terrestrial ecosystems (Ruppert, Kline, and Rahman 2019). Comparisons of data from eDNA
metabarcoding and conventional sampling (e.g. gillnet, pitfall traps, acoustic, electrofishing)
in various ecosystems have revealed that eDNA metabarcoding is typically either more
sensitive (i.e. higher richness and/or taxonomic resolution) or at worst complementary to
traditional sampling, often detecting taxa not captured in traditional surveys (Milla et al. 2022;
Hallam et al. 2021; Keck et al. 2021; Nørgaard et al. 2021; Maracle et al. 2024).

In DNA metabarcoding, short fragments (i.e. DNA barcodes) of a single target gene for
an environmental sample are amplified using a “single PCR”, a “two-steps PCR” or a “tagged
PCR” method. Once amplified, amplicons are sequenced on a high throughput sequencing
platform such as Illumina, Oxford Nanopore or Roche 454. In this manual, we focus on the
two-step PCR method as it is most commonly-used and is cost-effective for the analysis of
large numbers of samples. Technical aspects of each method are detailed in Bohmann et al.
(2021) wherein there is also a useful summary (8.2. Amplicon library preparation). Briefly, in
the first PCR-based amplification (PCR1), using conserved DNA primer pairs, amplicons of the
focal DNA barcode region for multiple species are amplified in millions of copies. The second
PCR (PCR2, dual indexation) adds multiplexing indices (a “molecular label”, unique
combination per sample) at both ends of each PCR1 product (Figure 11). For example, using
the 32 i5 and 48 i7 indices from Kozich et al. (2013), it is possible to multiplex up to 1,536 PCR1
products within the same Illumina MiSeq run (MiSeq is one of the many Illumina platforms
usually used for smaller scale projects) and therefore to multiplex several hundred samples
and including several technical replicates per sample (Galan et al. 2018) – note that a technical
replicate is simply a repeated assay of the same sample to assess amplification or other
methodological biases. After sequencing, reads (sequenced DNA fragments) are processed to
filter out contamination, remove low quality reads, and reads caused by PCR and sequencing
errors. Clean data are then compared to sequences available in reference databases to assign
species identity. The final output is a read abundance table with the number of reads for each
taxa in each sample.

eDNA metabarcoding provides invaluable information and can be used to assess biotic
community richness and species composition in space and time. Generally the number of
reads for a particular taxon cannot be interpreted as representing abundance because
multiple factors in the field and laboratory can influence the number of reads (e.g. difference
in eDNA shedding between species, DNA extraction efficiency, PCR primer biases among
species, data cleaning procedures) (Deiner et al. 2017; Lamb et al. 2019). For example, a metaanalysis
of mock community (artificial array of DNA from multiple species) metabarcoding
studies showed high variance of the quantitative performance among studies (relationship
between the proportion of reads and the amount of input material) (Lamb et al. 2019). eDNAbased
metabarcoding studies (i.e. using samples from nature) are probably even more biased
than mock communities because of myriad other factors (e.g. PCR inhibitors), thus precluding
consistent and strong relationships between read numbers and species abundances using
metabarcoding. One simple way to address this issue is simply to convert the number of reads
to presence/absence. Note that this can inflate the importance of a rare taxa in a sample
(Deagle et al. 2018). Alternative practices include transforming the data into frequency of
occurrence (FOO = % of samples that contain a given taxon) or relative read abundance data
(RRA; assumes that the abundance of a taxa is proportional to its sequence read) (Deagle et
al. 2018). In some cases correlation between biomass and relative read abundance has been
shown (Schenk et al. 2019), but it is currently not possible to link the number of reads to the
number of individuals in all scenarios.

Insert Figure 11.

**Figure 11.** Two-step PCR workflow.

