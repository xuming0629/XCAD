from setuptools import setup, find_packages

setup(
    name="XCAD",
    version="0.1.0",
    description="XCAD PyQt5 Ribbon 控件库",
    author="XuMing",
    author_email="920972751@qq.com",
    packages=find_packages(),  # 不再指定 where
    python_requires=">=3.11",
    install_requires=[
        "PyQt5>=5.15",
        # "pythonocc-core>=7.9",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
