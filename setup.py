from distutils.core import setup
from prelude import __version__
import os

URL='https://github.com/hircus/python-prelude'

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='prelude',
      version=__version__,
      author='Michel Alexandre Salim',
      author_email='michel@sylvestre.me',
      url=URL,
      download_url=('%s/zipball/%s' % (URL, __version__)),
      description='Prelude library of functional programming constructs',
      license='MIT',
      long_description=read('README.rst'),
      packages=['prelude'],
      data_files=[('.', ['LICENSE', 'AUTHORS.rst', 'TODO.rst']),
                  ],
      install_requires=[],
      classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
      )
