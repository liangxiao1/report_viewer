from flask import Markup, url_for
from flask_appbuilder import Model
from flask_appbuilder.filemanager import ImageManager
from flask_appbuilder.models.mixins import ImageColumn, BaseMixin
from flask_appbuilder.security.sqla.models import User
from sqlalchemy import (Column, ForeignKey, Integer, String, Text, Date, Float,
                        MetaData)
from sqlalchemy.orm import relationship


class EC2_Report(Model):
    '''
    table for storing ec2 project log
    '''
    log_id = Column(Integer, primary_key=True)
    ami_id = Column(String(50))
    instance_type = Column(String(50))
    instance_available_date = Column(Date, nullable=True)
    compose_id = Column(String(50))
    pkg_ver = Column(String(50))
    bug_id = Column(String(50))
    report_url = Column(String)
    branch_name = Column(String(50))
    cases_pass = Column(Integer)
    cases_fail = Column(Integer)
    cases_cancel = Column(Integer)
    cases_other = Column(Integer)
    cases_total = Column(Integer)
    pass_rate = Column(Integer)
    test_date = Column(Date, nullable=True)
    comments = Column(String)
    platform = Column(String(50))
    testrun = Column(String(100))

    def __repr__(self):
        return self.log_id

    def result_url(self):
        print("testrun is {}".format(self.testrun))
        if self.testrun is not None and self.testrun != '' and "None" not in self.testrun:
            self.report_url = url_for('EC2CasePubView.list',_flt_0_testrun=str(self.testrun), _flt_0_instance_type=str(self.instance_type))
            print("testrun is {}".format(self.testrun))
        return Markup('<a href="' + self.report_url + '">result</a>')

class EC2ReportCase(Model):
    '''
    table for storing ec2 project log by casename
    '''
    log_id = Column(Integer, primary_key=True)
    ami_id = Column(String(50))
    instance_type = Column(String(50))
    compose_id = Column(String(50))
    pkg_ver = Column(String(50))
    branch_name = Column(String(50))
    testrun = Column(String(50))
    case_name = Column(String(50))
    case_result = Column(String(50))
    run_time = Column(Float)
    case_debuglog = Column(String)
    test_date = Column(Date, nullable=True)
    component = Column(String(50))
    comments = Column(String)
    failure_id =  Column(Integer)
    platform = Column(String(50))

    def __repr__(self):
        return self.log_id

    def failure(self):
        self.failure_url = None
        if self.failure_id is not None and self.failure_id != '' and "None" not in str(self.failure_id):
            self.failure_url = url_for('BugsPubView.show', pk=str(self.failure_id))
            return Markup('<a href="' + self.failure_url + '">' + str(self.failure_id) + '</a>')
        return Markup(self.failure_id)

    def case_intro(self):
         return Markup('<a href="' + url_for('EC2CaseSourcePubView.list',_flt_0_case_name=str(self.case_name)) + '">intro</a>')

class EC2Case(Model):
    '''
    table for storing ec2 project test cases
    '''
    case_id = Column(Integer, primary_key=True)
    case_name = Column(String(100))
    bugzilla_id = Column(Integer)
    polarion_id = Column(String(50))
    component = Column(String(50))
    priority = Column(Integer)
    maintainer = Column(String(50))
    description = Column(Text)
    key_steps = Column(Text)
    expected_result = Column(Text)
    source_url = Column(String)
    comments = Column(Text)

    def __repr__(self):
        return self.case_id

    def source(self):
         return Markup('<a href="' + self.source_url + '">source</a>')

class AliyunReport(Model):
    '''
    table for storing Aliyun project
    '''
    __tablename__ = 'aliyun_report'
    log_id = Column(Integer, primary_key=True)
    ami_id = Column(String(50))
    instance_type = Column(String(50))
    instance_available_date = Column(Date, nullable=True)
    compose_id = Column(String(50))
    pkg_ver = Column(String(50))
    bug_id = Column(String(50))
    report_url = Column(String)
    branch_name = Column(String(50))
    cases_pass = Column(Integer)
    cases_fail = Column(Integer)
    cases_cancel = Column(Integer)
    cases_other = Column(Integer)
    cases_total = Column(Integer)
    pass_rate = Column(Integer)
    test_date = Column(Date, nullable=True)
    comments = Column(String)
    platform = Column(String(50))

    def __repr__(self):
        return self.log_id

    def result_url(self):
        return Markup('<a href="' + self.report_url + '">result</a>')



class Ali_Report(Model):
    '''
    table for storing Aliyun project
    '''
    log_id = Column(Integer, primary_key=True)
    ami_id = Column(String(50))
    instance_type = Column(String(50))
    instance_available_date = Column(Date, nullable=True)
    compose_id = Column(String(50))
    pkg_ver = Column(String(50))
    bug_id = Column(String(50))
    report_url = Column(String)
    branch_name = Column(String(50))
    cases_pass = Column(Integer)
    cases_fail = Column(Integer)
    cases_cancel = Column(Integer)
    cases_other = Column(Integer)
    cases_total = Column(Integer)
    pass_rate = Column(Integer)
    test_date = Column(Date, nullable=True)
    comments = Column(String)
    platform = Column(String(50))

    def __repr__(self):
        return self.log_id

    def result_url(self):
        return Markup(
            '<a href="' +
            self.report_url +
            '">result</a>'
        )


class AzureReport(Model):
    '''
    Table for Azure RHEL project log
    '''
    __tablename__ = "azure_rhel_report"
    index = Column(Integer, primary_key=True)
    rhel = Column(String(20))
    version = Column(String(50))
    vm_size = Column(String(50))
    automation_tool = Column(String(50))
    result = Column(String(20))
    tests = Column(Integer)
    failures = Column(Integer)
    errors = Column(Integer)
    skipped = Column(Integer)
    failed_cases = Column(String)
    rerun_failed_cases = Column(String)
    duration = Column(Integer)
    finished_time = Column(Date, nullable=True)
    log = Column(String)
    platform = Column(String(20))

    def __repr__(self):
        return self.index

    def log_link(self):
        return Markup('<a href="' + self.log + '">log</a>')



class FailureType(Model):
    '''
    general use: table for specify failure types, eg. product_bug, tool_bug,
                 env_bug
    '''
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(String(150), unique=True, nullable=True)

    def __repr__(self):
        return self.name


class FailureStatus(Model):
    '''
    general use: table for specify failure status, like closed, open, on_qa,
                 verified, blocker
    '''
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(String(150), unique=True, nullable=True)

    def __repr__(self):
        return self.name


class Bugs(Model):
    '''
    general use: table for recording all test failures.
    '''
    id = Column(Integer, primary_key=True)
    test_suite = Column(String(50))
    case_name = Column(String(50))
    bug_id = Column(Integer, nullable=True)
    bug_title = Column(String(200), nullable=True)
    failure_id = Column(Integer,
                        ForeignKey("failure_status.id"),
                        nullable=False)
    failure_status = relationship("FailureStatus")
    branch_name = Column(String(50), nullable=True)
    comments = Column(Text)
    last_update = Column(Date)
    create_date = Column(Date)
    failure_type_id = Column(Integer,
                             ForeignKey("failure_type.id"),
                             nullable=False)
    failure_type = relationship("FailureType")
    identify_keywords = Column(Text)
    identify_debuglog = Column(Text)
    contactor = Column(String(50), nullable=True)

    def __repr__(self):
        return self.log_id

    def bug_url(self):
        if self.bug_id:
            return Markup(
                '<a href="https://bugzilla.redhat.com/show_bug.cgi?id=' +
                str(self.bug_id) + '">' + str(self.bug_id) + '</a>')
        else:
            return self.bug_id


class TestCases(Model):
    '''
    table for store general cases in all project.
    '''
    case_id = Column(Integer, primary_key=True)
    case_title = Column(String)
    case_description = Column(Text)
    case_keycmd = Column(Text)
    ec2_repo = Column(String)
    ec2_casename = Column(String(100))
    ec2_owner = Column(String(50))
    ec2_comments = Column(String)
    azure_repo = Column(String)
    azure_casename = Column(String(100))
    azure_owner = Column(String(50))
    azure_comments = Column(String)
    aliyun_repo = Column(String)
    aliyun_casename = Column(String(100))
    aliyun_owner = Column(String(50))
    aliyun_comments = Column(String)
    openstack_repo = Column(String)
    openstack_casename = Column(String(100))
    openstack_owner = Column(String(50))
    openstack_comments = Column(String)
    esx_repo = Column(String)
    esx_casename = Column(String(100))
    esx_owner = Column(String(50))
    esx_comments = Column(String)
    hyperv_repo = Column(String)
    hyperv_casename = Column(String(100))
    hyperv_owner = Column(String(50))
    hyperv_comments = Column(String)
    create_date = Column(Date, nullable=True)
    last_update = Column(Date, nullable=True)
    create_by = Column(String(50))
    comments = Column(Text)

    def __repr__(self):
        return self.case_id


class Client(User):
    __tablename__ = "ab_user"
    extra = Column(String(50), unique=True, nullable=False)
