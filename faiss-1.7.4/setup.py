from setuptools import setup, Extension, find_packages
import numpy
import os

# Find the build directory
build_dir = os.path.join(os.getcwd(), 'build')

setup(
    name='faiss-cpu',
    version='1.7.4',
    description='Faiss library for efficient similarity search and clustering of dense vectors',
    packages=find_packages(),
    ext_modules=[
        Extension(
            'faiss',
            sources=[],
            include_dirs=[
                numpy.get_include(), 
                os.path.join(os.getcwd(), 'build/_deps/faiss-src'),
                os.path.join(os.getcwd(), 'build/_deps/faiss-src/faiss')
            ],
            library_dirs=[
                build_dir,
                os.path.join(build_dir, 'lib'),
                os.path.join(build_dir, 'faiss')
            ],
            libraries=['faiss']
        )
    ],
    install_requires=[
        'numpy>=1.20.0'
    ]
)
