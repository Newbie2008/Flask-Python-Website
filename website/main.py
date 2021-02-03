from __init__ import create_app
# Starting up the Flask server
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)