# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 18:51:40 2024

@author: admin
"""

from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
# Sample inventory data
inventory = []
@app.route('/')
def index():
    return render_template('index.html', inventory=inventory)
@app.route('/add_item', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        item_name = request.form['item_name']
        item_quantity = request.form['item_quantity']
        inventory.append({'name': item_name, 'quantity': item_quantity})
        return redirect(url_for('index'))
    return render_template('add_item.html')
@app.route('/edit_item/<int:item_id>', methods=['GET', 'POST'])
def edit_item(item_id):
    if request.method == 'POST':
        inventory[item_id]['name'] = request.form['item_name']
        inventory[item_id]['quantity'] = request.form['item_quantity']
        return redirect(url_for('index'))
    item = inventory[item_id]
    return render_template('edit_item.html', item=item, item_id=item_id)
if __name__ == '__main__':
    app.run(debug=True)