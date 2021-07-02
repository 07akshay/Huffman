from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3',
  'Programming Language :: Python :: 3.4',
  'Programming Language :: Python :: 3.5',
  'Programming Language :: Python :: 3.8',
  'Programming Language :: Python :: 3.9'
]
 
setup(
  name='akcompress',
  version='0.0.1',
  description='Based of huffman compression',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Akshay Kumar',
  author_email='akshaykrsingh490@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='compression', 
  packages=find_packages(),
  install_requires=['']
)