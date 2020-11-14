import xlwt
import xlwt

workbook = xlwt.Workbook(encoding='utf-8')  # 创建workbook对象
worksheet1 = workbook.add_sheet('hello')  # 创建工作表
worksheet1.write(0, 0, 'hello')  # 写入数据

worksheet2 = workbook.add_sheet('九九乘法表')
for i in range(0, 9):
    for j in range(0, i + 1):
        worksheet2.write(i, j, "%d * %d = %d" %
                         (i + 1, j + 1, (i + 1)*(j + 1)))
workbook.save('./test/student.xls')  # 保存数据
