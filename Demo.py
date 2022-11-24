import cgi
import random, time
import requests
from pypinyin import lazy_pinyin
from lxml import etree

form = cgi.FieldStorage()

class log():
    citynamepy=''
    city=[]
    def cityin(self,city):                       #将输入的城市返回拼音首字符
        self.city=city.split(' ')
        self.citynamepy=''
        for i in lazy_pinyin(city):
            self.citynamepy+=i[0].upper()
        return self.citynamepy

print('Content-type:text/html \n\n')
print(r'<title>PyHouse</title>')
print('<link rel="stylesheet" type="text/css" href="../boolstrap/css/bootstrap.min.css"/>')
pri='''<div>
        <nav class="navbar navbar-inverse navbar-default" role="navigation">
    <div class="container-fluid">
    <div class="navbar-header">
        <a class="navbar-brand" href="#">PyHouse</a>
    </div>
    <div>
        <ul class="nav navbar-nav">
            <li class="active"><a href="#">首页</a></li>
            <li><a href="../cgi-bin/fenxi.py">分析</a></li>

        </ul>
    </div>

        <form class="navbar-form navbar-right" role="search" method="post" action="#">
        <div class="form-group">
            <input type="text" class="form-control" placeholder="Search" name="city"/>
        </div>
        <button type="submit" class="btn btn-default">提交</button>
    </form>
    </div>
</nav>

    </div>
    <div class="container">

<table class="table table-striped">

  <thead>
    <tr>
      <th>地点</th>
      <th>区域</th>
      <th>户型</th>
        <th>面积</th>
        <th>朝向</th>
        <th>装修</th>
        <th>楼层</th>
        <th>楼龄</th>
        <th>结构</th>
        <th>价格</th>
    </tr>
  </thead>
  <tbody>
    '''
print(pri)

city_name=form['city'].value
pro=log()
city_py=pro.cityin(city_name).lower()
url = 'https://' + city_py + '.lianjia.com/ershoufang/'
roww = 0
for i in range(1, 3):
    stip = f'pg{i}/'
    urrl = url + stip
    time.sleep(0.5)
    response = requests.get(urrl)
    data = etree.HTML(response.text)
    for r in range(1, 31):
        inserted = []
        goal = data.xpath(f'/html/body/div[4]/div[1]/ul/li[{r}]/div[1]/div[2]/div/a[1]/text()') + data.xpath(
            f'/html/body/div[4]/div[1]/ul/li[{r}]/div[1]/div[2]/div/a[2]/text()')  # 位置
        goal2 = data.xpath(f'/html/body/div[4]/div[1]/ul/li[{r}]/div[1]/div[3]/div/text()')  # 7个户型|
        goal2_lis = goal2[0].split('|')
        goal3 = data.xpath(f'/html/body/div[4]/div[1]/ul/li[{r}]/div[1]/div[6]/div[1]/span/text()') + data.xpath(
            f'/html/body/div[4]/div[1]/ul/li[{r}]/div[1]/div[6]/div[1]/i[2]/text()')  # 价格
        goal3 = ''.join(goal3)

        # sheet.write(roww + 1, 0, str(roww + 1))
        # sheet.write(roww + 1, 1, goal)
        inserted.append(goal[0])
        inserted.append(goal[1])

        for w in range(7):
            if w == 5:
                if (not goal2_lis[w][1:5].isdigit()):
                    # sheet.write(roww + 1, 3 + w, goal2_lis[w])
                    inserted.append('')
                    inserted.append(goal2_lis[w])
                    break
            # sheet.write(roww + 1, 2 + w, goal2_lis[w])
            inserted.append(goal2_lis[w])
        # sheet.write(roww + 1, 9, goal3)
        inserted.append(goal3)
        roww += 1
        print('<tr>')
        for i0 in inserted:
            if(i0!=''):
                print('<td>{}</td>'.format(i0))
            else:
                print('<td>暂无数据</td>')
        print('</tr>')

    response.close()
print('''</tbody>
</table>
    </div>
''')


#
# title='''
# <table class="table table-striped">
#
#   <thead>
#     <tr>
#       <th>序号</th>
#       <th>位置</th>
#       <th>户型</th>
#         <th>面积</th>
#         <th>朝向</th>
#         <th>装修</th>
#         <th>楼层</th>
#         <th>楼龄</th>
#         <th>结构</th>
#         <th>价格</th>
#     </tr>
#   </thead>
#   <tbody>
#     <tr>
#       <td>Tanmay</td>
#       <td>Bangalore</td>
#       <td>560001</td>
#     </tr>
#     <tr>
#       <td>Sachin</td>
#       <td>Mumbai</td>
#       <td>400003</td>
#     </tr>
#     <tr>
#       <td>Uma</td>
#       <td>Pune</td>
#       <td>411027</td>
#     </tr>
#   </tbody>
# </table>
# '''