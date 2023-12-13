from setuptools import find_packages, setup

setup(
    name="foo",
    version="0.0.1",
    packages=find_packages(),
    package_data={
        "foo": [
            "dbt-project/**/*",
        ],
    },
    install_requires=[
        "dagster",
        "dagster-cloud",
        "dagster-dbt",
        "dbt-core>=1.4.0",
        "dbt-redshift",
        "dbt-redshift",
        "dbt-snowflake",
        "dbt-bigquery",
        "dbt-postgres",
        "dbt-postgres",
    ],
    extras_require={
        "dev": [
            "dagster-webserver",
        ]
    },
)

