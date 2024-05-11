========
Glossary
========

**Abiotic factor:** non-living (e.g. physical or chemical) facet of the environment

**Absolute quantification:** determination of the exact concentration of a target DNA product
(number of DNA copies/μL)

**Amplicon:** PCR-amplified fragment of DNA, also termed PCR product.

**Amplification biases:** difference in amplification efficiency, for example due to different
affinity of the PCR primers for some species.

**Amplification curve:** a graph of the fluorescence signal versus cycle numbers. Accumulation
curves show a letter “S” shape.

**Barcode:** fragment of DNA used for taxonomic identification of species.

**Bioinformatics:** use of programs and softwares (most often command line tools) to process
raw sequencing data.

**Bioinformatic pipeline:** automated workflow of bioinformatics analyses

**Biotic factor:** living facet of the environment (e.g. micro-organisms)

**Chimera:** artificial DNA sequence originating from the incorrect combination of two sequences
during PCR amplification or Reads merging. Chimera can be filtered out using
bioinformatics.

**Clustering:** bioinformatics step that groups highly similar sequences together (e.g. variants
of a same species and erroneous sequences due to PCR stochasticity) in Operational
Taxonomic Unit (OTU).

**Contamination:** accidental introduction of undesirable DNA in a sample or reaction.
Contaminations can occur at any step (field, filtration, DNA extraction, qPCR/PCR) and
create false positive issues if data are not carefully filtered using no template controls.

**Consensus sequence:** sequence constructed from the most frequent nucleotides at each site
of an alignment of sequences. The alignment of sequences shows which nucleotides are
conserved (always the same nucleotide at a given position) within a species/group of taxa.

**Copy number (amplicon):** the number of copies of a DNA amplicon in a sample

**Cross-contamination threshold:** maximum number of reads obtained for an ESV/OTU in the
different no-template controls. A sample is considered negative to an ESV/OTU if the
ESV/OTU shows less reads in that sample than the threshold.

**Cycle threshold (Ct):** number of qPCR cycles for which the fluorescence generated becomes
higher than the background noise. The Ct value is inversely proportional to the initial
number of target DNA.

**Digital Droplet PCR (ddPCR):** “a method for performing digital PCR that is based on water-oil
emulsion droplet technology. A sample is fractionated into 20,000 droplets, and PCR
amplification of the template molecules occurs in each individual droplet. Following PCR,
each droplet is read to determine the fraction of PCR-positive droplets in the original
sample. These data are then analysed using Poisson statistics to determine the target DNA
template concentration in the original sample.” (definition from the Bio-rad website)

**Denaturing gradient gel electrophoresis (DGGE):** use of an agent to denature the DNA as it
moves across an electrophoresis gel. This makes it possible to distinguish differences in
DNA sequences as they will stop migrating at different positions on the gel.

**DNA extraction:** process of isolating and purifying (e.g. removing RNA, salt and proteins) the
DNA from a sample.

**Efficiency (qPCR):** ratio of the number of target DNA at the end of a PCR cycle divided by the
number of target DNA at the start of the same PCR cycle. Between the Ct and the plateau
of fluorescence, the efficiency is constant cycle-to-cycle. E is calculated using the formula:
EE = 10\ :sup:`-1/slope of the standard curve` - 1. We expect 90% < E < 110%.

**Environmental DNA/RNA:** pool of DNA/RNA isolated from environmental samples such as
sediment, water, air and feces (Pawlowski, Apoth.loz-Perret-Gentil, and Altermatt 2020;
Taberlet et al. 2012). eDNA can be derived from whole organisms (ex: diatoms) or be
captured separately from the organism it originated from (e.g. blood, mucus, faeces, urine,
saliva, shed skin/scales/hair).

**Exact Sequence variant (ESV):** individual sequences that are used for taxonomic assignment.
Erroneous sequences are filtered out using denoising algorithms such as obiclean
implemented in the obitools program. Using ESV is an alternative to clustering into OTUs.
Synonyms are Amplicon Sequence Variant (ASV) and zero-radius OTU.

**False-assignment threshold:** sequences can be mis-assigned (not attributed to the right
sample) due to sequencing itself (i.e. generation of mixed cluster). The false assignment
rate is calculated by dividing the maximal number of reads of the non-resident control in
a sample by the total number of reads of the non-resident control. The non-resident
control is a species that cannot be present on site but is sequenced on the same run than
the samples and other controls. Unexpected presence of the non-resident control in the
samples indicates a sequence assignment error due to sequencing itself. For example, if
we observe a maximum of 4 reads of mole rat (PC non-resident) in a marine sample and if
the total number of reads of mole rat is 20,000 in the run, then the false assignment rate
is 4/20,000=0.0002. The threshold of false assignment (Tfa) is applied to each ESV/OTU by
multiplying its value to the total number of reads of the ESV/OTU. ESV/OTU detection is
considered as TRUE in a sample only if the number of reads in that sample is higher than
the Tfa.

**False positive:** erroneous detection of a taxon in a sample; a species is absent but is detected
as present.

**False negative:** erroneous non-detection of a taxon in a sample; a species is present but is not
detected.

**Filtration:** passage of water samples through a filter to collect the DNA

**Gel electrophoresis:** technique used to separate DNA fragments based on their size. Mix of
DNA and dye is loaded into wells at one end of a gel (e.g. agarose, starch and acrylamide)
and an electric current is applied to make the DNA fragments migrate through the gel.

**High-throughput sequencing (HTS):** sequencing techniques that allow for parallel analysis of
millions of sequences compared to the Sanger sequencing that processes one sequence at
a time.

**Indexing:** allows the multiplexing of samples, by adding a short sequence of nucleotides
(usually 8 or 9 bp) on both ends of each sequence during library preparation (e.g. PCR2 of
the two-step PCR approach). All sequences in a sample have a unique combination of
indices that differs from the other samples. After indexing, hundreds of samples can be
pooled on one HTS run. Sequences are then assigned to the sample they come from after
sequencing using bioinformatics; this is the demultiplexing step.

**Inhibition:** efficiency of the amplification can be reduced by the presence of inhibitors (e.g.
humic acids, tannin, ethanol) in the solution. If inhibitor concentration is too high, the
amplification can fail and lead to a false negative result.

**Intercalation:** phenomenon where ligands (ions, small molecules including proteins) insert
themselves in between base pairs of DNA.

**In silico validation:** computer-based analysis. In an eDNA context, in silico validation of primers
consists of testing the primer sequences against sequences available in reference
databases (e.g. BOLD, NCBI GenBank) that is evaluating the number of mismatches
between the primer sequences and the sequences of the target species.

**In vitro validation:** laboratory analysis. In eDNA context, in vitro validation of primers consists
in testing the primers against DNA (e.g. species of interest DNA, mock community DNA).

**Library:** for our purposes, DNA prepared for sequencing on a High Throughput Sequencing
platform.

**Limit of detection (LOD):** assessment of the assay sensitivity:** the limit of detection is the
lowest concentration of target DNA that produces positive replicates (detection/ non-detection criteria).

**Limit of quantification (LOQ):** assessment of the assay capability to precisely quantify the copy
number of the target species in a sample.

**Lysis buffer:** solution that disrupts cell membranes, causing the release of cellular and
organellar contents (DNA).

**Metabarcoding:** simultaneous taxonomic identification of multiple species in a sample using
DNA sequences of a short, variable focal region of the genome.

**Metadata:** supplementary data associated with an observation or sample providing more
information (e.g. sex, age, water chemistry).

**Mock community:** in eDNA studies, a mixture of DNA of species of known composition

**Negative control:** sample collected from a site where the target species is known to be absent
to check for contamination. While it is different from “No template control” (see definition
below) both terms are often used interchangeably.

**No template control (NTC):** DNA-free sample (i.e. only reagents) used to check for
contaminations. NTC should be included at each step of eDNA-based studies. For example,
filtration NTC will be distilled water filtered alongside the eDNA samples to check that
there is no cross contamination between samples (DNA transferred from one sample to
another by contamination of the equipment). DNA extraction NTC, PCR NTC, qPCR NTC
and ddPCR NTC will be DNA-free reagents.

**Operational Taxonomic Unit (OTU):** cluster of highly similar reads.

**Polymerase chain reaction (PCR):** creating copies of a fragment of the total DNA. The reaction
is carried out thanks to primers that target (flank) the fragment to be amplified and a PCR
mix made of polymerase, buffer, nucleotides, sterile water, and DNA template. PCR phases
are denaturation, annealing and extension. At each cycle the amount of amplicon doubles
(exponential amplification). The cycles are repeated between 30 and 40 times to obtain
millions of DNA molecules.

**Polymerase:** enzyme that catalyzes the synthesis of DNA or RNA

**Positive control:** sample that is known to produce a positive result. It allows evaluation
whether the process (e.g. PCR) is working as it should.

**Precipitation:** use of ethanol or other agent to precipitate DNA in the water sample

**Primers:** short sequences (~20bp) that match the target fragment of DNA (barcode). Two
primers - one at each end of the barcode (forward and reverse) - are necessary for
amplification.

**Quantitative PCR (qPCR):** PCR reaction that records in real time the accumulating DNA
sequences during amplification through the continuous measurement of a fluorescence
signal incorporated in the DNA.

**Reads:** sequences produced by sequencing - usually in reference to high throughput, massively
parallel sequencing

**Reference database:** repository containing the DNA sequences of taxa with valid taxonomic
identification. The most extensive public reference databases are NCBI’s Genbank
(although not curated, so contains a lot of errors) and the Barcode of Life Database (BOLD).
The latter was specifically developed to provide a clean and extensive database (~10M of
sequences available, ~237k animal species, 70k plant species, 24k fungi and other species)
for DNA barcoding but is limited to a few genes.

**Repeatability:** an experiment is considered repeatable if, by replicating the same experiment
with the same parameters, the same results are produced.

**Replicability:** consistent results are obtained across studies (parameters can be different)

**Replicate (sample):** samples collected at the same location and same time

**Replicate (technical):** same sample processed several times independently. For example, PCR
triplicates means that three PCRs have been run on the same sample to account for PCR
stochasticity.

**Secondary structure (primers):** interactions between bases that bind to each other. Primer
dimers are primer sequences that bind to each other instead of binding to DNA template.
Hairpin loops are created by complementary regions on primer sequences.

**Sequencing:** determination of the nucleotide sequence of an amplicon.

**Specificity (primers):** specific primers must bind to the target species only. Specificity can be
improved by maximizing the number of mismatches between the primer sequences and
the non-target species, and/or by increasing the annealing temperature of the PCR/qPCR.

**Shotgun sequencing:** shotgun sequencing determines the DNA sequence of an organism
genome by randomly breaking up a genome into fragments and sequencing all of them,
whereas metabarcoding sequencing determines the DNA sequence of a specific short
genomic region of DNA.

**SYBR green:** SYBR Green intercalates the fluorescent dye between double-stranded DNA
strands as they anneal. Specificity relies on primers and annealing temperature.

**Taqman probe:** ~20bp sequence that binds to the DNA fragment between the two primer
sequences. The probe is labelled with a quencher on its both ends and a fluorescent
reporter during extension, the quencher is cleaved out enabling the emission of the
fluorescence signal. Specificity relies on primers, probe, and annealing temperature.

**Temperature gradient gel electrophoresis (TGGE):** use of a temperature gradient to denature
the sample DNA as it moves across an electrophoresis gel. This makes it possible to
distinguish differences in DNA sequences as they will stop migrating at different positions
on the gel.