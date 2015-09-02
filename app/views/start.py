# -*- coding: utf-8 -*-
from flask import render_template, redirect, url_for, flash, jsonify
from flask_classy import FlaskView, route
from flask_security import login_required, current_user
from app import db


class StartView(FlaskView):
    decorators = [login_required]
    route_base = '/start/'

    def index(self):
        if current_user.is_evaluate:
            return redirect(url_for('MainView:recommend'))
        else:
            return render_template('start/index.html')

    def post(self):
        if not current_user.is_evaluate:
            current_user.is_evaluate = True
            db.session.commit()
        else:
            flash('You are already evaluated')
            return redirect(url_for('MainView:recommend'))

        return redirect(url_for('StartView:evaluate'))

    def evaluate(self):
        flash('Your information successfully evaluated!')
        return redirect(url_for('MainView:recommend'))

    @route('/getfoodlist/', methods=['GET'])
    def getfoodlist(self):
        return jsonify({'foodlist' : [
            {'id' : 1, 'foodName' : '된장찌개', 'image' : 'http://ftp.fs25.co.kr/wp-content/uploads/sites/14/2014/08/abr2.jpg'},
            {'id' : 2, 'foodName' : '김치찌개', 'image' : 'http://cfs13.tistory.com/image/15/tistory/2009/01/25/01/56/497b4820e8269'},
            {'id' : 3, 'foodName' : '햄버거', 'image' : 'http://cfile9.uf.tistory.com/image/252C664051A3222E18F4EB'},
            {'id' : 4, 'foodName' : '사과', 'image' : 'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcT3jSOMkNfn00XEtHXvLm7c4vH_szmyWTIoHriAZ5p6dUMkSaXc'},
            {'id' : 5, 'foodName' : 'banana', 'image' : 'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcT3jSOMkNfn00XEtHXvLm7c4vH_szmyWTIoHriAZ5p6dUMkSaXc'},
            {'id' : 6, 'foodName' : 'banana', 'image' : 'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcT3jSOMkNfn00XEtHXvLm7c4vH_szmyWTIoHriAZ5p6dUMkSaXc'},
            {'id' : 7, 'foodName' : 'banana', 'image' : 'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcT3jSOMkNfn00XEtHXvLm7c4vH_szmyWTIoHriAZ5p6dUMkSaXc'},
            {'id' : 8, 'foodName' : 'banana', 'image' : 'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcT3jSOMkNfn00XEtHXvLm7c4vH_szmyWTIoHriAZ5p6dUMkSaXc'},
            {'id' : 9, 'foodName' : 'banana', 'image' : 'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcT3jSOMkNfn00XEtHXvLm7c4vH_szmyWTIoHriAZ5p6dUMkSaXc'},
            {'id' : 10, 'foodName' : 'banana', 'image' : 'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcT3jSOMkNfn00XEtHXvLm7c4vH_szmyWTIoHriAZ5p6dUMkSaXc'}
        ]})
