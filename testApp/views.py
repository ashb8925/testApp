from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.views import View
from .models import MCQs
from random import sample
import numpy as np
# Create your views here.



class HomePage(View):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.all = {}
    def get(self, request, *args, **kwargs):
        # creating a dict to store question id as key and its answer as value
        all = {}
        mcqs = MCQs.objects.all()
        end_range = len(mcqs)
        random_ques = sample(range(0, end_range), 3)
        questions = [mcqs[i] for i in random_ques]
        answers = [q.ans for q in questions]

        print(len(mcqs))
        for i in range(len(questions)):
           # self.all[questions[i].id] = answers[i]
            self.all[questions[i].id] = answers[i]
        print('answers ',answers)
        print('all ', self.all)
        print('questions', questions)
        request.session['all'] = self.all


        return render(request, 'testpage.html', {'questions': questions, 'all': self.all})
    def post(self, request, *args, **kwargs):
        mcqs = MCQs.objects.all()
        mcqs_dic = {mcq.id: mcq.ques for mcq in mcqs}
        values = request.session.get('all')
        questions = list(values.keys())
        #ques_ids = list(values.keys())
        #questions = [i for i in values.keys()]
        #ques_ids = np.array(ques_ids)
        #ques_ids = [str(i) for i in ques_ids]
        #ques_ids = np.array(list(values.keys()))
        print('msqs_dic', mcqs_dic)
        print('ques_ids', questions)
        print('values', values)
        score = 0
        skip = True
        for key, value in request.POST.items():
            print(key, value)
            if skip:
                skip = False
            else:
                if values[key] == value:
                    score+= 1
        return render(request, 'result.html', {'score': score , 'mcqs_dic': mcqs_dic, 'questions': questions} )

