from copy import deepcopy

query_list = [
    {"PO行项目号": "01850", "价格单位": "1000", "供应商编号": "100056", "公司编号": "1000", "制造商零件号": "2325415-1",
     "剩余送货数量": "10800.0", "单位": "PC", "备注": "", "工厂": "1001", "库存地点": "1002", "最小包装量": "1200.000 ",
     "未税价": "1150", "本次送货数量": "10800.0", "物料名称": "国产 护套 40 不防水 自然色", "物料编号": "A02030920",
     "订单数量": "26400.000 ", "订单日期": "2024-07-22", "订单类型": "ZNB", "采购组织编号": "1000",
     "采购订单号": "6100074323"},
    {"PO行项目号": "00600", "价格单位": "1000", "供应商编号": "100056", "公司编号": "1000", "制造商零件号": "2325415-1",
     "剩余送货数量": "268800.0", "单位": "PC", "备注": "", "工厂": "1001", "库存地点": "1002",
     "最小包装量": "1200.000 ", "未税价": "1150", "本次送货数量": "268800.0", "物料名称": "国产 护套 40 不防水 自然色",
     "物料编号": "A02030920", "订单数量": "270000.000 ", "订单日期": "2024-07-22", "订单类型": "ZNB",
     "采购组织编号": "1000", "采购订单号": "6100075167"},
    {"PO行项目号": "00020", "价格单位": "1000", "供应商编号": "100056", "公司编号": "1000", "制造商零件号": "2005327-1",
     "剩余送货数量": "0.0", "单位": "PC", "备注": "", "工厂": "1001", "库存地点": "1002", "最小包装量": "576.000 ",
     "未税价": "973.73", "本次送货数量": "0.0", "物料名称": "进口 护套 24 不防水 白", "物料编号": "A02000092",
     "订单数量": "18432.000 ", "订单日期": "2024-08-01", "订单类型": "ZNB", "采购组织编号": "1000",
     "采购订单号": "6100083100"},
    {"PO行项目号": "00130", "价格单位": "1000", "供应商编号": "100056", "公司编号": "1000", "制造商零件号": "2005327-1",
     "剩余送货数量": "2304.000 ", "单位": "PC", "备注": "", "工厂": "1001", "库存地点": "1002",
     "最小包装量": "576.000 ", "未税价": "973.73", "本次送货数量": "2304.000 ", "物料名称": "进口 护套 24 不防水 白",
     "物料编号": "A02000092", "订单数量": "2304.000 ", "订单日期": "2024-08-24", "订单类型": "ZNB",
     "采购组织编号": "1000", "采购订单号": "6100084523"},
    {"PO行项目号": "00010", "价格单位": "1000", "供应商编号": "100056", "公司编号": "1000", "制造商零件号": "2005327-1",
     "剩余送货数量": "576.000 ", "单位": "PC", "备注": "", "工厂": "1001", "库存地点": "1002", "最小包装量": "576.000 ",
     "未税价": "973.73", "本次送货数量": "576.000 ", "物料名称": "护套 24 不防水 白", "物料编号": "A02000092",
     "订单数量": "576.000 ", "订单日期": "2024-08-30", "订单类型": "ZNB", "采购组织编号": "1000",
     "采购订单号": "6100084977"},
    {"PO行项目号": "00010", "价格单位": "1000", "供应商编号": "100056", "公司编号": "1000",
     "制造商零件号": "1-936119-2", "剩余送货数量": "888000.000 ", "单位": "PC", "备注": "", "工厂": "1001",
     "库存地点": "1003", "最小包装量": "6000.000 ", "未税价": "710", "本次送货数量": "888000.000 ",
     "物料名称": "护套 4 不防水 黄", "物料编号": "A02100665", "订单数量": "888000.000 ", "订单日期": "2024-08-10",
     "订单类型": "ZYP", "采购组织编号": "1000", "采购订单号": "6200025719"}]
real_list = [
    {
        "matCode": "A02030920",
        "poNo": "6100074323",
        "shippedQty": "2400"
    },
    {
        "matCode": "A02000092",
        "poNo": "6100084977",
        "shippedQty": "576"
    },
    {
        "matCode": "A02000092",
        "poNo": "6100084977",
        "shippedQty": "576"
    },
    {
        "matCode": "A02100665",
        "poNo": "6200025719",
        "shippedQty": "18000"
    },
    {
        "matCode": "A02100665",
        "poNo": "6200025719",
        "shippedQty": "6000"
    }
]


def try_allocate(queryList: list, real: dict) -> dict:
    ret_dict:dict = {"type": 0, "index": 0, "qd_list": [], "rd_data": deepcopy(real), "err": "人工审核"}
    real['remain'] = float(real['shippedQty'])
    # 完全匹配
    for query_item in queryList:
        if real['matCode'] == query_item['物料编号'] and real['poNo'] == query_item['采购订单号']:
            try:
                query_all_remain = float(query_item['剩余送货数量'])
                query_reamin = query_all_remain - query_item['used']
                real_remain = real['remain']
                if real_remain == 0.0:
                    break
                if query_reamin > 0.0:
                    if real_remain <= query_reamin:
                        query_item['used'] = query_item['used'] + real_remain
                        query_item['本次送货数量'] = str(real_remain)
                        real['remain'] = 0.0
                        ret_dict['qd_list'].append(deepcopy(query_item))
                    else:
                        query_item['used'] = query_all_remain
                        query_item['本次送货数量'] = str(query_reamin)
                        real['remain'] = real_remain - query_reamin
                        ret_dict['qd_list'].append(deepcopy(query_item))
            except Exception as e:
                print(f'{real},{query_item},failed')

    if real["remain"] == 0.0:
        ret_dict['err'] = 'ok'
    else:
        for query_item in queryList:
            if real['matCode'] == query_item['物料编号']:
                try:
                    query_all_remain = float(query_item['剩余送货数量'])
                    query_reamin = query_all_remain - query_item['used']
                    real_remain = real['remain']
                    if real_remain == 0.0:
                        break
                    if query_reamin > 0.0:
                        if real_remain <= query_reamin:
                            query_item['used'] = query_item['used'] + real_remain
                            query_item['本次送货数量'] = str(real_remain)
                            real['remain'] = 0.0
                            ret_dict['qd_list'].append(deepcopy(query_item))
                        else:
                            query_item['used'] = query_all_remain
                            query_item['本次送货数量'] = str(query_reamin)
                            real['remain'] = real_remain - query_reamin
                            ret_dict['qd_list'].append(deepcopy(query_item))
                except:
                    print(f'{real},f{query_item},failed')

        if real["remain"] == 0:
            ret_dict['err'] = 'ok'
        else:
            ret_dict['qd_list'].clear()


    return ret_dict


if __name__ == "__main__":
    result_list = []
    for query_item in query_list:
        query_item['used'] = 0

    for real in real_list:

        real_temp = deepcopy(real)
        query_list_temp = deepcopy(query_list)
        ret_dict = try_allocate(query_list_temp, real_temp)
        result_list.append(ret_dict)
        if ret_dict['err'] == 'ok':
            query_list = query_list_temp

    print(result_list)

    for ret in result_list:
        qd_list = ret['qd_list']
        for qd in qd_list:
            del qd['used']
    print(result_list)