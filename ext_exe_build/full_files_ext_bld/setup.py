from setuptools import setup

setup(name='extract_build',
      version='0.1.0',
      packages=['extract_build'],
      entry_points={
          'console_scripts': [
              'extract_build = extract_build.__main__:main'
          ]
      },
      )
