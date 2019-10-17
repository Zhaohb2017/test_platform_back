import os

__author__ = "zhongyin zhang "
__version__ = "0.0.0.1"
import time


class Template_mixin:
    HTML_PLATE = """<?xml version="1.0" encoding="UTF-8"?>
                    <html xmlns="http://www.w3.org/1999/xhtml">
                    <head>
                        <title>测试报告</title>
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
                    <h1>版本测试报告</h1>
                    </div>

                    <div style="width: 50%; ">
                        <table id='result_table' class="table table-condensed table-bordered table-hover" >
                            <tr id='header_row' class="text-center success" style="font-weight: bold;font-size: 14px;">
                                <th colspan="6" style="width: 30%; text-align: center;background: #00a647">版本测试报告</th>
                            </tr>
                    """
    VER_HTML = f"""<tr>
                        <th>版本名称</th>
                        <td>%(version_name)s</td>
                        <th>测试阶段</th>
                        <td>%(testing_phase)s</td>
                        <th>测试时间</th>
                        <td>%(testing_time)s</td>
                    </tr>
                    <tr>
                        <th colspan="2">版本说明</th>
                        <td colspan="4">%(release_note)s</td>
                    </tr>
                    <tr>
                        <th colspan="2">测试说明</th>
                        <td colspan="4">%(testing_note)s</td>
                    </tr>
                    <tr>
                        <th colspan="2">测出标准</th>
                        <td colspan="4">%(testing_standard)s</td>
                    </tr>
                    <tr>
                        <th>测试人员</th>
                        <td>%(tester)s</td>
                        <th>测试结果</th>
                        <td>%(test_result)s</td>
                        <th>测试项</th>
                        <td>%(testing_items)s</td>
                    </tr>
                    <tr>
                        <th colspan="2">延期说明</th>
                        <td colspan="4">%(delay_note)s</td>
                    </tr>
                """
    BUG_HTML = """        <tr class="text-center success" style="font-weight: bold;font-size: 14px;">
            <th colspan="6" style="width: 30%; text-align: center;background: #2db158">Bug汇总</th>
        </tr>
        <tr style="text-align: center">
            <th>Bug总数</th>
            <th>严重bug（个）</th>
            <th>一般bug（个）</th>
            <th>低级bug（个）</th>
            <th>挂起bug（个）</th>
            <th>备注</td>
        </tr>
        <tr>
            <td>{sum}</td>
            <td>{danger}</td>
            <td>{normal}</td>
            <td>{low}</td>
            <td>{hang}</td>
            <td>{note}</td>
        </tr>
        <tr class="text-center success" style="font-weight: bold;font-size: 14px;">
            <th colspan="6" style="width: 30%; text-align: center;background: #2db158">遗留问题</th>
        </tr>
        <tr style="text-align: center">
            <th>序号</td>
            <th>问题描述</th>
            <th>准出原因</th>
            <th>严重程度</th>
            <th>责任人</th>
            <th>问题地址</th>
        </tr>"""
    LEGACY_HTML = """<tr>
                        <td>%(id)s</td>
                        <td>%(ques_desc)s</td>
                        <td>%(reason)s</td>
                        <td>%(severity)s</td>
                        <td>%(duty_officer)s</td>
                        <td>%(address)s</td>
                    </tr>"""

    RISK_HTML = """ <tr class="text-center success" style="font-weight: bold;font-size: 14px;">
                        <th colspan="6" style="width: 30%; text-align: center;background: #2db158">风险</th>
                    </tr>
                    <tr style="text-align: center">
                        <th>序号</th>
                        <th>风险描述</th>
                        <th>风险级别</th>
                        <th>应对措施</th>
                        <th>负责人</th>
                        <th>备注</th>
                    </tr>"""

    RISK_DETAIL_HTML = """  <tr>
                                <td>%(id)s</td>
                                <td>%(risk_desc)s</td>
                                <td>%(deal_method)s</td>
                                <td>%(severity)s</td>
                                <td>%(duty_officer)s</td>
                                <td>%(note)s</td>
                            </tr>"""

    END_HTML = """    </table>
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
        self.version_name = receive_data["version_name"]
        self.testing_phase = receive_data["testing_phase"]
        self.testing_time = receive_data["testing_time"]
        self.release_note = receive_data["release_note"]
        self.testing_note = receive_data["testing_note"]
        self.testing_standard = receive_data["testing_standard"]
        self.tester = receive_data["tester"]
        self.test_result = receive_data["test_result"]
        self.testing_items = receive_data["testing_items"]
        self.delay_note = receive_data["delay_note"]
        self.bug_num = receive_data["bug_num"]
        self.legacy = receive_data["legacy"]
        self.risk = receive_data["risk"]

    def html_PLATE(self):
        return self.HTML_PLATE

    def version_HTML(self):
        version_HTML = self.VER_HTML % dict(
            version_name=str(self.version_name),
            testing_phase=str(self.testing_phase),
            testing_time=str(self.testing_time),
            release_note=str(self.release_note),
            testing_note=str(self.testing_note),
            testing_standard=str(self.testing_standard),
            tester=str(self.tester),
            test_result=str(self.test_result),
            testing_items=str(self.testing_items),
            delay_note=str(self.delay_note)
        )
        return version_HTML

    def bug_HTML(self):
        bug_HTML = self.BUG_HTML.format(sum=self.bug_num[0],
                                        danger=self.bug_num[1],
                                        normal=self.bug_num[2],
                                        low=self.bug_num[3],
                                        hang=self.bug_num[4],
                                        note=self.bug_num[5],
                                        )
        return bug_HTML

    def legcacy_HTML(self):
        legcays = []
        for i in self.legacy:
            legcay = self.LEGACY_HTML % dict(
                id=i["id"],
                ques_desc=i["ques_desc"],
                reason=i["reason"],
                severity=i["severity"],
                duty_officer=i["duty_officer"],
                address=i["address"]
            )
            legcays.append(legcay)
        return legcays

    def risk_detail_HTML(self):
        risks = []
        for i in self.risk:
            risk = self.RISK_DETAIL_HTML % dict(
                id=i["id"],
                risk_desc=i["risk_desc"],
                deal_method=i["deal_method"],
                severity=i["severity"],
                duty_officer=i["duty_officer"],
                note=i["note"]
            )
            risks.append(risk)
        return risks

    def risk_HTML(self):
        return self.RISK_HTML

    def end_HTML(self):
        return self.END_HTML


class WriteHtml(ReportTest):
    def __init__(self, receive_data):
        super().__init__(receive_data)

    def write_HTML(self):
        now = time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime(time.time()))
        # todo exchange to offical path when on line
        local_path = os.getcwd()
        report_file_path = local_path + '/TesterRunner/static/reports/'

        file_version = self.version_name
        fileName = file_version + "-" + now + ".html"
        file_name = report_file_path + fileName
        f = open(file_name, "w", encoding="utf-8")
        f.write(self.html_PLATE())
        f.write(self.version_HTML())
        f.write(self.bug_HTML())
        for i in self.legcacy_HTML():
            f.write(i)
        f.write(self.risk_HTML())
        for j in self.risk_detail_HTML():
            f.write(j)
        f.write(self.end_HTML())
        return fileName



