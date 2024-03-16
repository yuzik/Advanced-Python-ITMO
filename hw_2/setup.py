from setuptools import setup, find_packages

setup(
    name='latex_generator_itmo_yuzik',
    version='0.1.0',
    packages=find_packages(),
    description='Simple LaTeX document generator with image inclusion.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Joseph Ya',
    author_email='yuzik.74@gmail.com',
    url='https://github.com/yuzik/Advanced-Python-ITMO/HW_2',
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ]
)
