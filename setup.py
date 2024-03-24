from setuptools import setup

setup(
    name='email_api',
    version='0.2',
    packages=['email_api'],
    install_requires=[
        'requests',
    ],
    description='quickly get the verification code from the temp email',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',  # 添加这一行
    author='XuHongsheng',
    author_email='xuhongsheng5@outlook.com',
    license='MIT',
    keywords='email temp email verification code',
    url='https://github.com/xu0329',
    platforms='any',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)