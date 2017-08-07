long_description = '''
monkeyhex.py is a small library to assist users of the python shell who work in contexts where printed numbers are more usefully viewed in hexadecimal.

Monkeyhex, as the name suggests, monkeypatches the system displayhook as well as the pprint and pdb modules to format integers as hex. To use it, just import the library and all future results will be formatted. To view a result in decimal again, put the expression in a print statement.
'''

from distutils.core import setup
setup(name='monkeyhex',
      version='1.3',
      py_modules=['monkeyhex'],
      description='Monkeypatch the python interpreter and debugger to print integer results in hex',
      long_description=long_description,
      url='https://github.com/rhelmot/monkeyhex',
      author='rhelmot',
      author_email='andrewrdutcher@gmail.com',
      license='MIT',
      keywords='hex hexadecimal monkeypatch integer number interpreter result debug debugger'
      )
