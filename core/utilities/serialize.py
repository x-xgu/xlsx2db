from xlrd.sheet import Sheet

from core.utilities.convert import unmerge_cells, transform_excel_cell_value


class XlsxDeserialize:
    """
    Xlsx 反序列化

    1、检查工作簿头部信息
    2、取消所有的合并单元格
    3、将工作簿转换成对象列表
    """

    def __init__(self, worksheet: Sheet, head_row_index: int = 0):
        self.head_row_index = head_row_index
        self.worksheet = unmerge_cells(worksheet)
        self.n_rows = worksheet.nrows
        self.head_row = worksheet.row_values(self.head_row_index)

    def read_rows(self):
        """
        将 worksheet 转成 head 对象
        """

        row_dictionaries = []
        for i in range(self.head_row_index + 1, self.n_rows):
            record = self.worksheet[i]
            row_dict = {self.head_row[i]: transform_excel_cell_value(record[i]) for i in range(len(self.head_row))}
            row_dictionaries.append(row_dict)
        return row_dictionaries
