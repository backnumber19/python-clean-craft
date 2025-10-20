def calc_mdd(price_list):
    max_dd = 0
    max_peak = 0
    for price in price_list:
        if price > max_peak:
            max_peak = price
        current_dd = max_peak - price
        max_dd = max(max_dd, current_dd)
    return max_dd
