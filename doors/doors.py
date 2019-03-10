from enum import Enum


class Door(Enum):
    INTERROOM = 'interroom'
    ENTRANCE = 'entrance'

    @classmethod
    def get_categories(cls, category):
        categories = {
            cls.INTERROOM: {
                'name': 'Межкомнатные двери',
                'subcategories': [
                    'Двери из массива',
                    'Складные двери',
                    'Ламинированные двери',
                    'Двери ПВХ',
                    'Экошпон',
                    'Шпонированные двери',
                    'Двери окрашенные (эмаль)',
                    'Раздвижные двери',
                ],
            },
            cls.ENTRANCE: {
                'name': 'Металлические двери',
                'subcategories': [],
            },
        }

        return categories[category]



categories = {
    'interroom': {
        'name': 'Межкомнатные двери',
        'subcategories': [
            'Двери из массива',
            'Складные двери',
            'Ламинированные двери',
            'Двери ПВХ',
            'Экошпон',
            'Шпонированные двери',
            'Двери окрашенные (эмаль)',
            'Раздвижные двери',
        ],
    },
    'entrance': {
        'name': 'Металлические двери',
        'subcategories': [],
    },
}
