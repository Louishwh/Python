
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS
import pygal

def graphing(language,projectnames,stars):
	# style = LS('1199bb',base_style=LCS)
	# chart = pygal.Bar(style=style,x_label_rotation=45,show_legend=False)
	chart = pygal.Bar(x_label_rotation=35,show_legend=False)
	chart.title = 'Most-started '+language+' Projects On Github '
	chart.x_labels = projectnames
	chart.add('',stars)
	chart.render_to_file(language+"_repos.svg")