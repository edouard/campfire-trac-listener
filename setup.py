from setuptools import setup

setup(
    name='TracCampfireListener', version='0.1',
    packages=['campfirelistener'],
    entry_points = {
        'trac.plugins' : [
	    'campfirelistener.campfirelistener = campfirelistener.campfirelistener'
	]
    },
)
				
