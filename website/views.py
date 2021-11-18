from operator import indexOf
import re
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json
from datetime import date
import tkinter as tk



views = Blueprint('views', __name__)

def getPoll(JsonFile):

    with open(JsonFile, "r") as f:
     data = json.loads(f.read())
    return data



@views.route('/', methods=['GET', 'POST'])
def home():
    
    if request.method == 'POST':
        note = request.form.get('note')
        question = request.form.get('question');
        print('HIER STEHT AUCH WAS HALLO', question);

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')
            print('##1###',note)

        

    return render_template("home.html", user=current_user)

@views.route('/Poll1', methods=['GET', 'POST'])
def poll1():
   #holy shit thats redundant af -> fix this mess
    data = getPoll("website\poll1.json")
    isActive = data['poll_active']
    question = data['question']
    casparOptions = data['caspar_options']
    casparDesctiption = data['question_desc']
    answer1 = casparOptions['option1']
    answer2 = casparOptions['option2']
    answer3 = casparOptions['option3']
    answer4 = casparOptions['option4']
    answerContainer = []
    answerContainer.append(answer1)
    answerContainer.append(answer2)
    answerContainer.append(answer3)
    answerContainer.append(answer4)
    return render_template("datBoy.html", pollQuestion=question, pollDescription=casparDesctiption, pollOptions=answerContainer, isActive=isActive)

@views.route('/Poll2', methods=['GET', 'POST'])
def poll2():
   #holy shit thats redundant af -> fix this mess
    data = getPoll("website\poll2.json")
    isActive = data['poll_active']
    question = data['question']
    casparOptions = data['caspar_options']
    casparDesctiption = data['question_desc']
    answer1 = casparOptions['option1']
    answer2 = casparOptions['option2']
    answer3 = casparOptions['option3']
    answer4 = casparOptions['option4']
    answerContainer = []
    answerContainer.append(answer1)
    answerContainer.append(answer2)
    answerContainer.append(answer3)
    answerContainer.append(answer4)
    return render_template("datBoy.html", pollQuestion=question, pollDescription=casparDesctiption, pollOptions=answerContainer, isActive=isActive)


@views.route('/Poll3', methods=['GET', 'POST'])
def poll3():
   #holy shit thats redundant af -> fix this mess
    data = getPoll("website\poll3.json")
    isActive = data['poll_active']
    question = data['question']
    casparOptions = data['caspar_options']
    casparDesctiption = data['question_desc']
    answer1 = casparOptions['option1']
    answer2 = casparOptions['option2']
    answer3 = casparOptions['option3']
    answer4 = casparOptions['option4']
    answerContainer = []
    answerContainer.append(answer1)
    answerContainer.append(answer2)
    answerContainer.append(answer3)
    answerContainer.append(answer4)
    return render_template("datBoy.html", pollQuestion=question, pollDescription=casparDesctiption, pollOptions=answerContainer, isActive=isActive)


@views.route('/Poll4', methods=['GET', 'POST'])
def poll4():
   #holy shit thats redundant af -> fix this mess
    data = getPoll("website\data.json")
    isActive = data['poll_active']
    question = data['question']
    casparOptions = data['caspar_options']
    casparDesctiption = data['question_desc']
    answer1 = casparOptions['option1']
    answer2 = casparOptions['option2']
    answer3 = casparOptions['option3']
    answer4 = casparOptions['option4']
    answerContainer = []
    answerContainer.append(answer1)
    answerContainer.append(answer2)
    answerContainer.append(answer3)
    answerContainer.append(answer4)
    return render_template("datBoy.html", pollQuestion=question, pollDescription=casparDesctiption, pollOptions=answerContainer, isActive=isActive)



@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

@views.route('/DatBoy', methods=['GET', 'POST'])
def getDatBoy():

    with open("website/poll1.json", "r") as f:
     data = json.loads(f.read())
    question = data['question']
    casparOptions = data['caspar_options']
    casparDesctiption = data['question_desc']

#holy shit thats redundant af -> fix this mess
    answer1 = casparOptions['option1']
    answer2 = casparOptions['option2']
    answer3 = casparOptions['option3']
    answer4 = casparOptions['option4']
    answerContainer = []
    answerContainer.append(answer1)
    answerContainer.append(answer2)
    answerContainer.append(answer3)
    answerContainer.append(answer4)
    return render_template("datBoy.html", pollQuestion=question, pollDescription=casparDesctiption, pollOptions=answerContainer)

@views.route('/createPoll', methods=['GET', 'POST'])
def createPoll():
   
    return render_template("createPoll.html")