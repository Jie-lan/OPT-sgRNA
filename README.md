# OPT-sgRNA
A user-friendly tool for single-guide RNA (sgRNA) design of CRISPR-Cas system

## Motivation 
The CRISPR/Cas9 system is currently considered as the most advanced tool used for numerous areas of biological study in which it is useful to target or modify specific DNA sequences. However, low on-target cleavage efficiency and off-target effects impede its wide application. Therefore, screening of sgRNAs with maximum on-target activity and minimum potential off-target effects is a glorious but challenging task. Although much progress has been made for the sgRNA design and evaluation, very few tools which could implement both on-target activity and off-target effect evaluation are available. Here, we present a new computational tool to combine off-target prediction and on-target activity evaluation. Here, with public large-scale CRISPR screen data, we evaluated contribution of different features influence sgRNA activity and off-target effects, and developed models for sgRNA off-target evaluation and on-target activity prediction. In addition, we combined both activity and off-target prediction models and packaged them as an online sgRNA design tool, OPT-sgRNA. 
## Highlights
  Provide web services for computer-aided design of sgRNA with minimal off-target and maximal activity potentials.   
  Provide standalone Linux command version for more comprehensive application.  
  Provide prepared sgRNA library for CRISPR-screen (spyCas9), including Human (GRCh38.p12), Mouse (GRCm38.p6), Zebrafish (GRCz11) etc.



## A General View of OPT-sgRNA
#### Main command
<pre><code> Usage:
        OPT-sgRNA -I <input> -P [PAM] -G [ref seq] -S [ref species] -N [sgRNAs] -O [sgRNAs]

Option:
        -I this is a input file
        -P this is a given PAM (NGG)
        -S this is a reference genome applied in off-target sites searching
        -N best N sgRNAs with minimum off-target effect
        -O sgRNAs with maximum activity and minimum off-target effect
Example:
OPT-sgRNA -I t.txt -P NGG -S Human -N 100 -O 10

cat t.txt
CD18A

</pre></code>


## Prerequisites
The following software and libraries are additionally required:
  Seqmap (1.0.12)  
  Python (>2.7)  
  RNAfold (2.4.3)  
