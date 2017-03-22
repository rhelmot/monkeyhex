long_description = '''monkeyhex.py is a small library to assist users of the python shell who work in contexts where printed numbers are more usefully viewed in hexadecimal.
Monkeyhex will format the results of statements in the python interactive shell in hex. To use it, just import the library and all future results will be formatted. To view a result in decimal again, put the expression in a print statement.
In addition, Monkeyhex implements a pprint-like pretty-printing of long lists and dictionaries.
'''

from distutils.core import setup
setup(name='monkeyhex',
      version='1.2',
      py_modules=['monkeyhex'],
      description='Monkeypatch the python interpreter to print integer results in hex',
      long_description=long_description,
      url='https://github.com/rhelmot/monkeyhex',
      author='Andrew Dutcher',
      author_email='andrew@andrewdutcher.com',
      license='MIT',
      keywords='hex hexadecimal monkeypatch integer number interpreter result'
      )
