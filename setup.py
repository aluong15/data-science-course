from setuptools import setup, find_packages

setup(
    name="DataScienceCourse",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # List your project's dependencies here, e.g.,
        # 'numpy',
        # 'pandas',
    ],
    entry_points={
        'console_scripts': [
            # If you want to create any command-line scripts, list them here
            # 'some-command = some_module.some_function'
        ],
    }
)