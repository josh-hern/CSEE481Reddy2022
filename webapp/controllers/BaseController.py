from flask import Blueprint, render_template
import os

def viewHome():
    return render_template('pages/home/home.html', test=os.getcwd())
