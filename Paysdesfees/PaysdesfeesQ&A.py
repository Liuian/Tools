import requests
from bs4 import BeautifulSoup

url = 'http://paysdesfees.com/pages/clarity'

# 发送 GET 请求获取网页内容
response = requests.get(url)

# 检查响应状态码是否为 200，表示请求成功
if response.status_code == 200:
    # 获取网页 HTML 代码
    html_content = response.text

    # 使用 BeautifulSoup 解析 HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # 创建一个文件用于存储结果
    with open("qa_results.txt", "w", encoding="utf-8") as file:
        # 找到所有的問題和答案
        qa_items = soup.find_all('div', class_='panel')

        # 遍歷每個 Q&A 項目並提取問題和答案
        for item in qa_items:
            question = item.find('button', class_='panel-button').text.strip()
            answer = item.find('div', class_='panel-body').text.strip()
            
            # 写入问题和答案到文件中
            file.write("問題: " + question + "\n")
            file.write("答案: " + answer + "\n")
            file.write("------\n")
            
    print("结果已保存到 qa_results.txt 文件中。")

else:
    print('请求失败，状态码:', response.status_code)
