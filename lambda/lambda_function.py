# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import ask_sdk_core.utils as ask_utils
import requests

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Welcome to Covid Hero! You can know coronavirus cases update, news and symptoms here."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CovidStateHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("CovidState")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        slots = handler_input.request_envelope.request.intent.slots
        state = slots['state'].value.lower()
        speak_output = " "
        api_address = "https://api.covid19india.org/data.json"
        json_data = requests.get(api_address).json()
        num=range(0,38)
        for n in num:
            if state == json_data['statewise'][n]['state'].lower():
                Confirmed_Case = json_data['statewise'][n]['confirmed'] 
                Active_Case = json_data['statewise'][n]['active']
                Total_Deaths = json_data['statewise'][n]['deaths']
            n+= 1
        speak_output = "Coronavirus Cases in {} are like confirmed cases are {} in which active cases are {} and total deaths are {}. ".format(state, Confirmed_Case, Active_Case, Total_Deaths)
        reprompt_output = ' Want to know the coronavirus cases of other states?'
        return (
            handler_input.response_builder
                .speak(speak_output + reprompt_output)
                .ask(reprompt_output)
                .response
        )


class CovidCountryHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("CovidCountry")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        slots = handler_input.request_envelope.request.intent.slots
        country = slots['country'].value.lower()
        speak_output = " "
        api_address = "https://covid-19.dataflowkit.com/v1/{}".format(country)
        json_data = requests.get(api_address).json()
        Confirmed_Case = json_data['Total Cases_text']
        Active_Case = json_data['Active Cases_text']
        Total_Deaths = json_data['Total Deaths_text']
        speak_output = "Coronavirus Cases in {} are like confirmed cases are {} in which active cases are {} and total deaths are {}. ".format(country, Confirmed_Case, Active_Case, Total_Deaths)
        reprompt_output = ' Want to know the coronavirus cases of other countries and Indian states?'
        return (
            handler_input.response_builder
                .speak(speak_output + reprompt_output)
                .ask(reprompt_output)
                .response
        )

class TotalCovidHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("TotalCovid")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = ""
        api_address = "https://covid-19.dataflowkit.com/v1/world"
        json_data = requests.get(api_address).json()
        Confirmed_Case = json_data['Total Cases_text']
        Active_Case = json_data['Active Cases_text']
        Total_Deaths = json_data['Total Deaths_text']
        Recovered_Case = json_data['Total Recovered_text']
        speak_output = "Coronavirus Cases in the world are like confirmed cases are {} in which active cases are {}, total deaths are {} and recovered cases are {}. ".format(Confirmed_Case, Active_Case, Total_Deaths, Recovered_Case)
        reprompt_output = ' Want to know the coronavirus cases of other countries and Indian states?'
        return (
            handler_input.response_builder
                .speak(speak_output + reprompt_output)
                .ask(reprompt_output)
                .response
        )


class CovidHeadlinesHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("CovidHeadlines")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        api_address = 'http://newsapi.org/v2/top-headlines?country=in&q=COVID&apiKey=067e2926d01e46ba950031664c5be431'
        response = requests.get(api_address)
        response_json = response.json()
        formatted_response = [ i['title'] for i in response_json['articles']]
        speak_output = 'These are some news headlines: {} '.format(formatted_response)
        reprompt_output = ' Want to know coronavirus cases of other countries?'
        return (
            handler_input.response_builder
                .speak(speak_output + reprompt_output)
                .ask(reprompt_output)
                .response
        )

class CoronavirusHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("Coronavirus")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = 'According to the World Health Organization, there are many different coronaviruses (CoV). They can cause illnesses ranging from the common cold to more severe lung infection. COVID-19 is the disease caused by the new or "novel" coronavirus.'
        reprompt_output = ' Want to know the coronavirus cases of other countries and Indian states?'
        return (
            handler_input.response_builder
                .speak(speak_output + reprompt_output)
                .ask(reprompt_output)
                .response
        )

class CovidSymptomsHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("CovidSymptoms")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = 'According to the Center for Disease Control and Prevention, current symptoms reported for patients with COVID-19 have included fever, with a temperature above 100.4 °F or 38 °C, cough, shortness of breath or difficulty breathing, chills, muscle pain, sore throat, and new loss of taste or smell. Symptoms may appear 2-14 days after exposure. This list is not all inclusive. Other less common symptoms have been reported, including gastrointestinal symptoms like nausea, vomiting, or diarrhea.'
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = 'Hello, to use covid hero you say like coronavirus cases in Delhi or India. To know covid 19 news headlines try to say like coronavirus news. To know symptoms say coronavirus symptoms.'
        reprompt_output = ' Try to say like coronavirus cases in Delhi or India'
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(reprompt_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Goodbye! see you soon. Stay Safe Stay Home."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I had trouble doing what you asked. Please try again or say help to learn more."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(CovidStateHandler())
sb.add_request_handler(CovidCountryHandler())
sb.add_request_handler(TotalCovidHandler())
sb.add_request_handler(CovidHeadlinesHandler())
sb.add_request_handler(CoronavirusHandler())
sb.add_request_handler(CovidSymptomsHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()