from setuptools import setup, find_packages

setup(
  name='streamlit_push_notifications',
  version='0.1',
  packages=find_packages(),
  description='A Streamlit library for sending browser notifications and alerts',
  author='Wambugu Kinyua',
  author_email='kenliz1738@gmail.com',
  url='https://github.com/wambugu71/streamlit-push-notifications.git', 
  classifiers=[
      'Programming Language :: Python :: 3',
      'License :: OSI Approved :: MIT License',
      'Operating System :: OS Independent',
  ],
  install_requires=[
      'streamlit>=1.0.0', 
  ],
  python_requires='>=3.8',
)
