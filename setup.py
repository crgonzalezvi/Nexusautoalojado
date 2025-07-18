from setuptools import setup, find_packages

setup(
    name="store-api",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "fastapi",
        "uvicorn",
        "prometheus_client",
        "requests"
    ],
    entry_points={
        "console_scripts": [
            "start-api=run:main"
        ]
    },
)
