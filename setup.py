import setuptools

setuptools.setup(
    name="wgit",
    version="0.0.1",
    author="Ericson Joseph",
    author_email="ericsonjoseph@gmail.com",
    description="Wrapper of git for multiple accounts and servers",
    scripts=['wgit'],
    url="https://github.com/ericsonj/wgit",
    license="MIT",
    packages=setuptools.find_packages(),
    install_requires=[
        'giturlparse',
        'ssh_agent_setup'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
