from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Contact

app = Flask(__name__)

engine = create_engine('sqlite:///addressbook.db?check_same_thread=False')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
@app.route('/contacts')
def showContacts():
    contacts = session.query(Contact).all()
    return render_template("contacts.html", contacts=contacts)


@app.route('/contacts/new/', methods=['GET', 'POST'])
def newContact():
    if request.method == 'POST':
        newContact = Contact(name=request.form['name'], surname=request.form['surname'], phone=request.form['phone'],
                             birthday=request.form['birthday'], email=request.form['email'],
                             address=request.form['address'])
        session.add(newContact)
        session.commit()
        return redirect(url_for('showContacts'))
    else:
        return render_template('newContact.html')


@app.route("/contacts/<int:contact_id>/edit/", methods=['GET', 'POST'])
def editContact(contact_id):
    editedContact = session.query(Contact).filter_by(id=contact_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedContact.name = request.form['name']
        if request.form['surname']:
            editedContact.surname = request.form['surname']
        if request.form['phone']:
            editedContact.phone = request.form['phone']
        if request.form['birthday']:
            editedContact.birthday = request.form['birthday']
        if request.form['email']:
            editedContact.email = request.form['email']
        if request.form['address']:
            editedContact.address = request.form['address']
        return redirect(url_for('showContacts'))
    else:
        return render_template('editContact.html', contact=editedContact)


@app.route('/contacts/<int:contact_id>/delete/', methods=['GET', 'POST'])
def deleteContact(contact_id):
    contactToDelete = session.query(Contact).filter_by(id=contact_id).one()
    if request.method == 'POST':
        session.delete(contactToDelete)
        session.commit()
        return redirect(url_for('showContacts', contact_id=contact_id))
    else:
        return render_template('deleteContact.html', contact=contactToDelete)


if __name__ == '__main__':
    app.debug = True
    app.run(port=4996)
