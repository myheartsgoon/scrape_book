# coding=utf-8
from flask import Flask, render_template, request, redirect, session, url_for, flash
from datetime import timedelta
import capture_ysqc

app = Flask(__name__)


@app.before_request
def make_session_permant():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=20)

app.secret_key = 'development-key'


@app.route('/')
def home():
    book_info = [("一世倾城","苏小暖", 11133, "ysqc")]
    # with open("books", "r") as f:
    #     for line in f:
    #         book_info.append(line.split())
    return render_template("home.html", book_info=book_info)

@app.route('/ysqc')
def ysqc():
    chapters_list = capture_ysqc.capture_chapter_list()
    return render_template("ysqc.html", chapters_list=chapters_list)

@app.route('/ysqc_chapter')
def ysqc_chapter():
    chapter_url = request.args.get('url')
    chapter_no = request.args.get('chapter')
    content = capture_ysqc.capture_content(chapter_url)
    return render_template("chapter.html", content=content, chapter_no=chapter_no)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run('0.0.0.0', port=5000, debug=True)
