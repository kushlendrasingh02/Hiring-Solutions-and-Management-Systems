from mvc import create_app

from flask import Flask, session, redirect, url_for, request, render_template, flash

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)



