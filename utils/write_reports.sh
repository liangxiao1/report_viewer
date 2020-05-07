#!/bin/bash
#
# Description:
#   Batch write jobs to the database.
#
# History:
#   v1.0  2020-05-07  charles.shih  Init version

set -e

python=python3
executable=./ali_report_write.py
dbfile=../app.db

logpath=/var/www/html/results/iscsi/aliyun/ebm_validation_with_rhel7u7/
imgname=rhel_7_7_64_20G_alibaba_20190830.vhd
branchname=RHEL7.7
pkgver=kernel-3.10.0-1062.el7.x86_64
bugid=1823190
comments="EBS validation with RHEL7.7"

# get jobs
pushd $logpath
logpath=$(pwd)
jobname_list=$(ls -d job-*)
popd

for jobname in $jobname_list; do
	# show details and ask for uploading
	echo "===================="
	echo "JOB NAME   : $jobname"
	echo "IMAGE NAME : $imgname"
	echo "LOG PATH   : $logpath"
	echo "BRANCH NAME: $branchname"
	echo "PACKAGE VER: $pkgver"
	echo "BUG ID     : $bugid"
	echo "COMMENTS   : $comments"
	read -t 30 -p "Write above job into report database? [y/N] (in 30s) " answer
	echo
	if [ "$answer" != "Y" ] && [ "$answer" != "y" ]; then
		echo "Abort!"
		continue
	fi

	# write the job into database
	[ -e $logpath/$jobname/results.html ] && file=results.html || file=job.log
	$python $executable --dir $logpath/$jobname/ --db_file $dbfile --compose-id $imgname \
--report_url http://10.73.196.185/results/iscsi/aliyun/$(basename $logpath)/$jobname/$file \
--branch_name $branchname --pkg_ver $pkgver --bug-id $bugid --comments "$comments"

done

exit 0

