from setuptools import setup

setup(
    name='Python IPStack',
    version='1.1',
    url='https://github.com/tamara-bain/python-ipstack',
    license='MIT',
    description='Python wrapper for IPStack.com requests and responses.',
    install_requires=['requests'],

    py_modules=['ipstack'],
    platforms='any',
    test_suite='test_ipstack',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)
