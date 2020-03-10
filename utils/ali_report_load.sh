#!/bin/bash

set -e

imgname=redhat_8_1_x64_20G_alibase_20200110.vhd

pushd /var/www/html/results/iscsi/aliyun/$imgname/
jobname_list=$(ls -d job-*)
popd

jobname=job-2020-02-14T10.55-da1a175

for jobname in $jobname_list; do
	echo $jobname
	[ -e /var/www/html/results/iscsi/aliyun/$imgname/$jobname/results.html ] && report=results.html || report=job.log
	python3 ./ali_report_write.py --dir /var/www/html/results/iscsi/aliyun/$imgname/$jobname/ \
		--report_url http://10.73.196.185/results/iscsi/aliyun/$imgname/$jobname/$report \
		--branch_name RHEL8.1 --pkg_ver kernel-4.18.0-147.3.1.el8_1.x86_64 --bug-id 1802393 \
		--compose-id $imgname --comments image_validation --db_file ../app.db
done

exit 0

