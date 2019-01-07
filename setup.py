from setuptools import setup, find_packages

version = '0.03'

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='tsresolve',
      version=version,
      description="Natural language parsing of recurring events",
      long_description=long_description,
      classifiers=[
          'Natural Language :: English',
          'Topic :: Text Processing :: Linguistic',
          'License :: OSI Approved :: MIT License'
      ],
      keywords='Natural language parsing of time stamps',
      author='Akhil Kumar D',
      author_email='akhilkumar.doppalapudi@gmail.com',
      url='https://github.com/akhilkumard/tsresolve',
      license='MIT',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      zip_safe=False,
      install_requires=[
          'parsedatetime','python-dateutil',
      ]
      )
