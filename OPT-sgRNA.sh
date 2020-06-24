#!/usr/bin/bash


###help
helpdoc(){
	cat <<EOF

##############################################################################################
Description:

	This is a help document
 	OPT-sgRNA: An User-friendly tool for sgRNA design

Usage:
	sh $0 -I <input> -P <PAM> -G <ref seq> -S <ref species> -N <sgRNAs> -O <sgRNAs>

Option:
	-I this is a input file
	-P this is a given PAM (NGG)
	-S this is a reference genome applied in off-target sites searching
	-N best N sgRNAs with minimum off-target effect
	-O sgRNAs with maximum activity and minimum off-target effect

##############################################################################################

EOF
}
startTime=`date +%Y%m%d-%H:%M`

###parameters
while getopts "hI:P:G:S:N:O:M" opt ;
do 
	case $opt in
	h)
	echo ""
	;;
	I)
	input=`echo $OPTARG`
	;;
	P)
	pam=`echo $OPTARG`
	;;
	G)
	ref_genome=`echo $OPTARG`
	;;
	S)
	species=`echo $OPTARG`
	;;
	N)
	num=`echo $OPTARG`
	;;
	O)
	outnum=`echo $OPTARG`
	;;
	M)
	m=`echo $OPTARG`
	;;
	?)
	echo "Wrong parameters"
	exit 1 ;;
esac
done

if [ $# = 0 ]
then
	helpdoc
	exit 1
fi

if [ "$1" == "-h" ]
then
	helpdoc
	exit 0
fi

if [ "$species" = "Human" ];then
	sgRNA_file="./sgRNA_library/9606_exon_prom_ts_sgRNA_clean.fa"
elif [ "$species" = "Mouse" ];then
	sgRNA_file="./sgRNA_library/10090_exon_prom_ts_sgRNA_clean.fa"

#elif [ "$species" = "Rat" ];then
#	sgRNA_file="/home/lanjie/website/mypro/app/sgRNA_library/"
#elif [ "$species" = "Zebrafish" ];then
#	sgRNA_file="/home/lanjie/website/mypro/app/sgRNA_library/"
	
fi

file=$input
echo "The input file is "$file "and "$num" for activity evaluation, output "$outnum" sgRNAs finally."
fn=$(echo $file|cut -d . -f1)
if [ "${file##*.}" = "txt" ];then
	for line in $(cat $file)
	do
	cat $sgRNA_file|grep ':'$line':' -A 1|grep -v "\--" > $fn'_'$line'_sgRNA.fa'
	python scripts/clean_sgRNA.py $fn'_'$line'_sgRNA.fa' $fn'_'$line'_sgRNA_clean.fa'
	seqmap 4 $fn'_'$line'_sgRNA_clean.fa' $sgRNA_file  $fn'_'$line'_seqmap_exon_prom.out' /output_all_matches /forward_strand /skip_N /silent /no_fast_index>seq.log
	#if [ $? -eq 0 ];then
	#	echo "Seqmap right"
	#else
	#	echo "Seqmap wrong"
	#fi
	#echo $fn'_'$line'_seqmap_exon_prom.out'
	python scripts/get_seqmap_latest.py $fn'_'$line'_seqmap_exon_prom.out' sgRNA_off.out sgRNA.out $num $outnum
        rm $fn'_'$line'_sgRNA.fa'
	rm $fn'_'$line'_sgRNA_clean.fa' 
	rm $fn'_'$line'_seqmap_exon_prom.out'
	done

elif [ "${file##*.}" = "fa" ];then
	line=$(echo $file | cut -d . -f1) 
        python scripts/sgdesign.py search --query $line'.fa' --pam $pam --out $line'_sgRNA.txt'
        python scripts/trans_sgRNA.py $line'_sgRNA.txt' $line'_sgRNA.fa'
        seqmap 4 $line'_sgRNA.fa' $sgRNA_file  $line'_seqmap_exon_prom.out' /output_all_matches /forward_strand /silent /skip_N >seq.log
        python scripts/get_seqmap_latest_ffq.py $line'_seqmap_exon_prom.out' $line'_sgRNA_off.out' $line'_sgRNA.out' $num $outnum

	rm $line'_sgRNA.fa'
	rm $line'_sgRNA.txt'
	rm $fn'_'$line'_seqmap_exon_prom.out'
fi

endTime=`date +%Y%m%d-%H:%M`
echo "$startTime ---> $endTime"
