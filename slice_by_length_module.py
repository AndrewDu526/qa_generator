import os
from langchain.text_splitter import RecursiveCharacterTextSplitter, CharacterTextSplitter
from langchain_community.document_loaders import UnstructuredFileLoader

from docx import Document

def slicing_by_length(file_path, name):
    # 加载文件 loading
    name = name[:-4]  # 删除文件后缀
    loader = UnstructuredFileLoader(file_path)
    data = loader.load()

    # 文本分割器配置 setting of splitter
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=160,
        separators=["\n"]
    )
    # 切片列表 list of slices
    slices = splitter.split_documents(data)
    slice_save(slices, name)
    list = []
    for slice in slices:
        list.append(slice.page_content)
    return list

def slice_save(slices, name):  # 备份
    doc = Document()
    for slice in slices:
        doc.add_paragraph(slice.page_content.replace('\n\n', '\n')+'\n-------------------------------------')
    doc.save('D:\coding\workingspace\myprojects\qa_generator_tool\output\\01_sliced\\sliced_' + name + '.docx')


