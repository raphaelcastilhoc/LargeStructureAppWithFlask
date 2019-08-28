from flask import render_template
from flask import render_template, redirect, url_for, abort, flash
from . import main
from models.auth import User
from .forms.auth.auth_form import EditProfileForm

@main.route('/', methods=['GET'])
def index():
    return render_template('main/index.html')

@main.route('/user/<userName>')
def user(userName):
    user = User(userName, 'jf', 'developer')
    return render_template('auth/user.html', user=user)

@main.route('/user/edit-profile', methods=['GET', 'POST'])
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        user = User(form.name.data, form.location.data, form.aboutMe.data)
        flash('Your profile has been updated.')
        return redirect(url_for('.user', userName=user.name))
    form.name.data = 'Castilho'
    form.location.data = 'jf'
    form.aboutMe.data = 'developer'
    return render_template('auth/edit_profile.html', form=form)