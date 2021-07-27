#!/bin/bash
#
# Description:
#   Batch write jobs to the database.
#
# History:
#   v1.0  2020-05-07  charles.shih  Init version
#   v1.1  2020-10-14  charles.shih  Get information from logs

set -e

python=python3
executable=./ali_report_write.py
dbfile=../app.db

# User define: begin
testname=check_aliyun_boot_time
imgname=$outer_imgname
branchname=$imgname
pkgver=
bugid=1870090
comments="Instance boot time check."
# User define: end

logpath=/var/www/html/results/iscsi/aliyun/$testname/$imgname
if [ -z "$pkgver" ]; then
	ver=$(find $logpath -type f -name *uname__r_.log | head -n 1 | xargs cat) || exit 1
	pkgver=kernel-$ver
fi
if [ -z "$branchname" ]; then
	branchname=$(echo $imgname | sed 's/.*redhat_\([0-9]\)_\([0-9]\)_.*/RHEL\1.\2/') || exit 1
fi

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
--report_url http://10.73.196.185/results/iscsi/aliyun/${logpath#*aliyun/}/$jobname/$file \
--branch_name $branchname --pkg_ver $pkgver --bug-id $bugid --comments "$comments"

done

exit 0

