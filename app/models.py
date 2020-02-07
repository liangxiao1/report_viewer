from flask import Markup, url_for
from flask_appbuilder import Model
from flask_appbuilder.filemanager import ImageManager
from flask_appbuilder.models.mixins import ImageColumn
from flask_appbuilder.security.sqla.models import User
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Text, Date
from sqlalchemy.orm import relationship

class Report(Model):
    '''
    table for storing ec2 project
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
    test_date =  Column(Date, nullable=True)
    comments = Column(String)

    def __repr__(self):
        return self.log_id

    def result_url(self):
        return Markup(
            '<a href="' +
            self.report_url +
            '">result</a>'
        )

class FailureType(Model):
    '''
    general use: table for specify failure types, eg. product_bug, tool_bug, env_bug
    '''
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(String(150), unique=True, nullable=True)

    def __repr__(self):
        return self.name

class FailureStatus(Model):
    '''
    general use: table for specify failure status, like closed, open, on_qa, verified, blocker
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
    bug_id = Column(Integer,nullable=True)
    bug_title = Column(String(200),nullable=True)
    failure_id = Column(Integer, ForeignKey("failure_status.id"), nullable=False)
    failure_status = relationship("FailureStatus")
    branch_name = Column(String(50),nullable=True)
    comments = Column(Text)
    last_update =  Column(Date)
    create_date =  Column(Date)
    failure_type_id = Column(Integer, ForeignKey("failure_type.id"), nullable=False)
    failure_type = relationship("FailureType")
    identify_keywords = Column(Text)
    identify_debuglog = Column(Text)
    contactor = Column(String(50),nullable=True)

    def __repr__(self):
        return self.log_id

    def bug_url(self):
        if self.bug_id:
            return Markup(
                '<a href="https://bugzilla.redhat.com/show_bug.cgi?id=' +
                str(self.bug_id) +
                '">'+str(self.bug_id)+'</a>'
            )
        else:
            return self.bug_id


class Client(User):
    __tablename__ = "ab_user"
    extra = Column(String(50), unique=True, nullable=False)
