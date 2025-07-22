from app import create_app

app = create_app()

if __name__ == "__main__":
    # Flask 3 style
    app.run(debug=True, host="0.0.0.0", port=8001)
