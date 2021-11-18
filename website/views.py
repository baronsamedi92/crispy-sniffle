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

    def onclick(args):
        if args == 1:
         flash('CLICK1')
        if args == 2:
         flash('CLICK2')
    root = tk.Tk()
    root.title('GUI BUTTON')

    btn1 = tk.Button(root, text="BUTTON1",command=lambda:onclick(1))
    btn2 = tk.Button(root, text="BUTTON1",command=lambda:onclick(2))

    with open("website/poll1.json", "r") as f:
     data = json.loads(f.read())
    question = data['question']
    casparOptions = data['caspar_options']
    casparDesctiption = data['question_desc']
    
   
    def getDaPoll():
     for k,v in casparOptions.items():
         x = []
         x.append(k+v)
     return x
     
    #flash(getDaPoll())

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
     
   

    flash(answer1)
    flash(answer2)
    flash(answer3)
    flash(answer4)
    
    

    

     



    #flash(data['question'])
    #flash(data['caspar_options']['option1'])
    
    
    return render_template("datBoy.html", pollQuestion=question, pollDescription=casparDesctiption, pollOptions=answerContainer)