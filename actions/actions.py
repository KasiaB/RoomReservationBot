# # This files contains your custom actions which can be used to run
# # custom Python code.
# #
# # See this guide on how to implement these action:
# # https://rasa.com/docs/rasa/custom-actions


# # This is a simple example for a custom action which utters "Hello World!"

# # from typing import Any, Text, Dict, List
# #
# # from rasa_sdk import Action, Tracker
# # from rasa_sdk.executor import CollectingDispatcher
# #
# #
# # class ActionHelloWorld(Action):
# #
# #     def name(self) -> Text:
# #         return "action_hello_world"
# #
# #     def run(self, dispatcher: CollectingDispatcher,
# #             tracker: Tracker,
# #             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
# #
# #         dispatcher.utter_message(text="Hello World!")
# #
# #         return []

# # from typing import Text, List, Any, Dict
# from typing import Dict, Text, Any, List, Union, Optional


# from rasa_sdk import Action, Tracker, FormValidationAction
# from rasa_sdk.events import SlotSet, UserUtteranceReverted
# from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.types import DomainDict

# from rasa_sdk.forms import FormAction


# # class ValidateRoomReservationForm(FormValidationAction):
# #     def name(self) -> Text:
# #         return "validate_room_reservation_form"

# #     # @staticmethod
# #     # def cuisine_db() -> List[Text]:
# #     #     """Database of supported cuisines"""

# #     #     return ["caribbean", "chinese", "french"]

# #     # def validate_cuisine(
# #     #     self,
# #     #     slot_value: Any,
# #     #     dispatcher: CollectingDispatcher,
# #     #     tracker: Tracker,
# #     #     domain: DomainDict,
# #     # ) -> Dict[Text, Any]:
# #     #     """Validate cuisine value."""

# #     #     if slot_value.lower() in self.cuisine_db():
# #     #         # validation succeeded, set the value of the "cuisine" slot to value
# #     #         return {"cuisine": slot_value}
# #     #     else:
# #     #         # validation failed, set this slot to None so that the
# #     #         # user will be asked for the slot again
# #     #         return {"cuisine": None}

    
# #     def validate_q2_date(
# #         self,
# #         value: Text,
# #         dispatcher: CollectingDispatcher,
# #         tracker: Tracker,
# #         domain: Dict[Text, Any],
# #     ) -> Dict[Text, Any]:

# #         # return_slots = []
# #         if value != None:
# #             datetime_obj = dateutil.parser.parse(value)
# #             q2_date= datetime_obj.strftime('%d-%m-%Y')
# #             # logger.info("humanDate value: {}".format(date))
# #             q4_starting_time = datetime_obj.strftime('%H:%M:%S')
# #             # logger.info("time value: {}".format(time))
# #             # return_slots.append(SlotSet("appt_date", apptDate))
# #             # return_slots.append(SlotSet("appt_time", time))

# #         # return return_slots
# #         return {"q2_date": value, "q4_starting_time": value}
    



# class RoomReservationForm(FormAction):
#     """A custom form action"""

#     def name(self) -> Text:
#         """Unique identifier of the form"""

#         return "tableBooking_form"

#     @staticmethod
#     def required_slots(tracker: Tracker) -> List[Text]:
#         """A list of required slots that the form has to fill"""

#         return ["q1_location", "q2_date", "q3_number_of_of_participants", "q4_starting_time", "q5_duration"]

#     def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
#         """A dictionary to map required slots to
#             - an extracted entity
#             - intent: value pairs
#             - a whole message
#             or a list of them, where a first match will be picked"""

#         return {
#             "q1_location": [
#                 self.from_entity(
#                     entity="LOC", intent=["request_room_reservation", "say_q3_number_of_participants"]
#                 ),
     
#             ],
#             "q2_date": [
#                 self.from_entity(entity="time",intent=["request_room_reservation", "say_q2_date"]),
                
                
               
#             ],
#             "q3_number_of_participants": [
#                 self.from_entity(entity="number", intent=["request_room_reservation", "say_q3_number_of_participants"]),
                
#             ],
#            "q4_time": [
#                 self.from_entity(entity="time", intent=["request_room_reservation", "say_q4_starting_time"]),
                
#             ],
#            "q5_duration": [
#                 self.from_entity(entity="duration", intent=["request_room_reservation", "say_q5_duration"]),
                
#             ],
#         }



#     # @staticmethod
#     # def is_int(string: Text) -> bool:
#     #     """Check if a string is an integer"""

#     #     try:
#     #         int(string)
#     #         return True
#     #     except ValueError:
#     #         return False

  

#     # def validate_num_people(
#     #     self,
#     #     value: Text,
#     #     dispatcher: CollectingDispatcher,
#     #     tracker: Tracker,
#     #     domain: Dict[Text, Any],
#     # ) -> Dict[Text, Any]:
#     #     """Validate num_people value."""

#     #     if self.is_int(value) and int(value) > 0:
#     #         return {"num_people": value}
#     #     else:
#     #         dispatcher.utter_template("utter_wrong_num_people", tracker)
#     #         # validation failed, set slot to None
#     #         return {"num_people": None}

#     # def validate_outdoor_seating(
#     #     self,
#     #     value: Text,
#     #     dispatcher: CollectingDispatcher,
#     #     tracker: Tracker,
#     #     domain: Dict[Text, Any],
#     # ) -> Dict[Text, Any]:
#     #     """Validate outdoor_seating value."""

#     #     if isinstance(value, str):
#     #         if "out" in value:
#     #             # convert "out..." to True
#     #             return {"outdoor_seating": True}
#     #         elif "in" in value:
#     #             # convert "in..." to False
#     #             return {"outdoor_seating": False}
#     #         else:
#     #             dispatcher.utter_template("utter_wrong_outdoor_seating", tracker)
#     #             # validation failed, set slot to None
#     #             return {"outdoor_seating": None}

#     #     else:
#     #         # affirm/deny was picked up as T/F
#     #         return {"outdoor_seating": value}

#     def submit(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> List[Dict]:
#         """Define what the form has to do
#             after all required slots are filled"""

#         # utter submit template
#         dispatcher.utter_message("Also ein Raum in {q1_location} für {q3_number_of_participants} Personen am {q2_date} um {q4_time}. Stimmt das?")
#         return []