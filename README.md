# 5stepTreeAnalysis
The code for the five-step phylogenetic analysis
A five-step phylogenetic analysis was developed by combining percentages and distances for clusters of reported and function-known entries. As illustrated in Fig. S1, the specific steps are listed as follows.
(1) Label the annotated and unannotated peptides, and if it is determined to be an annotated protein, it is marked as "1". Among them, if it is a strong annotation of the six QSP annotations (AgrD, Bacteriocin, Competence, Pheromone, Signal, and Regulator) labeled as “a”, it is a weak label for other annotations as “b”, and the unannotated peptides are labeled as "0". In the analysis of 22,675 QSPs, 10,369 sequences were labeled as "0" due to lack of annotation, while 12,306 sequences were labeled as "1". Among these, 6,325 QSPs were specifically annotated as "a" and 5,981 peptides were annotated as "b".
(2) For each peptide of category "0", start from that node and go up to its smallest branch until there are "1" nodes in the branch.
(3) Calculate the shortest evolutionary distance between the "0" node and different "1" nodes inside the branch.
(4) Identify the similar peptide annotation of the "0" node with the shortest distance to the corresponding "1" node.
(5) Determine the peptide classification of the corresponding “0” node according to strong annotation (“a”) or weak annotation (“b”).
