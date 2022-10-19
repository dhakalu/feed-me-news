from setuptools import find_packages, setup, find_namespace_packages


with open("README.md", 'r') as file:
    long_description = file.read()

with open("requirements.txt", 'r') as requirements_file:
    dependencies = list(map(lambda x: x.strip(), requirements_file.readlines()))

print(dependencies)

setup(
    name='feed',
    version="0.0.4",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Upen Dhakal<dhakal.upenn@gmail.com>",
    install_requires=dependencies,
    packages=find_packages(),
    url="https://github.com/dhakalu/feed-me-news"
)