from core.utilities.file import load_worksheet_by_name
from core.utilities.serialize import XlsxDeserialize

country = {
    'code': '国家地区代码',
    'name': '国家地区简称',
    'full_name': '国家地区全称',
    'english_name': '英文名称',
    'phone_code': '电话代码',
    'currency': '本位货币'
}

xlsx = '基础参数.xlsx'

worksheet = load_worksheet_by_name(xlsx, '国家地区')
xlsx_obj = XlsxDeserialize(worksheet, country)
import_list = xlsx_obj.to_rows_head_list()
print(import_list)


aaa = {
    'code': '',
    'name': '',
    'full_name': '',
    'english_name': '',
    'phone_code': '',
    'currency': 'select id from '
}



