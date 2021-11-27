from operator import indexOf
import re
from flask import Blueprint, render_template, request, flash, redirect
import flask
from flask_login import login_required, current_user
from .models import Note
from . import db
import json
from datetime import date
import tkinter as tk
import os



views = Blueprint('views', __name__)

def getPoll(JsonFile):

    with open(JsonFile, "r") as f:
     data = json.loads(f.read())
    return data

directory_in_str = "website/jsonFiles/"
def sortDirectory():
    directory = sorted(os.listdir(unsortedDirectory))
    return directory
unsortedDirectory = os.fsencode(directory_in_str)
directory = sorted(os.listdir(unsortedDirectory))
fileNameArray = []

for count, file in enumerate(directory):
     filename = os.fsdecode(file)
     fileNameArray.append(filename)
print(count)


    

#allPolls = getPoll('website/allPolls.json')



@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home.html")

@views.route('/poll-deleted', methods=['GET', 'POST'])
def pollDeleted():
    return render_template("poll-deleted.html")

@views.route('/DatBoy', methods=['GET', 'POST'])
def datBoy():
    directory_in_str = "website/jsonFiles/"
    directory = os.fsencode(directory_in_str)
    fileNameArray = []

    for count, file in enumerate(os.listdir(directory)):
     filename = os.fsdecode(file)
     fileNameArray.append(filename)
     print(count)
    
    print(count)

    allPolls = getPoll("website/jsonFiles/allPolls.json")
    pollsIteratedAndBrokenUpForStupidPython = []
    for i in (range( 1, len(allPolls)+1)):
     pollsIteratedAndBrokenUpForStupidPython.append(allPolls['poll'+str(i)])

    data = getPoll("website/jsonFiles/poll_template.json")
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

    return render_template("datBoy.html", pollQuestion=question, pollDescription=casparDesctiption, 
    pollOptions=answerContainer, isActive=isActive, count=count, polls=fileNameArray)


@views.route('/<str>', methods=['GET', 'POST'])  # /PollXYZ
def pollPages(str):

#sort the directory and set up the poll

    directory_in_str = "website/jsonFiles/"
    directory = os.fsencode(directory_in_str)
    fileNameArray = []

    for count, file in enumerate(os.listdir(directory)):
     filename = os.fsdecode(file)
     fileNameArray.append(filename)
     print(count)
    
    print(count)
    data = getPoll("website/jsonFiles/"+str)
    sortDirectory()
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
    pollName = str[:len(str)-5]
   

    #data['poll_active'] = True
    #with open("website/casparJsonFIle/poll.json", "w+") as f:
     #json.dump(data, f, indent=4)
   
    #data['poll_active'] = False
    #with open("website/casparJsonFIle/poll.json", "w+") as f:
     #json.dump(data, f)
    #os.remove("website/jsonFiles/"+str)

     #Check Buttons if none was clicked just go on with the data loading
    if 'activate' in flask.request.url:
        flash('DING IS AKTIV')
        data['poll_active'] = True
        with open("website/casparJsonFIle/poll.json", "w+") as f:
         json.dump(data, f, indent=4)
        with open("website/jsonFiles/"+str, "w+") as file:
         json.dump(data, file, indent=4)
    elif 'offline' in flask.request.url:
        pass 
        data['poll_active'] = False
        with open("website/casparJsonFIle/poll.json", "w+") as f:
         json.dump(data, f, indent=4)
        with open("website/jsonFiles/"+str, "w+") as file:
         json.dump(data, file, indent=4)
    elif 'delete' in flask.request.url:
        pass # do something else
        os.remove("website/jsonFiles/"+str)
        flash(pollName + " is nu im Müll.", category="info")
        return redirect("/DatBoy?file-deleted", code=302)
    elif 'LIVE' in flask.request.url:
        pass # do something else
        os.remove("website/jsonFiles/"+str)
        flash(pollName + "WE LIFE BOIS", category="info")
    

    else:
        pass # unknown
    

    return render_template("datBoy.html", pollQuestion=question, pollDescription=casparDesctiption, pollOptions=answerContainer, isActive=isActive,
    count=count, polls=fileNameArray, pollName=pollName, url=str)

@views.route('/poll-deleted', methods=['GET', 'POST'])
def activate():
    return "OH SHIT OH SHIT OH SHIT"

    





@views.route('/DatBoy', methods=['GET', 'POST'])
def getDatBoy():

    with open("website/jsonFiles/poll1.json", "r") as f:
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

@views.route('/form', methods=['GET', 'POST'])
def form():

    with open("website/jsonFiles/poll_template.json", "r+") as f:
     newPoll = json.loads(f.read())
#get input from poll
    inputPollName = request.form.get('inputPollName')
    inputQuestion = request.form.get('inputQuestion')
    inputQuestionDesc = request.form.get('inputQuestionDesc')
    inputOption1 = request.form.get('inputOption1')
    inputOption2 = request.form.get('inputOption2')
    inputOption3 = request.form.get('inputOption3')
    inputOption4 = request.form.get('inputOption4')
    inputCheckbox = request.form.get('gridCheck')

#pare input into new poll
    newPoll['poll_active'] = inputCheckbox
    newPoll['question'] = inputQuestion
    casparOptions = newPoll['caspar_options']
    newPoll['question_desc'] = inputQuestionDesc
    casparOptions['option1'] = inputOption1
    casparOptions['option2'] = inputOption2
    casparOptions['option3'] = inputOption3
    casparOptions['option4'] = inputOption4

    with open("website/jsonFiles/"+str(inputPollName)+".json", "w+") as f:
         json.dump(newPoll, f)


    return render_template("form.html", pollName= inputPollName)
