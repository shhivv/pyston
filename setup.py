from distutils.core import setup
setup(
  name = 'pyston',
  packages = ['pyston'],
  version = '1.0.0',
  license='MIT',
  description = 'An asynchronous API wrapper for the Piston API',
  author = 'Fang',
  url = 'https://github.com/ffaanngg/pyston',
  download_url = 'https://github.com/ffaanngg/pyston/archive/refs/tags/1.0.0.tar.gz',
  keywords = ['Pyston', 'Piston API', 'API wrapper'],
  install_requires=[
          'aiohttp',
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)