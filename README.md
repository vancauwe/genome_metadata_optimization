# genome_metadata_optimization
Genome Metadata Optimization for the SDSC

**Why do we need optimization ?** 
DNA sequences are typically represented digitally as text files in FASTA format. This format is simple but contains little metadata. Genomic laboratories frequently work with many different genomes across various projects. Over time the collected sequence data grows into an extensive collection of FASTA files downloaded from diverse sources or edited in-house to reflect mutation. As a result, retrieving what every genome represents and how it was obtained can be challenging.

**Proposed solution**:

Use json metadata collections to ensure fast and easy creation, edit and access to FASTA file metadata. 

This repository is composed of 3 main jupyter notebooks. Two are user oriented and one is an explanation of the reasoning behind the elaboration of this optimization solution.

For all notebooks, if the repository structure is preserved (with *genome_metadata* and its 3 subfolders, *FASTA_files*, *metadata*, and *scripts*), they can be run as such.

**Reasoning explanations:** 
- SDSC_Genome_metadata_storage_optimization:
Here there are ready to run examples. There are also some explanations about conception choices as well as Future possibilities of development of the project.

**User oriented: (user profile, coder or non-coder knowledgeable to run a jupyter notebook)**
- SDSC_New_Metadata:
Here the user can input new metadata for a FASTA file he/she/they have added to the *FASTA_files* folder of the repository. The procedure aims to be self explanatory inside the notebook. It ensures quality checks and standardization of naming.

- SDSC_Edit_Metadata:
Here the user can edit metadata or extract metadata. The edit applies to the naming of the FASTA file, and to changing the values for the different metadata fields. The extract can be performed for an entire metadata or for specific metadata files, fulfilling a criteria. 


