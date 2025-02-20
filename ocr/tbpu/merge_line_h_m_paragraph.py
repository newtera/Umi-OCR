# 文块处理：横排-合并多行-自然段
from ocr.tbpu.merge_line_h_m_left import TbpuLineHMultiLeft


class TbpuLineHMultiParagraph(TbpuLineHMultiLeft):
    def __init__(self):
        super().__init__()
        self.tbpuName = '横排-合并多行-自然段'

    def isRuleMerge(self, box1, box2):
        '''合并规则：两个box可以合并时返回T'''
        # y不接壤，说啥也没用
        if abs(box2[0][1]-box1[3][1]) > self.limitY:
            return False
        # 若当前是第一行，则额外允许第二行的x位置前移2个全角字符（即行高）
        if self.mergeNum == 1:
            x = box2[0][0] + self.rowHeight*2
            if abs(x-box1[3][0]) <= self.limitX:
                return True
        # 1的左下角与2的左上角接壤时OK
        return abs(box2[0][0]-box1[3][0]) <= self.limitX
