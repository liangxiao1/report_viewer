from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.views import ModelView
from flask_appbuilder.widgets import ListBlock, ShowBlockWidget


from . import appbuilder, db
from .models import Report, Bugs

#Below import is for charts
import calendar
from flask_appbuilder.charts.views import (
    DirectByChartView, DirectChartView, GroupByChartView
)
from flask_appbuilder.models.group import aggregate_avg, aggregate_sum, aggregate_count, aggregate

class ReportPubView(ModelView):
    datamodel = SQLAInterface(Report)
    base_permissions = ["can_list", "can_show","menu_access"]
    #list_widget = ListBlock
    #show_widget = ShowBlockWidget

    label_columns = {"result_url": "Result"}

    list_columns = ["log_id", "instance_type", "instance_available_date", "compose_id", "pkg_ver",
"bug_id", "branch_name", "cases_pass", "cases_fail", "cases_cancel",
"cases_other", "cases_total", "pass_rate", "test_date"]
    search_columns = ["log_id", "ami_id", "instance_type", "instance_available_date", "compose_id", "pkg_ver",
"bug_id", "branch_name", "cases_pass", "cases_fail", "cases_cancel",
"cases_other", "cases_total", "pass_rate", "test_date", "comments"]

    show_fieldsets = [
        ("Summary", {"fields": ["log_id", "ami_id", "instance_type", "instance_available_date", "compose_id", "pkg_ver",
"bug_id", "result_url", "branch_name", "cases_pass", "cases_fail", "cases_cancel",
"cases_other", "cases_total", "pass_rate", "test_date", "comments"]}),
        ("Description", {"fields": ["description"], "expanded": True}),
    ]
    #base_order = ("log_id", "asc")
    base_order = ("log_id", "desc")
    #base_filters = [["created_by", FilterEqualFunction, get_user]]


class ReportView(ModelView):
    datamodel = SQLAInterface(Report)
    base_permissions = ["can_list", "can_show","menu_access","can_add","can_edit","can_delete"]
    label_columns = {"result_url": "Result"}
    list_columns = ["log_id", "instance_type", "instance_available_date", "compose_id", "pkg_ver",
"bug_id", "branch_name", "cases_pass", "cases_fail", "cases_cancel",
"cases_other", "cases_total", "pass_rate", "test_date", "comments"]
    search_columns = ["log_id", "ami_id", "instance_type", "instance_available_date", "compose_id", "pkg_ver",
"bug_id", "branch_name", "cases_pass", "cases_fail", "cases_cancel",
"cases_other", "cases_total", "pass_rate", "test_date", "comments"]

    show_fieldsets = [
        ("Summary", {"fields": ["log_id", "ami_id", "instance_type", "instance_available_date", "compose_id", "pkg_ver",
"bug_id", "result_url", "branch_name", "cases_pass", "cases_fail", "cases_cancel",
"cases_other", "cases_total", "pass_rate", "test_date", "comments"]}),
        ("Description", {"fields": ["description"], "expanded": True}),
    ]
    base_order = ("log_id", "desc")

class BugsPubView(ModelView):
    datamodel = SQLAInterface(Bugs)
    base_permissions = ["can_list", "can_show","menu_access"]

    #label_columns = {"bug_url": "BZ#"}

    list_columns = ["id", "test_suite","case_name", "bug_url", "bug_title", "bug_status", "branch_name",
"comments", "last_update","create_date"]
    search_columns = ["id", "test_suite","case_name", "bug_id", "bug_title", "bug_status", "branch_name",
"comments", "last_update","create_date"]

    show_fieldsets = [
        ("Summary", {"fields": ["id", "test_suite","case_name", "bug_id", "bug_title", "bug_status", "branch_name",
"comments", "last_update","create_date"]}),
        ("Description", {"fields": ["description"], "expanded": True}),
    ]
    #base_order = ("log_id", "asc")
    base_order = ("id", "desc")

class BugsView(ModelView):
    datamodel = SQLAInterface(Bugs)
    base_permissions = ["can_list", "can_show","menu_access","can_add","can_edit","can_delete"]

    #label_columns = {"bug_url": "BZ#"}

    list_columns = ["id", "test_suite","case_name", "bug_url", "bug_title", "bug_status", "branch_name",
"comments", "last_update","create_date"]
    search_columns = ["id", "test_suite","case_name", "bug_id", "bug_title", "bug_status", "branch_name",
"comments", "last_update","create_date"]

    show_fieldsets = [
        ("Summary", {"fields": ["id", "test_suite","case_name", "bug_url", "bug_title", "bug_status", "branch_name",
"comments", "last_update","create_date"]}),
        ("Description", {"fields": ["description"], "expanded": True}),
    ]
    #base_order = ("log_id", "asc")
    base_order = ("id", "desc")

def pretty_month_year(value):
    return calendar.month_name[value.month] + " " + str(value.year)

class EC2TestRunChartView(DirectByChartView):
    datamodel = SQLAInterface(Report)
    chart_title = "EC2 Test Per Run"
    chart_type = 'LineChart'

    definitions = [
        {
            "label": "EC2 Pass Rate",
            "group": "test_date",
            "series": [
                "pass_rate"
            ],
        },
        {
            "label": "EC2 Test Per Run",
            "group": "test_date",
            "series": [
                "cases_total",
                "cases_pass",
                "cases_fail",
                "cases_cancel",
                "cases_other",
            ],
        },
#        {
#            "group": "month_year",
#            "formatter": pretty_month_year,
#            "series": [
#                (aggregate_sum, "cases_total"),
#                (aggregate_sum, "cases_fail"),
#            ],
#        },
]


#@aggregate(label='Total diff')
#def aggregate_total(items, col):
#    """
#        Function to count how many diff itmes found.
#        accepts a list and returns the sum of the list's items
#    """
#    col_list = []
#    col_list.append(getattr(item, col) for item in items)
#    #col_set = set(col_list)
#    #print("%s"%items)
#    return len(items)

class EC2TestSumChartView(GroupByChartView):
    datamodel = SQLAInterface(Report)
    chart_title = "EC2 Test Sum"
    chart_type = 'LineChart'

    definitions = [
        {
            "label": "EC2 Test By Day",
            "group": "test_date",
            "series": [
                (aggregate_sum, "cases_total"),
            ],
        },
        {
            "label": "EC2 Test By Instance",
            "group": "instance_type",
            "series": [
                (aggregate_count, "instance_type"),
            ],
        },
        {
            "label": "EC2 Test By Compose ID",
            "group": "compose_id",
            "series": [
                (aggregate_count, "compose_id"),
            ],
        },
    ]


db.create_all()
appbuilder.add_view(ReportPubView, "List avocado-cloud Test Reports", icon="fa-folder-open-o",category="TestReports")
appbuilder.add_view(
    ReportView, "Edit Test Reports", icon="fa-envelope", category="Management"
)
appbuilder.add_view(BugsPubView, "List Know Failures", icon="fa-folder-open-o",category="TestBugs")
appbuilder.add_view(
    BugsView, "Edit Know Failures", icon="fa-envelope", category="Management"
)
appbuilder.add_separator("Management")

#appbuilder.add_view(ProductPubView, "Our Products", icon="fa-folder-open-o")
#appbuilder.add_view(
#    ProductView, "List Products", icon="fa-folder-open-o", category="Management"
#)
#
#appbuilder.add_view(
#    ProductTypeView, "List Product Types", icon="fa-envelope", category="Management"
#)


appbuilder.add_view(
    EC2TestRunChartView, "EC2 Test Per Run", icon="fa-folder-open-o", category="DataAnalyze"
)
appbuilder.add_view(
    EC2TestSumChartView, "EC2 Test Sum", icon="fa-folder-open-o", category="DataAnalyze"
)

#appbuilder.add_view(ReportPubView, "TestReports", icon="fa-folder-open-o", category="TestReports")
#appbuilder.add_separator("TestReports")
#appbuilder.add_view(
#    ReportView, "List avocado-cloud Test Reports", icon="fa-envelope", category="TestReports"
#)
#appbuilder.add_separator("Management")
#appbuilder.add_view(
#    ReportView, "List Test Reports", icon="fa-envelope", category="Management"
#)


