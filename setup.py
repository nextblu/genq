import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt") as fp:
    install_requires = fp.read()

setuptools.setup(
    name='genq',
    version='0.1.0',
    description='Query builder for Python',
    author='NextBlu',
    author_email='hello@nextblu.com',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    packages=setuptools.find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    url='https://github.com/nextblu/genq',
    install_requires=install_requires,
    python_requires='>=3.6.0',
    include_package_data=True
)
