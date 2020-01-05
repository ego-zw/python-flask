
from flask import Flask, render_template, request
import pandas as pd
import cufflinks as cf
import plotly as py

app = Flask(__name__)

option_list = ['居民消费水平', '人均GDP与人均消费水平', 'GDP水平情况', '分省人均GDP']

# 准备工作
df = pd.read_csv('try.csv',encoding='gbk')#读取
Race_available_names = list(df.表头.dropna().unique())#列表下拉值赋予给regions_available
cf.set_config_file(offline=True, theme="ggplot")
py.offline.init_notebook_mode()

Race_available = []

for i in range(len(Race_available_names)):
  Race_available.append({
    "index": i,
    "name": Race_available_names[i]
  })

plot_all = ["","","",""]
df_data = [{},{},{},{}]

with open("templates/cpi.html", encoding="utf8", mode="r") as f:
    plot_all[0] = "".join(f.readlines())
    df_data[0] = pd.read_csv('cpi.csv',encoding='utf-8')

with open("templates/gdpandcpi.html", encoding="utf8", mode="r") as f:
    plot_all[1] = "".join(f.readlines())
    df_data[1] = pd.read_csv('renjungdp.csv',encoding='utf-8')

with open("templates/ditu.html", encoding="utf8", mode="r") as f:
    plot_all[2] = "".join(f.readlines())
    df_data[2] = pd.read_csv('gdp.csv',encoding='utf-8')

with open("templates/gdpi.html", encoding="utf8", mode="r") as f:
    plot_all[3] = "".join(f.readlines())  
    df_data[3] = pd.read_csv('renjungdp.csv',encoding='utf-8')



@app.route('/',methods=['GET'])
def hu_run_2019():
    data_str = df.to_html()
    return render_template('results2.html',
                           the_res = data_str,
                           the_select_region=Race_available)

@app.route('/hurun',methods=['POST'])
#三个图表
def timeline_bar():
    the_region_selected = int(request.form.get("the_region_selected"))
    data_str = df_data[the_region_selected]
    data_str = data_str.to_html()
    # data_str = df.to_html()
    df_data2 = ""
    # if the_region_selected == 1:
    #   df_data2 = pd.read_csv('cpi.csv',encoding='utf-8').to_html()


    return render_template('results2.html',
                            the_plot_all = plot_all[the_region_selected],
                            selected = the_region_selected,
                            the_res = data_str,
                            the_res2 = df_data2,
                            the_select_region=Race_available,
                           )
    option = request.form['option']
    if option == "居民消费水平":
        return redirect('/cpi')
    elif option == "人均GDP与人均消费水平":
        return redirect('/gdpandcpi')
    elif option == "GDP水平情况":
        return redirect('/ditu')
    elif option == "分省人均GDP":
        return redirect('/gdpi')
    else:
        return "异常"
@app.route('/cpi',methods=['GET'])
def analysis_one():
    if not request.args.get('type') == None:
        return render_template( 'cpi.html', option_list=option_list )
    df = pd.read_csv( 'csv_conf/adult newly infected with HIv.csv', encoding='utf-8', delimiter="," )
    regions_available = list(df)
    data_str = df.to_html( )
    return render_template('cpi.html',the_res = data_str,option_list=option_list)

@app.route('/gdpandcpi',methods=['GET'])
def analysis_two():
    if not request.args.get('type') == None:
        return render_template( 'gdpandcpi.html', option_list=option_list )
    df = pd.read_csv( 'csv_conf/legalcountryfinal.csv', encoding='utf-8', delimiter="," )
    regions_available = list(df)
    data_str = df.to_html( )
    return render_template('gdpandcpi.html',the_res = data_str,option_list=option_list)

@app.route('/ditu',methods=['GET'])
def analysis_three():
    if not request.args.get('type') == None:
        return render_template( 'ditu.html', option_list=option_list )
    df = pd.read_csv( 'csv_conf/chinafensheng.csv', encoding='utf-8', delimiter="," )
    regions_available = list(df)
    data_str = df.to_html( )
    return render_template('ditu.html',the_res = data_str,option_list=option_list)


@app.route('/gdpi',methods=['GET'])
def analysis_four():
    if not request.args.get('type') == None:
        return render_template( 'gdpi.html', option_list=option_list )
    df = pd.read_csv( 'csv_conf/chinafensheng.csv', encoding='utf-8', delimiter="," )
    regions_available = list(df)
    data_str = df.to_html( )
    return render_template('gdpi.html',the_res = data_str,option_list=option_list)

if __name__ == '__main__':
    app.run(debug=True,port=8000)
