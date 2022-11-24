import requests
from lxml import etree


#/html/body/div[4]/div[1]/div[2]/h2/span

print('Content-type:text/html \n\n')

htm='''
<html>
    <head>
        <title>PyHouse</title>
        <link rel="stylesheet" type="text/css" href="../boolstrap/css/bootstrap.min.css"/>
        <script src="../echarts.js"></script>
    </head>
    <body>
    <div>
        <nav class="navbar navbar-inverse navbar-default" role="navigation">
    <div class="container-fluid">
    <div class="navbar-header">
        <a class="navbar-brand" href="#">PyHouse</a>
    </div>
    <div>
        <ul class="nav navbar-nav">
            <li ><a href="index.html">首页</a></li>
            <li class="active"><a href="#">分析</a></li>

        </ul>
    </div>

        <form class="navbar-form navbar-right" role="search" method="post" action="/cgi-bin/Demo.py">
        <div class="form-group">
            <input type="text" class="form-control" placeholder="Search" name="city"/>
        </div>
        <button type="submit" class="btn btn-default">提交</button>
    </form>
    </div>
</nav>
 </div>
 
    <div class="container">
    <div id="main" style="width: 100%;height:600px;"></div>

    <script type="text/javascript">

        // 基于准备好的dom，初始化echarts实例
      var myChart = echarts.init(document.getElementById('main'));

      // 指定图表的配置项和数据
      var option = {
        title: {
          text: '全国主要城市二手房数量'
        },
        tooltip: {},
        legend: {
          data: ['二手房数量']
        },
        xAxis: {
          data: ['北京', '合肥', '重庆', '沈阳', '乌鲁木齐', '郑州','天津','哈尔滨']
        },
        yAxis: {},
        series: [
          {
            name: '二手房（套）',
            type: 'bar',
            data: ['''

#5, 20, 36, 10, 10, 20,54,60
city_py=['bj','hf','cq','sy','wlmq','zz','tj','hrb']
for i in city_py:
    url = 'https://' + i + '.lianjia.com/ershoufang/'
    response = requests.get(url)
    data = etree.HTML(response.text)
    # print(data.xpath('/html/body/div[4]/div[1]/div[2]/h2/span/text()'))
    htm+=(data.xpath('/html/body/div[4]/div[1]/div[2]/h2/span/text()')[0]+',')



htm2=''']
          }
        ]
      };

      // 使用刚指定的配置项和数据显示图表。
      myChart.setOption(option);
    </script>
</div>
    </body>
</html>
'''
print(htm+htm2)