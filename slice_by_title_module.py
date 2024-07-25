from txt2md import generate_md
from collections import namedtuple
from langchain.text_splitter import MarkdownHeaderTextSplitter
Document = namedtuple('Document', ['page_content', 'metadata'])

def cutter(docs,max_content_length=500):
    list = []
    for doc in docs:
        if len(doc.page_content) > max_content_length:
            # 如果内容超过最大长度，使用 Header 2 分割子文档
            sub_docs = MarkdownHeaderTextSplitter(headers_to_split_on=[("##", "Header 2")]).split_text(doc.page_content)
            for sub_doc in sub_docs:
                if len(sub_doc.page_content) > max_content_length:
                    # 如果子文档内容仍然超过最大长度，使用 Header 3 分割子子文档
                    sub_sub_docs = MarkdownHeaderTextSplitter(headers_to_split_on=[("###", "Header 3")]).split_text(sub_doc.page_content)
                    for sub_sub_doc in sub_sub_docs:
                        if len(sub_sub_doc.page_content) > max_content_length:  # 如果三级标题划分后仍然超过最大字数限制
                            long_text = sub_sub_doc.page_content
                            lines = long_text.split('\n')  # 先按照空行分隔
                            chunks = [lines[i:i + 20] for i in range(0, len(lines), 20)]  # 再将文本按照每20行分割
                            merged = ['\n'.join(chunk) for chunk in chunks]  # 合并
                            for slice in merged:
                                list.append(slice)

                        else:
                            list.append(sub_sub_doc.page_content)
                else:
                    list.append(sub_doc.page_content)
        else:
            list.append(doc.page_content)
    return list

def slicing_by_title(md):

    s = md+''

    markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=[("#", "Header 1")])
    docs = markdown_splitter.split_text(s)  # 按照一级标题划分
    return cutter(docs)
