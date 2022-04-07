from setuptools import setup, find_packages

with open("Readme.md", "r") as readme_file:
    readme = readme_file.read()

setup(
    name='Huobi Pool api',
    version='0.1.0',
    license='MIT',
    author="Inkviz96",
    author_email='b-semen-b@mail.ru',
    packages=find_packages(),
    python_requires='>=3.8',
    url='https://github.com/inkviz96/huobi_api_python',
    keywords='huobi api pool',
    description="Huobi Pool api lib for easy work with huobi",
    long_description=readme,
    long_description_content_type="text/markdown",
    install_requires=[
          'requests',
      ],
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
