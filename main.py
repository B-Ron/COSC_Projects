from WebsiteProj import create_app

app = create_app() #create app

if __name__ == "__main__":
    app.run(debug=True) # only run web server through this file
    
