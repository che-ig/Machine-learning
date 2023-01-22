"""Модуль реализующий наивный Байес."""

from __future__ import annotations

import math
import re
from collections import defaultdict
from enum import Enum
from pathlib import Path
from typing import Dict, List, NamedTuple, Set

# Прикладные типы данных.
Dictwords = Dict[str, List[int]]

separator: str = '###'


def get_prepared_data(path: Path, result_file: Path) -> None:
    """Проходим по всем файлам и выясняем тип сообщения по названию файла."""
    for file in path.glob('*'):
        if file.is_dir():
            get_prepared_data(file, result_file)
        else:
            if 'ham' in str(file):
                message_type = MessageType.SPAM.value
            else:
                message_type = MessageType.NOT_SPAM.value

            write_file(file, result_file, message_type)


def write_file(file_path: Path, result_file: Path, message_type: str) -> None:
    """Записываем в результирующий файл тип сообщения и текст сообщения."""
    with file_path.open(errors='replace') as doc:
        for line in doc:
            if line.startswith('Subject:'):
                # Удалим начальное слово Subject: и
                # возьмем все остальное
                subject = re.sub('(^Subject\:)?([rR]e\:)?(\[.*\])?', '',
                                 line).lower().strip()
                if not result_file.exists():
                    result_file.touch()

                with result_file.open(mode='a') as file_to:
                    file_to.write(f'{message_type} {separator} {subject}\n')


class MessagesCount(NamedTuple):
    spam: int
    not_spam: int


class MessageProb(NamedTuple):
    spam: float
    not_spam: float


class MessageType(Enum):
    SPAM = 'spam'
    NOT_SPAM = 'not_spam'


class NaiveBayesClassifier:
    """Класс, реализующий алгоритм наивного Байеса."""
    def __init__(self: NaiveBayesClassifier,
                 *,
                 data_source: Path,
                 coef: float = 0.5) -> None:
        """Конструктор класса."""
        # Константа сглаживания.
        self.coef = coef
        self.data_source = data_source
        self.word_probs: Dict = {}

    @staticmethod
    def get_words_from_message(message: str) -> Set[str]:
        """Возвращает множество уникальных слов из сообщения."""
        low_message = message.lower()
        # Извлекаем слова из сообщения.
        all_words = re.findall('[a-z0-9]+', low_message)
        return set(all_words)

    def spam_probability(self: NaiveBayesClassifier,
                         message: str) -> MessageProb:
        """Возвращаем вероятность, что данное сообщение является спамом."""
        message_words = self.get_words_from_message(message)
        log_prob_if_spam: float = 0
        log_prob_not_spam: float = 0

        for word in message_words:
            # Если слово есть в словаре, то добавляем логарифм вероятности.
            if word in self.word_probs:
                log_prob_if_spam += math.log(
                    self.word_probs[word]['prob_spam'])
                log_prob_not_spam += math.log(
                    self.word_probs[word]['prob_not_spam'])

        probability_spam = math.exp(log_prob_if_spam)
        probability_not_spam = math.exp(log_prob_not_spam)
        return MessageProb(probability_spam, probability_not_spam)

    def count_words(self: NaiveBayesClassifier) -> Dictwords:
        """Подсчитываем встречаемость слов в спам и неспам сообщениях."""
        # defaultdict возвращает словарь с дефолтным зн.
        # для любого нового ключа.
        counts: Dictwords = defaultdict(lambda: [0, 0])

        with self.data_source.open() as source:
            for line in source:
                if line.find(separator) < 0:
                    continue

                # Обучающая выборка состоит из пар (спам ### сообщение)
                is_spam, message = line.split(separator)

                for word in self.get_words_from_message(message):
                    counts[word][0 if is_spam else 1] += 1

        return counts

    def get_count_messages(self: NaiveBayesClassifier) -> MessagesCount:
        """Возвращает количество спамовых сообщений в наборе данных."""
        spam_count: int = 0
        not_spam_count: int = 0

        with self.data_source.open() as source:
            for line in source:
                if line.find(separator) < 0:
                    continue

                message_type, _ = line.split(separator)
                if message_type.strip() == MessageType.SPAM.value:
                    spam_count += 1
                else:
                    not_spam_count += 1
        return MessagesCount(spam_count, not_spam_count)

    # Вероятность слов
    def word_probabilities(self: NaiveBayesClassifier, counts: Dictwords,
                           total_spams: int, total_non_spams: int) -> Dict:
        """Преобразовать частотности слов в список именованных кортежей."""
        # Здесь вероятность каждого слова при условии спам или не спама
        # вычисляеся по формуле из книги - Грас Джоэл.
        # Наука о данных с нуля (194 стр.)

        return {
            word: {
                'prob_spam':
                (self.coef + spam) / (2 * self.coef + total_spams),
                'prob_not_spam':
                (self.coef + not_spam) / (2 * self.coef + total_non_spams)
            }
            for word, (spam, not_spam) in counts.items()
        }

    def train(self: NaiveBayesClassifier) -> None:
        """Обучение классификатора при помощи обучающей выборки."""
        spam_count, not_spam_count = self.get_count_messages()

        # Пропустим обучающую выборку через метод подсчета слов.
        word_counts = self.count_words()
        self.word_probs = self.word_probabilities(word_counts, spam_count,
                                                  not_spam_count)

    def classify(self: NaiveBayesClassifier, message: str) -> MessageProb:
        """Возвращаем вероятности спама и неспама."""
        return self.spam_probability(message)


if __name__ == '__main__':
    sources_path = Path.home() / 'spam'
    total_file = sources_path / 'data.csv'

    if not total_file.exists():
        # Собираем все данные в единый файл
        get_prepared_data(sources_path, total_file)

    nb = NaiveBayesClassifier(data_source=total_file)
    nb.train()
    # Проверка сооющения на спам.
    prob_spam, prob_not_spam = nb.classify('New testing packages')
    print(prob_spam, prob_not_spam)
