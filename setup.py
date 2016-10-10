"""Install setup."""
import setuptools

setuptools.setup(
    name="bgbl",
    version="0.0.1",
    url="git@github.com:xguse/big-gus-brewing-labs.git",

    author="Gus Dunn",
    author_email="w.gus.dunn@gmail.com",

    description="A re-awakening of the Big Gus Brewing Company habit of my mid 20s mixed with my aquired reproducible science and data-science affinities.",
    # long_description=open('README.rst').read(),

    packages=setuptools.find_packages('src/python'),


    install_requires=["click",
                      "munch",
                      "seaborn",
                      "pandas",
                      "numexpr",
                      "numpy",
                      "xlrd",
                      "xlwt",
                      ],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
