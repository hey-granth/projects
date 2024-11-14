from flask import Flask, Blueprint, render_template

main = Blueprint('main', __name__)


@main.route('/')
def index():  # put application's code here
    projects = [
        {'name': "Project 1", 'description': '.....', 'docs_url': "/docs/projects/project1"}
    ]
    return render_template('index.html', projects=projects)


@main.route('/projects/<project_name>')
def project(project_name):
    project_details = []
    return render_template('project.html', project=project_details)