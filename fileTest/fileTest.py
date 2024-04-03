import os
import xml.etree.ElementTree as ET
from openpyxl import Workbook


class testErrorDefine:
    def __init__(self):
        self.a = ''
        self.code = 0
        self.des = ''
        self.src = ''
        self.trans = ''
        self.isUsed = False

    def __str__(self):
        return f'{self.a},{self.code},{self.des},{self.src},{self.trans}'


def parseErrorCode(lstE):
    with open(f'{os.getcwd()}\\1.txt', mode='r', encoding='utf-8') as f:
        num = 0
        for line in f:
            errInfo: testErrorDefine = testErrorDefine()
            line = line.replace(',', '').replace('\r', '').replace('\n', '')
            index = line.find('//')

            df = line
            des = ''
            if index > 0:
                des = line[index:].replace('//', '')
                df = line[:index]

            idxeq = df.find('=')
            if idxeq > 0:
                num = int(df[idxeq + 1:])
                df = df[:idxeq]

            else:
                num = num + 1

            errInfo.a = df.strip()
            errInfo.code = num
            errInfo.des = des.strip()
            lstE.append(errInfo)


def extract_content(input_string):
    comma_index = input_string.find(',')
    if comma_index != -1:
        before_comma = input_string[:comma_index]
        quote_index1 = input_string.find('"', comma_index)
        quote_index2 = input_string.find('"', quote_index1 + 1)
        if quote_index1 != -1 and quote_index2 != -1:
            after_comma_quote_content = input_string[quote_index1 + 1:quote_index2]
            return before_comma.strip(), after_comma_quote_content.strip()
    return None, None


def parseXML(lstE):
    tree = ET.parse(f'{os.getcwd()}\\cubeagent_zh.ts')
    root = tree.getroot()
    for c in root:
        if c.tag == 'context':
            for sc in c:
                if sc.tag == 'message':
                    src = ''
                    tras = ''
                    for ssc in sc:
                        if ssc.tag == 'source':
                            try:
                                src = ssc.text.strip().replace('\r', '').replace('\n', '')
                            except:
                                pass

                        if ssc.tag == 'translation':
                            try:
                                tras = ssc.text.strip()
                            except:
                                pass

                    for item in lstE:
                        if item.src == src:
                            item.trans = tras


import re


def extract_from_string(input_string):
    # 定义正则表达式模式，匹配 GLOBALCODEDICT 后面的括号中的内容
    pattern = r'GLOBALCODEDICT\((.*?)\)'

    # 使用正则表达式搜索字符串
    match = re.search(pattern, input_string)

    # 如果匹配到了，则返回括号中的内容，否则返回空字符串
    if match:
        return match.group(1)
    else:
        return ""


def parseSrc(lstE):
    with open(f'{os.getcwd()}\\2.txt', mode='r', encoding='utf-8') as f:
        for line in f:
            a, src = extract_content(line)
            for item in lstE:
                if item.a == a:
                    item.src = src
                    break


def getErrorCode(errList):
    with open(f'{os.getcwd()}\\3.txt', mode='r', encoding='utf-8') as f:
        for line in f:
            a = extract_from_string(line).replace('Cube::', '')
            if a:
                for item in errList:
                    if item.a == a:
                        item.isUsed = True


if __name__ == "__main__":
    errList: list = []
    parseErrorCode(errList)
    parseSrc(errList)
    parseXML(errList)
    getErrorCode(errList)

    wb = Workbook()
    ws = wb.active

    ws.append(['枚举', '错误码', '描述', '源', '翻译', '是否在Agent中使用'])
    for e in errList:
        ws.append([e.a, e.code, e.des, e.src, e.trans, e.isUsed])

    wb.save(f'{os.getcwd()}\\aa.xlsx')
