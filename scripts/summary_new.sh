#!/bin/bash
startTime=`date +%Y%m%d-%H:%M`

###parameters
while getopts I:P:G:S:N:O: opt ;
do 
	case $opt in
	I)
	input=$OPTARG
	;;
	P)
	pam=$OPTARG
	;;
	G)
	ref_genome=$OPTARG
	;;
	S)
	species=$OPTARG
	;;
	N)
	num=$OPTARG
	;;
	O)
	outnum=$OPTARG
	;;
	?)
	echo "Wrong parameters"
	exit 1 ;;
esac
done

if [ "$species" = "Human" ];then
	sgRNA_file="/home/lanjie/sgRNA/app/sgRNA_library/9606_exon_prom_ts_sgRNA_clean.fa"
elif [ "$species" = "Mouse" ];then
	sgRNA_file="/home/lanjie/sgRNA/app/sgRNA_library/10090_exon_prom_ts_sgRNA_clean.fa"

#elif [ "$species" = "Rat" ];then
#	sgRNA_file="/home/lanjie/website/mypro/app/sgRNA_library/"
#elif [ "$species" = "Zebrafish" ];then
#	sgRNA_file="/home/lanjie/website/mypro/app/sgRNA_library/"
	
fi

###off-target evaluation
#mkdir /home/lanjie/website/mypro/app/data/off_result


file=$input
fn=$(echo $file|cut -d . -f1)
if [ "${file##*.}" = "txt" ];then
	for line in $(cat $file)
	do
	cat $sgRNA_file|grep ':'$line':' -A 1|grep -v "\--" > $fn'_'$line'_sgRNA.fa'
	python /home/lanjie/sgRNA/app/scripts/clean_sgRNA.py $fn'_'$line'_sgRNA.fa' $fn'_'$line'_sgRNA_clean.fa'
	seqmap 4 $fn'_'$line'_sgRNA_clean.fa' $sgRNA_file  $fn'_'$line'_seqmap_exon_prom.out' /output_all_matches /forward_strand /skip_N /silent /no_fast_index>seq.log
	if [ $? -eq 0 ];then
		echo "Seqmap right"
	else
		echo "Seqmap wrong"
	fi
	python /home/lanjie/sgRNA/app/scripts/get_seqmap_latest.py $fn'_'$line'_seqmap_exon_prom.out' $fn'_sgRNA_off.out' $fn'_sgRNA.out' $num $outnum >error1.log
       # python /home/lanjie/sgRNA/app/scripts/t2html.py $fn'_sgRNA.out' $fn'_result.html'
	
	tar_file=$(echo $fn|cut -d _ -f2)
	tar  czvf $fn'_sgRNA.tar.gz' -C /home/lanjie/sgRNA/app/data/ 'input_'$tar_file'_sgRNA.out' 'input_'$tar_file'_sgRNA_off.out'
	rm $fn'_'$line'_sgRNA.fa'
	rm $fn'_'$line'_sgRNA_clean.fa' 
	rm $fn'_'$line'_seqmap_exon_prom.out'
	rm $fn'_sgRNA_off.out'
	rm $fn'_sgRNA.out'	
	done

elif [ "${file##*.}" = "fa" ];then
	line=$(echo $file | cut -d . -f1) 
        python /home/lanjie/sgRNA/app/scripts/sgdesign.py search --query $line'.fa' --pam $pam --out $line'_sgRNA.txt'>error2.log
        python /home/lanjie/sgRNA/app/scripts/trans_sgRNA.py $line'_sgRNA.txt' $line'_sgRNA.fa'
        seqmap 4 $line'_sgRNA.fa' $sgRNA_file  $line'_seqmap_exon_prom.out' /output_all_matches /forward_strand /silent /skip_N >seq.log
        python /home/lanjie/sgRNA/app/scripts/get_seqmap_latest_ffq.py $line'_seqmap_exon_prom.out' $line'_sgRNA_off.out' $line'_sgRNA.out' $num $outnum
        #python /home/lanjie/sgRNA/app/scripts/t2html.py $line'_sgRNA.out' $line'_result.html'
	tar czvf $fn'_sgRNA.tar.gz' -C /home/lanjie/sgRNA/app/data/ $line'_sgRNA.out' $line'_sgRNA_off.out'
	rm $line'_sgRNA.fa'
	rm $line'_sgRNA.txt'
	rm $line'_seqmap_exon_prom.out'
	rm $fn'_'$line'_sgRNA_off.out' 
	rm $fn'_sgRNA.out' 
fi

endTime=`date +%Y%m%d-%H:%M`
echo "$startTime ---> $endTime"
