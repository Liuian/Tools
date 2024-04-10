from bs4 import BeautifulSoup
import requests

url = '您要下载 HTML 代码的网页 URL'

# 发送 GET 请求获取网页内容
response = requests.get(url)

# 检查响应状态码是否为 200，表示请求成功
if response.status_code == 200:
    # 获取网页 HTML 代码
    html_content = response.text
    # 输出或进一步处理 HTML 代码
    print(html_content)
else:
    print('请求失败，状态码:', response.status_code)


# 使用 BeautifulSoup 解析 HTML
soup = BeautifulSoup(html_content, 'html.parser')

# 找到所有的問題和答案
qa_items = soup.find_all('div', class_='panel')

# 遍歷每個 Q&A 項目並提取問題和答案
for item in qa_items:
    question = item.find('button', class_='panel-button').text.strip()
    answer = item.find('div', class_='panel-body').text.strip()
    
    print("問題:", question)
    print("答案:", answer)
    print("------")
