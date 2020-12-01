from distutils.core import setup

setup(
  name = 'thumbor-request-modifier-http-loader',
  packages = ['thumbor-request-modifier-http-loader'],   # Chose the same as "name"
  version = '0.1',
  license='GPL-3.0',
  description = 'Custom HTTP loader for Thumbor which allows to modify client request based on certain conditions.',
  author = 'Maksim Barouski',
  author_email = 'maksim.borovskij@yandex.ru',
  url = 'https://github.com/dffrntmedia/thumbor-request-modifier-http-loader',
  download_url = 'https://github.com/dffrntmedia/thumbor-request-modifier-http-loader',
  keywords = ['thumbor'],
  install_requires=[
    'thumbor',
    'tornado'
  ],
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',
    'Topic :: Software Development',
    'License :: GPL-3.0 License',
    'Programming Language :: Python :: 2'
  ],
)
