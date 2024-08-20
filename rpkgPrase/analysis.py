import os
import shutil
from pathlib import Path
import zipfile
import xml.etree.ElementTree as ET

_LST_DIR_ = [r'E:\package\rpkg_result', r'E:\package\rpkg_result_2309_2401']
output = r'e:\package\r.txt'


class AnalisisException(Exception):
    def __init__(self, strMsg):
        super.__init__(strMsg)


class _Analysis_Switch:
    def __init__(self, rpkgFile):
        self._rpkgFile = Path(rpkgFile)
        self._works: str = ''

    def visit_switch(self, s):
        n: int = 0
        nSteps: int = 0
        isDefaultHas: bool = False
        for c in s:
            if c.tag == 'steps':
                nSteps = nSteps + 1
                isDefault = c.get('default')
                if isDefault == 'true':
                    for cc in c:
                        isDefaultHas = True
                        n = n + 1
                        break
                else:
                    for ccc in c:
                        n = n + 1
                        break
        result = n == 1 and isDefaultHas and nSteps > 1
        return result

    def visitNode(self, obj):
        for c in obj:
            if c.tag == 'assign':
                rvar = c.get('rvar')
                if rvar and 'getPassword' in rvar:
                    print(self._rpkgFile, self._works)
                    with open(output, 'a') as outf:
                        data = f'{self._rpkgFile},{self._works} \r\n'
                        outf.write(data)
                        outf.flush()

            self.visitNode(c)

    # def visitNode(self, obj):
    #     for c in obj:
    #         if c.tag == 'switch':
    #             ret = self.visit_switch(c)
    #             if ret:
    #                 raise AnalisisException(self._works)
    #
    #         self.visitNode(c)

    def visitProjx(self, f):
        tree = ET.parse(f)
        root = tree.getroot()
        for obj in root:
            if obj.tag == "mainflow":
                self.visitNode(obj)
            elif obj.tag == 'subflows':
                for subflow in obj:
                    self.visitNode(subflow)

    def visitRpkg(self):
        if self._rpkgFile.suffix == ".rpkg":
            try:
                with zipfile.ZipFile(self._rpkgFile, 'r') as f:
                    for name in f.namelist():
                        if not name.endswith('.projx'):
                            continue

                        with f.open(name) as fn:
                            self._works = name
                            try:
                                self.visitProjx(fn)
                            except Exception as e:
                                print(e)
            except:
                pass


def parseRPKG():
    for d in _LST_DIR_:
        for root, dirs, files in os.walk(d):
            for f in files:
                p = os.path.join(root, f)
                print(p)
                a: _Analysis_Switch = _Analysis_Switch(p)
                a.visitRpkg()


def parseResult():
    with open(r'e:\\package\\pkgfiles.txt', 'w') as pkgf:
        workFlow: list = []
        filelist: list = []

        with open(output, 'r') as f:
            for line in f:
                if line:
                    lst = line.split(',')
                    if len(lst) == 2:
                        path = lst[0].split('\\')[-1]
                        workflow = lst[1]
                        if workflow in workFlow:
                            continue
                        workFlow.append(workflow)
                        print(path)
                        lst2 = path.split('_')
                        print(lst2)
                        if len(lst2) == 2:
                            rpkgfile = lst2[1]
                            if rpkgfile in filelist:
                                continue
                            filelist.append(rpkgfile)
                            pkgf.write(lst2[1])
                            pkgf.write('\n')


if __name__ == '__main__':
    lstRPKG: list = []
    with open(r'e:\\package\\pkgfiles.txt', 'r') as f:
        for line in f:
            # print(lstRPKG)
            lstRPKG.append(line.replace('\n',''))

    for d in _LST_DIR_:
        for root, dirs, files in os.walk(d):
            for ff in files:
                baseName = ff.split('_')[-1]
                # print(baseName)
                if baseName in lstRPKG:
                    absFile = os.path.join(root,ff)
                    shutil.copy(absFile, r"E:\package\securtystring")
                    print(absFile)
