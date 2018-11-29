# -*- coding: utf-8 -*-
from django.test import TestCase

# Create your tests here.
import datetime
from django.utils import timezone

from .models import Question

from django.urls import reverse

"""
class QuestionModelTests(TestCase):
    '''
    def test_1(self):
        futureTime = timezone.now() + datetime.timedelta(days=30)
        fQ = Question(pub_date=futureTime)

                                    #함수 실행 결과가 False 가 아니면 오류 나게 설정
        self.assertIs(fQ.was_published_recently(),False)
    '''

    #테스트 케이스를 작성 할 때는 입력을 세부화 해서 입력에따라 함수를 나눈다.

    def test_future(self):
        futureTime = timezone.now() + datetime.timedelta(days= 30)
        fQuestion = Question(pub_date=futureTime)

        self.assertIs(fQuestion.was_published_recently(), False)

    def test_now(self):
        nowTime = timezone.now()
        nQuestion = Question(pub_date=nowTime)

        self.assertIs(nQuestion.was_published_recently(), True)

    def test_past_1_day_less(self):
        lessTime = timezone.now() - datetime.timedelta(hours=10)
        lQuestion = Question(pub_date=lessTime)

        self.assertIs(lQuestion.was_published_recently(), True)

"""

def createQuestionByDays(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question(question_text=question_text,
                    pub_date= time)

class QuestionIndexViewTests(TestCase):

    # 뷰 테스트를 위한 함수들
    def test_no_questions(self):
        response = self.client.get(reverse('polls:index'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")

        self.assertQuerysetEqual(response.contxt['latest_question_list'],[])

