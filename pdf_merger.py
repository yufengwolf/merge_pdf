import os, sys
from pypdf import PdfMerger as pm

print('pdf_merger.py dir[default .]')

# default文件路径
pdf_path = r'.'

if len(sys.argv) >= 2:
    pdf_path = sys.argv[1]
print(pdf_path)

def merge():
    # 获取文件夹下pdf文件
    pdf_lst = [f for f in os.listdir(pdf_path) if f.endswith('.pdf')]
    if len(pdf_lst) == 0:
        print('current dir no pdf, merge failure !!!')
        return

    # 合成绝对路径
    pdf_lst = [os.path.join(pdf_path, filename) for filename in pdf_lst]

    # 合并pdf
    pdf_merger = pm()
    for pdf in pdf_lst:
        pdf_merger.append(pdf, outline_item=False)

    # 合并文件保存
    pdf_merger.write(r'merge.pdf')
    print('merge success !')

merge()