from flask import Blueprint, render_template
import os

def viewHome():
    return render_template('pages/home/home.html')

def viewAbout():
    return render_template('pages/about/about.html')

def viewHistory():
    return render_template('pages/history/history.html')

def viewMerch():
    return render_template('pages/merch/merch.html')
