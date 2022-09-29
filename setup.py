import os
from setuptools import setup, find_packages

def src(pth):
    return os.path.join(os.path.dirname(__file__), pth)

# Project description
descr = 'Seismic_PnP'

setup(
    name="package", # Choose your package name
    description=descr,
    long_description=open(src('README.md')).read(),
    keywords=['inverse problems',
              'deep learning',
              'seismic'],
    classifiers=[
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Scientific/Engineering :: Mathematics'
    ],
    author='Juan Romero, Miguel Corrales, Nick Luiken, Matteo Ravasi',
    author_email='juan.romeromurcia@kaust.edu.sa, miguel.corrales@kaust.edu.sa, nicolaas.luiken@kaust.edu.sa, matteo.ravasi@kaust.edu.sa',
    install_requires=['numpy >= 1.15.0',
                      'torch >= 1.2.0',
                      'pylops >= 1.17.0'],
    packages=find_packages(),
    use_scm_version=dict(root='.',
                         relative_to=__file__,
                         write_to=src('package/version.py')),
    setup_requires=['setuptools_scm'],

)
