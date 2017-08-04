import pygal

wm = pygal.maps.world.World()
wm.title = 'American'
# wm.add('North American',['ca','mx','us'])
# wm.add('Central American',['bz','cr','gt','hn','ni','pa','sv'])
# wm.add('South American',['ar','bo','br'])
wm.add('American',{'ca':34126000,'mx':309349000,'us':113423000})
wm.add('Asian',{'cn':140000000})
wm.render_to_file('americas.svg')