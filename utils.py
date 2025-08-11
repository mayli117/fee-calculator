from datetime import datetime, timedelta

def convert_to_gregorian(date_str):

    """將民國日期轉換為西元日期"""

    year = int(date_str[:3]) + 1911

    month = int(date_str[3:5])

    day = int(date_str[5:7])

    return datetime(year, month, day)

def calculate_fees(payload):

    """計算租金總額與天數"""

    start_date = convert_to_gregorian(payload['start_date'])

    end_date = convert_to_gregorian(payload['end_date'])

    total_days = (end_date - start_date).days

    rent = float(payload['rent'])

    cycle = int(payload['cycle'])

    fee_per_day = rent / 30

    total_fee = fee_per_day * total_days

    return {

        'total_days': total_days,

        'total_fee': round(total_fee, 2)

    }

def extract_discount_code(text):

    """

    從字串中提取折扣碼

    假設折扣碼格式為 DISCOUNT-XXXX

    """

    if text and "-" in text:

        return text.split("-")[-1]

    return None

def calculate_penalty(days_late, daily_penalty=10):

    """計算遲繳罰金"""

    return max(0, days_late) * daily_penalty
 

