from setuptools import setup, find_packages

setup(
    name='main',  # یا هر اسمی که دوست داری برای پکیج
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'jdatetime',
        'googletrans==4.0.0-rc1'
    ],
    author='tpas',
    description='کتابخانه هوشمند برای تاریخ، ترجمه و ذخیره‌سازی فایل',
    python_requires='>=3.6',
)

