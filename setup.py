from distutils.core import setup

setup(
  name = 'thumbor-request-modifier-http-loader',
  packages = ['thumbor_request_modifier_http_loader'],
  version = '0.1.4-dev',
  license='GPL-3.0',
  description = 'Custom HTTP loader for Thumbor which allows modifying client request based on certain conditions.',
  author = 'Maksim Barouski',
  author_email = 'maksim.borovskij@yandex.ru',
  url = 'https://github.com/dffrntmedia/thumbor-request-modifier-http-loader',
  download_url = 'https://github.com/dffrntmedia/thumbor-request-modifier-http-loader/archive/0.1.4-dev.tar.gz',
  keywords = ['thumbor'],
  install_requires=[
    'thumbor',
    'tornado'
  ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Libraries',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7'
  ],
)
