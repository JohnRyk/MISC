import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS



def plot(language):

	url = "https://api.github.com/search/repositories?q="+language+":python&sort=stars"

	r = requests.get(url)
	status_code = r.status_code
	if status_code!=200:
		print('[-] sorry, with something wrong! try to choose another language or try again')


	# json格式存储
	response_dict = r.json()

	# 打印仓库总计数
	print("total repositories:",response_dict['total_count'])
	   
	# 创建仓库字段列表
	repo_dicts = response_dict['items']

	# 名字列表，和项目的星数列表
	names,stars=[],[]
	for repo_dict in repo_dicts:
		names.append(repo_dict['name'])
		stars.append(repo_dict['stargazers_count'])

	# 可视化

	#my_style = ls(,base_style=lcs)
	chart = pygal.Bar(x_label_rotation=45,show_lengend=False)
	chart.title="most-starred "+language+" project on github"

	#chart.x_labels=names
	# 优化


	my_config = pygal.Config()
	my_config.x_label_rotation = 45
	my_config.show_legend = False
	my_config.title_font_size = 24
	my_config.label_font_size = 14
	my_config.major_label_font_size = 18
	my_config.truncate_label = 15
	my_config.show_y_guides = False
	my_config.width = 1000

	# 在pygal中，将鼠标指向条形将显示它表示的信息，这通常称为工具提示 
	# 下面add()函数的参数将会是两个字典，它们的键分别是'value'和‘'label'
	# pygal根据'value'对应的值确定柱子的高度，根据'label'的字符串关联工具提示 
	# xlink对应得是柱子单机可以跳转的链接
	names,plot_dicts =[],[]

	# 遍历每个仓库
	for repo_dict in repo_dicts:
		# 构造名字列表（x轴的字段） 
		names.append(repo_dict['name'])
		# 构造add接收的参数
		plot_dict = {
		   'value':repo_dict['stargazers_count'],
		   # 打印description但碰到了typeerror,需要指定类型 
		   'label':str(repo_dict['description']),
		   'xlink':repo_dict['clone_url'],
		}
		plot_dicts.append(plot_dict)

	my_style = LS('#00CCFF',base_style=LCS)
	chart.add('',plot_dicts)

	# 在图表中添加可单击的链接

	chart.render_to_file(language+'_repos.svg')


