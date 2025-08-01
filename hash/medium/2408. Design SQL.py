from typing import List


class SQL:

    def __init__(self, names: List[str], columns: List[int]):
        self.tables = {}
        for i in range(len(names)):
            self.tables[names[i]] = {
                'nextId': 1,
                'col': columns[i],
                'rows': {} # rowId: List
            }

    def ins(self, name: str, row: List[str]) -> bool:
        table = self.tables.get(name)
        if not table or table['col'] != len(row):
            return False
        table['rows'][table['nextId']] = row
        table['nextId'] += 1
        return True

    def rmv(self, name: str, rowId: int) -> None:
        table = self.tables.get(name)
        if not table or rowId not in table['rows']:
            return
        del table['rows'][rowId]

    def sel(self, name: str, rowId: int, columnId: int) -> str:
        table = self.tables.get(name)
        if not table or table['col'] < columnId or rowId not in table['rows']:
            return '<null>'
        return table['rows'][rowId][columnId-1]
        
    def exp(self, name: str) -> List[str]:
        table = self.tables.get(name)
        if not table:
            return []
        return [','.join([str(key)] + val) for key, val in table['rows'].items()]

# Your SQL object will be instantiated and called as such:
# obj = SQL(names, columns)
# param_1 = obj.ins(name,row)
# obj.rmv(name,rowId)
# param_3 = obj.sel(name,rowId,columnId)
# param_4 = obj.exp(name)