import os

__author__ = "zhongyin zhang "
__version__ = "0.0.0.1"
import time


class Template_mixin:
    display_HTML_PLATE = """<?xml version="1.0" encoding="UTF-8"?>
                    <html xmlns="http://www.w3.org/1999/xhtml">
                    <head>
                        <title>周报</title>
                        <meta name="generator" content="HTMLTestRunner 0.8.2.2"/>
                        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
                        <link href="http://libs.baidu.com/bootstrap/3.0.3/css/bootstrap.min.css" rel="stylesheet">
                        <script src="http://libs.baidu.com/jquery/2.0.0/jquery.min.js"></script>
                        <script src="http://libs.baidu.com/bootstrap/3.0.3/js/bootstrap.min.js"></script>

                    <style type="text/css" media="screen">
                    body        { font-family: Microsoft YaHei,Tahoma,arial,helvetica,sans-serif;padding: 20px; font-size: 80%; }
                    table       { font-size: 100%; }
                    /* -- heading ---------------------------------------------------------------------- */
                    .heading {
                        margin-top: 2px;
                        margin-bottom: 1ex;
                    }

                    </style>

                    </head>
                    </head>
                    <body >
                    <div class='heading'>
                    <h1>测试总结:</h1>
                    </div>

                    <div style="width: 80%; display:none" >
                        <table id='result_table' class="table table-condensed table-bordered table-hover">
                            <tr id='header_row' class="text-center success" style="font-weight: bold;font-size: 14px;">

                            </tr>
                    """
    HTML_PLATE = """<?xml version="1.0" encoding="UTF-8"?>
                    <html xmlns="http://www.w3.org/1999/xhtml">
                    <head>
                        <title>周报</title>
                        <meta name="generator" content="HTMLTestRunner 0.8.2.2"/>
                        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
                        <link href="http://libs.baidu.com/bootstrap/3.0.3/css/bootstrap.min.css" rel="stylesheet">
                        <script src="http://libs.baidu.com/jquery/2.0.0/jquery.min.js"></script>
                        <script src="http://libs.baidu.com/bootstrap/3.0.3/js/bootstrap.min.js"></script>

                    <style type="text/css" media="screen">
                    body        { font-family: Microsoft YaHei,Tahoma,arial,helvetica,sans-serif;padding: 20px; font-size: 80%; }
                    table       { font-size: 100%; }
                    /* -- heading ---------------------------------------------------------------------- */
                    .heading {
                        margin-top: 2px;
                        margin-bottom: 1ex;
                    }

                    </style>

                    </head>
                    </head>
                    <body >
                    <div class='heading'>
                    <h1>测试总结:</h1>
                    </div>

                    <div style="width: 80%; ">
                        <table id='result_table' class="table table-condensed table-bordered table-hover" >
                            <tr id='header_row' class="text-center success" style="font-weight: bold;font-size: 14px;">

                            </tr>
                    """
    tester_html = """        <tr class="text-center success" style="font-weight: bold;font-size: 14px;">
            <th colspan="3" style="width: 100%; text-align: center;background: #5bc0de61">测试工作分配及内容</th>
        </tr>
        <tr style="text-align: center">
            <td>测试人员</td>
            <td>测试内容</td>
            <td>测试进度</td>
        </tr>

        """

    tester_tr = """<tr>
                    <td>%(tester)s</td>
                    <td>%(test_content)s</td>
                    <td>%(progress)s</td>
                </tr>"""

    local_bug_html = """       <table id='result_table' class="table table-condensed table-bordered table-hover" >
                        <div>
                        <th colspan="9" style="width: 100%; text-align: center;background: #5bc0de61">本地bBUG情况</th>
                    </tr>
                    <tr style="text-align: center"> 
                    <td>需求总数</td>
                    <td>本地bug总数</td>
                    <td>本地无效bug数</td>
                    <td>本地有效bug数</td>
                    <td>本地一般bug数</td>
                    <td>本地严重bug数</td>
                    <td>本地致命bug数</td>
                    <td>本地历史遗留bug数</td>
                    <td>本地挂起bug数(附带bug挂起链接)</td>
                    </tr><tr>                   
        </tr>"""

    line_bug_html = """       <table id='result_table' class="table table-condensed table-bordered table-hover" >
                        <div>
                        <th colspan="9" style="width: 100%; text-align: center;background: #5bc0de61">线上bBUG情况</th>
                    </tr>
                    <tr style="text-align: center"> 
                    <td>需求总数</td>
                    <td>线上bug总数</td>
                    <td>线上无效bug数</td>
                    <td>线上有效bug数</td>
                    <td>线上一般bug数</td>
                    <td>线上严重bug数</td>
                    <td>线上致命bug数</td>
                    <td>线上历史遗留bug数</td>
                    <td>线上挂起bug数(附带bug挂起链接)</td>
                    </tr><tr>                   
        </tr>"""

    local_bug_tr = """<tr>
                    <td>%(demand_sum)s</td>
                    <td>%(bug_sum)s</td> 
                    <td>%(invalidBug_sum)s</td> 
                    <td>%(effectivityBug_sum)s</td> 
                    <td>%(ordinaryBug_sum)s</td> 
                    <td>%(severityBug_sum)s</td> 
                    <td>%(deadlyBug_sum)s</td> 
                     <td>%(leaveBug_sum)s</td> 
                      <td>%(bug_link)s</td> 
                </tr>"""

    bug_end = """       </div>
                    </table>"
                        </div>
                    </table>"""

    summary_html = """
    					<div><p>
    					"""
    summary_div = """{}"""

    end_summary = """</p>
                    </div>
                        """

    END_HTML = """          </el-collapse-item>
                        </table>
                    </div>

                        <div id='ending'>&nbsp;</div>
                            <div style=" position:fixed;right:50px; bottom:30px; width:20px; height:20px;cursor:pointer">
                            <a href="#"><span class="glyphicon glyphicon-eject" style = "font-size:30px;" aria-hidden="true">
                            </span></a>
                        </div>

                    </body>
                    </html>"""


class ReportTest(Template_mixin):
    def __init__(self, receive_data):

        self.tester = receive_data["job_content"]
        self.local_bug = receive_data["localbugList"]
        self.line_bug = receive_data["linebugList"]
        self.summary = receive_data['summary'].replace("\n","</p><p>")
        self.on = receive_data['on']

    def html_PLATE(self):
        if self.on is True:
            return self.HTML_PLATE
        else:
            return self.display_HTML_PLATE

    def write_tester_html(self):
        return self.tester_html

    def write_local_bug_html(self):
        return self.local_bug_html

    def write_line_bug_html(self):
        return self.line_bug_html

    def write_bug_end(self):
        return self.bug_end

    def wtrte_summary_html(self):
        return self.summary_html
    def write_end_summary(self):
        return self.end_summary


    def tester_tr_data(self):
        tester = []
        for i in self.tester:
            tester_html = self.tester_tr % dict(tester=i['user'],
                                                test_content=i['content'],
                                                progress=i['progress'],
                                                )
            tester.append(tester_html)
        return tester

    def local_bug_tr_data(self):
        bug = []
        for i in self.local_bug:
            bug_html = self.local_bug_tr % dict(demand_sum=i['demand_sum'],
                                                bug_sum=i['bug_sum'], invalidBug_sum=i['invalidBug_sum'],
                                                effectivityBug_sum=i['effectivityBug_sum'],
                                                ordinaryBug_sum=i['ordinaryBug_sum'],
                                                severityBug_sum=i['severityBug_sum'],
                                                deadlyBug_sum=i['deadlyBug_sum'],
                                                leaveBug_sum=i['leaveBug_sum'],
                                                bug_link=i['bug_link'],
                                                )
            bug.append(bug_html)
        return bug

    def line_bug_tr_data(self):
        bug = []
        for i in self.line_bug:
            bug_html = self.local_bug_tr % dict(demand_sum=i['demand_sum'],
                                                bug_sum=i['bug_sum'], invalidBug_sum=i['invalidBug_sum'],
                                                effectivityBug_sum=i['effectivityBug_sum'],
                                                ordinaryBug_sum=i['ordinaryBug_sum'],
                                                severityBug_sum=i['severityBug_sum'],
                                                deadlyBug_sum=i['deadlyBug_sum'],
                                                leaveBug_sum=i['leaveBug_sum'],
                                                bug_link=i['bug_link'],
                                                )
            bug.append(bug_html)
        return bug

    def summary_h5_data(self):
        summary = []
        data = self.summary_div.format(self.summary)
        summary.append(data)
        return summary

    # ========================================

    def end_HTML(self):
        return self.END_HTML


class WriteSummarHtml(ReportTest):
    def __init__(self, receive_data):
        super().__init__(receive_data)

    def write_HTML(self):
        now = time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime(time.time()))
        local_path = os.getcwd()
        report_file_path = local_path + '/TesterRunner/static/reports/'

        file_name = report_file_path + now + ".html"

        f = open(file_name, "w", encoding="utf-8")
        f.write(self.html_PLATE())
        f.write(self.write_tester_html())
        for i in self.tester_tr_data():
            f.write(i)
        f.write(self.write_local_bug_html())
        for i in self.local_bug_tr_data():
            f.write(i)
        f.write(self.write_line_bug_html())
        for i in self.line_bug_tr_data():
            f.write(i)

        f.write(self.write_bug_end())
        f.write(self.wtrte_summary_html())
        for i in self.summary_h5_data():
            f.write(i)
        f.write(self.write_end_summary())

        f.write(self.end_HTML())

        return now + ".html"


# if __name__ == '__main__':
#     a = {'summary': '测试总结:\n1.account is me!\n2.this my house!',
#          'on': True,
#          'testing_time': '2019-09-30T16:00:00.000Z',
#          'job_content': [
#              {'problem_description': '',
#               'cause': '',
#               'Severity': '',
#               'Responsible': '',
#               'address': '',
#               'user': ['郑润生'],
#               'content': '今天测试完成了',
#               'progress': '完成了'}],
#          'linebugList': [
#              {'demand_sum': '188',
#               'bug_sum': '88',
#               'invalidBug_sum': '8',
#               'effectivityBug_sum': '2345',
#               'ordinaryBug_sum': '542',
#               'severityBug_sum': '3212',
#               'deadlyBug_sum': '4122',
#               'leaveBug_sum': '22',
#               'bug_link': 'http://ww.baidu.com'}
#          ],
#          'localbugList': [
#              {'demand_sum': '11', 'bug_sum': '2', 'invalidBug_sum': '2',
#               'effectivityBug_sum': '2', 'ordinaryBug_sum': '2', 'severityBug_sum': '2',
#               'deadlyBug_sum': '2', 'leaveBug_sum': '2', 'bug_link': 'http://ww.baidu.com'}
#          ],
#          't_date': '2019/10/01 00:00:00'}
#     write = WriteHtml(receive_data=a)
#     print(write.write_HTML())
