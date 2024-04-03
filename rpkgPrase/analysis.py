from pathlib import Path
import zipfile
import xml.etree.ElementTree as ET


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
            if c.tag == 'switch':
                ret = self.visit_switch(c)
                if ret:
                    raise AnalisisException(self._works)

            self.visitNode(c)

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
            with zipfile.ZipFile(self._rpkgFile, 'r') as f:
                for name in f.namelist():
                    if not name.endswith('.projx'):
                        continue

                    with f.open(name) as fn:
                        self._works = name
                        self.visitProjx(fn)
