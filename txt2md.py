import re
import os


def txt_to_markdown(text):
    # 将标题转换为Markdown标题，并在前面添加一个换行符
    text = re.sub(r'^(一、|二、|三、|四、|五、|六、|七、|八、|九、|十、)(.*)$', r'# \1\2', text, flags=re.MULTILINE)

    # 将数字和字母之间的添加空格
    text = re.sub(r'(\d+)([\u4e00-\u9fa5])', r'\1 \2', text)

    # 转换一级标题
    text = re.sub(r'^(?P<level>\d+)\s(?P<title>.+)$', r'# \g<level> \g<title>', text, flags=re.MULTILINE)
    text = re.sub(r'(附录[A-Z])', r'# \1', text, flags=re.MULTILINE)

    # 转换二级标题
    text = re.sub(r'^(?P<level>\d+\.\d+)\s(?P<title>.+)$', r'## \g<level> \g<title>', text, flags=re.MULTILINE)
    text = re.sub(r'^([A-Z]\.\d+\s.+)$', r'## \1', text, flags=re.MULTILINE)

    # 转换三级标题
    text = re.sub(r'^(?P<level>\d+\.\d+\.\d+)\s(?P<title>.+)$', r'### \g<level> \g<title>', text, flags=re.MULTILINE)
    text = re.sub(r'^([A-Z]\.\d\.\d\s.*)$', r'### \1', text, flags=re.MULTILINE)

    # 将特点列表转换为Markdown列表
    text = re.sub(r'^●(.*)$', r'- \1', text, flags=re.MULTILINE)

    # 将连续的两个换行符转换为一个换行符
    text = re.sub(r'\n{2,}', '\n', text)

    # 检查连续的标题数量，如果超过3个，就在这些标题前添加"目录"
    titles = re.findall(r'# 一、|二、|三、|四、|五、|六、|七、|八、|九、|十、', text)
    if len(titles) > 3:
        text = text.replace(titles[0], '# 目录\n' + titles[0])

    return text


def generate_md(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        txt = f.read()

    txt = "# " + txt

    markdown = txt_to_markdown(txt)

    return markdown
