from setuptools import setup

setup(name='home',
      version='0.0.2',
      description='Home automation',
      url='http://github.com/manzato/home',
      author='Guillermo Manzato',
      author_email='manzato@gmail.com',
      license='MIT',
      packages=['home_ui', 'home_core'],
      setup_requires=['cython'],
      install_requires=[
          'kivy',
      ],
      entry_points = {
          'console_scripts': ['home=home_core.command_line:main'],
      },
      zip_safe=False)
