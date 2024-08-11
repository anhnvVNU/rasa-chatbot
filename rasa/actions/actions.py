# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

import csv
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionHandlePositiveFeedback(Action):

    def name(self) -> Text:
        return "action_handle_positive_feedback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        aspect = tracker.get_slot('aspect')
        user_message = tracker.latest_message.get('text')
        feedback_type = "Positive"

        # Save feedback to CSV file
        with open('feedback.csv', mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([feedback_type, aspect, user_message])

        dispatcher.utter_message(text=f"Cảm ơn bạn đã phản hồi rất tích cực về {aspect}!")
        return []

class ActionHandleNegativeFeedback(Action):

    def name(self) -> Text:
        return "action_handle_negative_feedback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        aspect = tracker.get_slot('aspect')
        user_message = tracker.latest_message.get('text')
        feedback_type = "Negative"

        # Save feedback to CSV file
        with open('feedback.csv', mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([feedback_type, aspect, user_message])

        dispatcher.utter_message(text=f"Chúng tôi rất tiếc khi nghe về trải nghiệm không tốt của bạn với {aspect}. Chúng tôi sẽ cố gắng cải thiện.")
        return []