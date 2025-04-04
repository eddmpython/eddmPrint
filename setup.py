from setuptools import setup, find_packages
import os


this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="eddmPrint",
    version="0.1.3",
    packages=find_packages(), 
    install_requires=[],
    author="eddmpython",
    author_email="eddmpython@gmail.com",
    description="색상과 위치 정보가 포함된 개선된 프린트 라이브러리 - 자동 초기화 및 다양한 출력 형식 지원",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/eddmpython/eddmPrint",
    keywords=["print", "logging", "color", "debug", "console"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    python_requires=">=3.6",
) 