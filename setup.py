from setuptools import find_packages, setup

setup(
    name='ChatBotGPT3',
    packages=find_packages(include=['ChatBotGPT3']),
    version='0.1.0',
    description='A library to easily create a chatbot with context and chat.',
    author='kasdmusic',
    license='MIT',
    install_requires=['openai'],
)