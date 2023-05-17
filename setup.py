from setuptools import setup

setup(
    name="tech_news",
    description="Projeto Tech News",
    install_requires=[
        "parsel==1.7.0",
        "requests==2.24.0",
        "pymongo==3.11.0",
        "python-decouple==3.3",
    ],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "run-scraper=tech_news.menu:analyzer_menu",
        ],
    },
)
