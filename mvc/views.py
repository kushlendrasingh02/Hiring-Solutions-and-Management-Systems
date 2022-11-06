from flask import Blueprint, render_template, redirect, url_for

views = Blueprint("views", __name__)

@views.route('/')
@views.route('/home')
def home():
    return render_template('index.html')

@views.route('/about')
def about():
    return render_template('about.html')

@views.route('/error')
def error():
    return render_template('error.html')

@views.route('/contact')
def contact():
    return render_template('contact.html')

@views.route('/pricing')
def pricing():
    return render_template('pricing.html')

@views.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@views.route('/dashboard/jobopenings/applications')
def jobopenings_applications():
    return render_template('jobopenings_applications.html')

@views.route('/dashboard/candidates/applications')
def candidates_applications():
    return render_template('candidates_applications.html')

@views.route('/dashboard/interviews')
def interviews():
    return render_template('interviews.html')

@views.route('/dashboard/clients')
def clients():
    return render_template('clients.html')

@views.route('/dashboard/pricing')
def dashboard_pricing():
    return render_template('dashboard_pricing.html')

@views.route('/dashboard/contactus')
def dashboard_contactus():
    return render_template('dashboard_contactus.html')

@views.route('/dashboard/aboutus')
def dashboard_aboutus():
    return render_template('dashboard_aboutus.html')