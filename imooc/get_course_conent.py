import requests
from lxml import html

# 指定要爬取的网页URL
url = "https://coding.imooc.com/class/892.html"

# 发送HTTP GET请求以获取网页内容
response = requests.get(url)

# 检查请求是否成功
if response.status_code == 200:
    # 使用lxml的html模块解析网页内容
    tree = html.fromstring(response.content)

    # 使用XPath获取所有的父级元素
    parents = tree.xpath("//*[contains(@class, 'catague-item')]")

    # 遍历每一个父级元素
    for parent in parents:
        # 在当前父级元素中提取子元素
        # title = parent.xpath("//*[contains(@class, 'left')]")  # 获取标题内容
        title = parent.xpath(
            "./*[contains(@class, 'name-box')]//*[contains(@class, 'left') and normalize-space(text())]/text()")  # 获取标题内容
        content = parent.xpath("./ul//*[contains(@class, 'media-name')]/text()")  # 获取段落内容

        # 遍历打印标题和段落内容
        for t in title:
            print(t.strip().replace('\n', ''))
        for paragraph in content:
            print(f"{paragraph.strip().replace('\n', '')}")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
