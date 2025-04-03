from setuptools import setup, find_packages

setup(
    name="eddmPrint",
    version="0.1.2",
    packages=find_packages(), 
    install_requires=[],
    author="eddmpython",
    author_email="eddmpython@gmail.com",
    description="색상과 위치 정보가 포함된 개선된 프린트 라이브러리",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/eddmpython/eddmPrint",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
) 