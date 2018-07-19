import unittest
from TestCases.case01 import testcase01
from TestCases.case02 import testcase02
from TestCases.case03 import testcase03
from TestCases.case04 import testcase04
from TestCases.case05 import testcase05
from TestCases.case06 import testcase06
from TestCases.case07 import testcase07


testsuite = unittest.TestSuite()       # 执行测试集命令
#testsuite.addTest(testcase01('test_case01'))
testsuite.addTests([testcase01('test_case01'), testcase01('test_case02')])    # 同一个接口不同的测试用例
testsuite.addTests([testcase02('test_case01'), testcase02('test_case02')])
testsuite.addTests([testcase03('test_case01'), testcase03('test_case02')])
testsuite.addTests([testcase04('test_case01'), testcase04('test_case02'), testcase04('test_case03')])
testsuite.addTests([testcase05('test_case01'), testcase05('test_case02'), testcase05('test_case03'), testcase05("test_case04"), testcase05('test_case05')])
testsuite.addTests([testcase06('test_case01'), testcase06("test_case02")])
testsuite.addTests([testcase07("test_case01"), testcase07("test_case02"), testcase07("test_case03"), testcase07("test_case04") ])





#unittest.TextTestRunner().run(testsuite

#--------执行测试集并生成html报告--------
import HTMLTestRunner
st = open('./report.html', 'wb')
HTMLTestRunner.HTMLTestRunner(stream=st, title=u"3.1.1智能场馆接口自动化测试").run(testsuite)

