import json

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

import requests


class ActionRetrieveCase(Action):

    

    def name(self) -> Text:
        return "action_retrieve_case"

    def __retrieve_case(self, key: Text) -> Text:
        """returns case according to key or empty string on failing"""

        resp = requests.get("http://www.boredapi.com/api/activity?type="+key)
        return json.loads(resp.content)['activity']

    def run(
        self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]
    ]:
        topic = tracker.get_slot('topic')
        case = self.__retrieve_case(topic)

        if case == '':
            dispatcher.utter_message(text="I could not find anything about {topic} :(")
        else:
            dispatcher.utter_message(text="I've found something interesting for you:")
            dispatcher.utter_message(text=case)

        return [SlotSet(key='topic', value=None)]