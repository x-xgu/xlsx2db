import math

from xlrd.sheet import Sheet


def transform_excel_cell_value(val):
    """
    将0.0转成0
    同时将字符串去除首位的多余空格
    """

    if isinstance(val, float) and math.modf(val)[0] == 0.0:
        return int(val)
    else:
        if isinstance(val, str):
            val = val.strip()
        return val


def num2excel_col(number):
    """
    将数值转成Excel中列的形式（AA AB AC AD……）
    目的：便于针对单元格报错时，精准定位
    """

    result = ''
    while number > 0:
        number, remainder = divmod(number - 1, 26)
        result = chr(ord('A') + remainder) + result
    return result


def unmerge_cells(sheet: Sheet):
    """
    取消合并单元格

    实现思路：
    1、先获取到当前工作簿中的所有的合并单元格
    2、使用列表记录合并单元格中的坐标值
    3、同步新建一个字典，将坐标值及合并单元格的值作为键值对保存

    4、遍历每一个单元格
    5、如果坐标落在合并单元的列表中，则从字典中获取坐标的值，进行单元格值的填充
    """

    new_sheet_data = []
    merge_cells_rx_record = []
    write_cells_value = {}

    n_rows = sheet.nrows
    n_cols = sheet.ncols

    for crange in sheet.merged_cells:
        rlo, rhi, clo, chi = crange
        cell_value = sheet.cell(rlo, clo).value
        for r in range(rlo, rhi):
            for c in range(clo, chi):
                merge_cells_rx_record.append((r, c))  # 记录合并单元格的行列值
                write_cells_value[(r, c)] = cell_value
    for r in range(n_rows):
        new_row_data = []
        for c in range(0, n_cols):
            cell_value = sheet.cell_value(r, c)
            if (r, c) in merge_cells_rx_record:
                cell_value = write_cells_value[(r, c)]
            new_row_data.append(cell_value)
        new_sheet_data.append(new_row_data)
    return new_sheet_data
