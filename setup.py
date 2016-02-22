# https://raw.githubusercontent.com/pypa/sampleproject/master/setup.py

# Although pypa's sampleproject does not bootstrap setuptools, we do, because
# we might want to run this on Python installations which do not have
# setuptools already installed.
#
# See http://pythonhosted.org/setuptools/using.html for further details

try:
    import setuptools
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()

import os

import codecs  # To use a consistent encoding
from pip import download
from pip import req

HERE = os.path.abspath(os.path.dirname(__file__))

def get_requirements(reqfile):
    path = os.path.join(HERE, reqfile)
    deps = set()
    for dep in req.parse_requirements(path, session=download.PipSession()):
        specs = ','.join(''.join(spec) for spec in dep.req.specs)
        requirement = '{name}{extras}{specs}'.format(
            name=dep.name,
            extras=(
                '[{extras}]'.format(extras=','.join(dep.extras))
                if dep.extras else ''
            ),
            specs=specs,
        )

        deps.add(requirement)
    return deps

# Get the long description from the relevant file
with codecs.open(os.path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


# Put here your dependencies for your application
# TODO: This should be filled with requirements/prod-requirements.txt
install_requires = get_requirements('requirements/requirements.txt')
# TODO: This should be filled with requirements/dev-requirements.txt
develop_requires = get_requirements('requirements/dev-requirements.txt')

setuptools.setup(
    name='your_script',
    version=':versiontools:your_script:',

    description='YOUR SCRIPT description, fits here',
    long_description=long_description,

    url='https://dgarana.github.io',

    author='YOUR NAME',
    author_email='you@yourcompany.com',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 2.7',
    ],

    keywords='your script keywords',

    packages=setuptools.find_packages(),

    install_requires=install_requires,
    setup_requires=['versiontools'],

    entry_points={
        'console_scripts': [
            'your_script=your_script.main:main',
        ],
    },
)
