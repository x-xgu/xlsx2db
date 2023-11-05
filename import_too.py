from core.utilities.file import load_worksheet_by_name
from core.utilities.serialize import XlsxDeserialize

xlsx = '基础参数.xlsx'

worksheet = load_worksheet_by_name(xlsx, '国家地区')
xlsx_obj = XlsxDeserialize(worksheet)
import_list = xlsx_obj.read_rows()


for instance in import_list:
    id_ = 'select nextval(eam_base_country_seq)'
    code = instance.get('国家地区代码')
    name = instance.get('国家地区简称')
    full_name = instance.get('国家地区全称')
    english_name = instance.get('英文名称')
    phone_code = instance.get('电话代码')

    currency = f'select id from eam_base_currency where name =%s ;' % (instance.get('本位货币'))
