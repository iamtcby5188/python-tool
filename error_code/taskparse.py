import json

import pandas as pd
import numpy as np

excel_file = r'C:\Users\C1\Desktop\Agent错误码_本期优化Agent为true的内容.xlsx'

if __name__ == "__main__":
    df = pd.read_excel(excel_file)
    selected_columns = df.iloc[:, [1, 6, 7]].to_numpy()
    print(selected_columns)
    ret = []
    for i in selected_columns:
        ret.append({
            "errorcode": i[0],
            "message": i[1],
            "suggestion": i[2]
        })

    with open('e:\\a.json', 'w') as f:
        f.write(json.dumps(ret,ensure_ascii=False))
