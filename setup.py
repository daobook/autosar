from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='autosar',
      version='0.5.0',
      description='autosar python module',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Topic :: Text Processing :: Markup :: XML',
      ],
      url='http://github.com/cogu/autosar',
      author='Conny Gustafsson',
      author_email='congus8@gmail.com',
      license='MIT',
	  install_requires=[
          'cfile>=0.2.0',
      ],
      packages=['autosar','autosar.parser', 'autosar.template', 'autosar.writer', 'autosar.util',
        'amber', 'amber.rte', 'amber.rte.generator', 'amber.rte.generator', 'amber.template', 'amber.template.services'],
	  zip_safe=False,
	  test_suite='tests.my_test_suite')
