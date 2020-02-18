from setuptools import setup, find_packages


def readme():
    return open('README.rst').read()


setup(name="pycards",
      version="0.2.2a1",
      description="A python-based card game framework",
      long_description=readme(),
      author="Sydney Weidman",
      author_email="sydney.weidman@gmail.com",
      packages=find_packages('src'),
      package_dir={'': 'src'},
      tests_require=['coverage'],
      include_package_data=True, )
