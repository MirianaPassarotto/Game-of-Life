from setuptools import setup, find_packages

setup(
    name='game_of_life',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib'
    ],
    
    entry_points={
        'console_scripts': [
            'gameoflife=game_of_life.game:main'
        ]
    },
    
    author='Miriana',
    description='Game of Life implementation using NumPy and Matplotlib',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License'
    ],
    
    python_requires='>=3.10'
)
