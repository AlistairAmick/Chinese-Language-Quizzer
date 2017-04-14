try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Quizzes the user on their knowledge of Chinese',
    'author': 'Alistair Amick',
    'url': 'https://github.com/AlistairAmick/Chinese-Language-Quizzer',
    'author_email': 'aamickWork@tutamail.com',
    'version': '1.1.1',
    'install_requires': ['nose'],
    'packages': ['language_game'],
    'scripts': ['language_game/main.py', 'language_game/score.py',
                'language_game/rungame.py',	'language_game/lessonarchive.py',
                'language_game/lesson1.py', 'language_game/lesson2.py', 'language_game/lesson3.py',],
    'name': 'Chinese-Language-Quizzer'
}

setup(**config)
