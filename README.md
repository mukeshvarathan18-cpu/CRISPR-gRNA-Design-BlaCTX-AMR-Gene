# CRISPR-gRNA-Design-BlaCTX-AMR-Gene
Computational design and validation of guide RNAs (gRNAs) targeting the BlaCTX  antimicrobial resistance gene using Cas9, Cas12, and Cas13

-----------------------------------------------------------------------------------
# CRISPR gRNA Design for BlaCTX AMR Gene
-----------------------------------------------------------------------------------

## What is this project about?
This is a mini project where I designed guide RNAs (gRNAs) targeting the BlaCTX 
antimicrobial resistance gene using three CRISPR-Cas systems — Cas9, Cas12, and Cas13.
The entire analysis was done computationally without any wet lab work.

-----------------------------------------------------------------------------------

## What I did?

1. Downloaded the BlaCTX gene sequence (876 bp) from NCBI GenBank 
   (Accession: CP162271.1, *Kluyvera sichuanensis*)

2. Imported the sequence into SnapGene Viewer for visualization

3. Used CHOPCHOP to design 3 gRNAs for each Cas type:
   - Cas9 uses NGG PAM (20nt gRNA)
   - Cas12 uses TTTV PAM (28nt gRNA)
   - Cas13 uses flexible PFS (28nt gRNA, targets RNA)

4. Annotated all 9 gRNA sites along with their PAM sequences in SnapGene

5. Validated the top gRNA from each Cas type using NCBI BLAST —
   all showed 100% identity to the source organism with zero off-targets


------------------------------------------------------------------------------
## Results
------------------------------------------------------------------------------
- Got the top 3 best gRNA in Cas9, Cas12, Cas13 through CHOPCHOP

------------------------------------------------------------------------------

## Tools Used
- SnapGene Viewer — sequence visualization and annotation
- CHOPCHOP v3 — gRNA design
- NCBI BLAST — specificity validation
- Python (pandas) — data cleaning and table formatting

-------------------------------------------------------------------------------

## What I learned
- How PAM sequences differ across Cas proteins and why it matters
- How to evaluate gRNAs based on on-target efficiency and off-target score
- The difference between Cas9/Cas12 (DNA targeting) and Cas13 (RNA targeting)
- How BLAST is used to confirm gRNA specificity before any wet lab work
