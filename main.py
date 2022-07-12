import re
import long_responses as long
import requests
from flask import Flask, request, render_template



def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    #Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty +=1

    #Calculates the percentage of recognised words in a user message
    percentage = float(message_certainty) / float (len(recognised_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage*100)
    else:
        return 0



app = Flask(__name__)
@app.get("/")
def index_get():
    return render_template("base.html")

@app.post("/weather")
def weather():
    query = request.get_json().get("message")
    stopwords = ['what', 'is', 'the', 'weather', 'climate', 'temperature', 'temp', 'humidity', 'condition', 'over', 'in', 'right', 'now']
    querywords = query.split()

    resultwords = [word for word in querywords if word.lower() not in stopwords]
    city_name = ' '.join(resultwords)
    api_key = "AAAAPPPPIIII_____KKKKEEEEYYYY"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    # city_name = input("Enter city name : ")
    complete_url = base_url + "appid=" + 'd850f7f52bf19300a9eb4b0aa6b80f0d' + "&q=" + city_name
    response1 = requests.get(complete_url)
    x = response1.json()
    if len(city_name) == 0:
        response = long.unknown()
    else:
        if x["cod"] != "404":
            y = x["main"]

            current_temperature = y["temp"]
            celcius = float(current_temperature - 273)
            format_celsius = "{:.2f}".format(celcius)

            feels_like_kelvin = y["feels_like"]
            feels_like_celcius = float(feels_like_kelvin - 273)
            format_feels_like = "{:.2f}".format(feels_like_celcius)

            humidity = str(y["humidity"])
            city_name_api = x["name"]
            z = x["weather"]

            weather_description = z[0]["description"]

              #print(city_name)
            response = 'The weather currently in ' + city_name_api + " is " + format_celsius + "°C with " + weather_description + ". Feels like " + format_feels_like + "°C with humidity " + humidity + "%"
        else:
            response = long.unknown()
    return response


def time():
    from datetime import datetime

    now = datetime.now()

    current_time = now.strftime("%H:%M")
    return current_time

def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response = False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)



    #Responses--------------------------------------------------------------

    response('Hello!', ['hello', 'hi', 'sup', 'hey', 'howdy', 'hola'], single_response=True)
    response("I'm doing fine, and you?", ['how', 'are', 'you', 'doing', 'doin', 'alright', 'do', 'okay'], required_words=['how'])
    response("I am glad to hear that", ['im', 'i', 'am', 'good'], required_words=['good'])
    response("I am glad to hear that", ['im', 'i', 'am', 'fine'], required_words=['fine'])

    response('Thank you!', ['i', 'like', 'love', 'you', 'nice', 'good'], required_words=['you'])
    response('I am sorry, I would try to improve!', ['i', 'hate', 'you', 'bad', 'hor     rible', 'suck'], required_words=['you'])
    response('Peanuts!', ['what', 'do', 'you', 'like'], required_words=['like'])
    response('I am quite new and still small', ['how', 'old', 'are', 'you'], required_words=['how', 'old'])
    response('I am quite new and still small', ['what', 'your', 'age'], required_words=['age'])
    response('The time currently is ' + time(), ['time', 'now'], required_words=['time'])


    response('Bye! I am going to sleep\n'+long.sleep(), ['bye', 'sleep', 'exit', 'goodbye', 'tata', 'adios'])
    response(weather() ,['weather', 'climate', 'temperature', 'humidity', 'temp', 'condition'])

    response(long.joke(), ['tell', 'me','joke','laugh', 'make'])

    response(long.R_EATING, ['what', 'you','have','lunch', 'eat'], required_words=['you', 'eat'])
    response(long.R_NAME, ['what', 'is', 'your','name'], required_words=['your', 'name'])
    response(long.R_NAME, ['who', 'are','you'], required_words=['who', 'are', 'you'])


    #Responses---------------------------------------------------------------------------

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    #print(highest_prob_list)

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match

def get_response(text):
    split_message = re.split(r'\s+|[,;?!.-]\s*', text.lower())
    response = check_all_messages(split_message)
    return response


#testing the response system
#while True:
    #key = input('You: ')
    #print('Anya: ' + get_response(key))

