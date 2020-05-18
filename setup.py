import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="elemental_analysis_scripts",
    version="0.0.1",
    url = 'https://github.com/elemental-analysis-group/elemental-analysis-scripts.git',
    description="elemental-analysis-scripts package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Thiago Gomes Veríssimo",
    author_email="verissimotgv@gmail.com",
    packages=setuptools.find_packages(),
    install_requires=['pyxray>=1.3','numpy>=1.14.1'],
)
