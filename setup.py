from setuptools import setup, find_packages
setup(name='FitImageToRoom',
      extras_require=dict(tests=['pytests']),
      packages=find_packages(where='src'),
      package_dir={"":"src"},
      )