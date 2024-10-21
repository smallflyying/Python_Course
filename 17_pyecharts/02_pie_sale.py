# @Version  : 1.0
# @Author   : LiHongFei
# @File     : 02_pie_sale.py
# @Time     : 2024/10/21 21:44


from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker


"""
    分析：
    1. Pie() 创建了Pie对象
    2. .add("", [list(z) for z in zip(Faker.choose(), Faker.values())])
    就是给饼状图添加数据
    3. .set_global_opts(title_opts=opts.TitleOpts(title="Pie-设置颜色"))
    4. .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    formatter="{b}: {c} 表示标签显示的形式为 名称：值
    5. .render("pie_sale.html") 生成对应的网页文件 pie_sale.html
"""

data = [['衬衫', 138], ['毛衣', 40], ['领带', 74], ['裤子', 112],
        ['风衣', 147], ['高跟鞋', 104], ['袜子', 65]]
c = (
    Pie()
    .add("", data)
    .set_colors(["blue", "green", "yellow", "red", "pink", "orange", "purple"])
    .set_global_opts(title_opts=opts.TitleOpts(title="Pie-商品销售情况"),
                     toolbox_opts=opts.ToolboxOpts(is_show=True))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}",
                                               font_size=20))
    .render("pie_sale.html")
)

# print([list(z) for z in zip(Faker.choose(), Faker.values())])

