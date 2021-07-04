What is it?
----------
The main goal of this project is generating test data to upload
to Amplitude. Our product is an online adults school that has different directions.
First a table was created with event descriptions and taxonomy.

Link to event taxonomy:
https://docs.google.com/spreadsheets/d/1ySZpUSauX7w77MHUekV_siETWQhY27CaoHtuBbHDPio/edit#gid=367769533

* 1st page - Table with categories of events. Each of the standards is responsible for a
specific business process and contains a set of events that allow you to perform user 
behavior at each stage of the critical path. Below is a summary table of events with a 
description that is passed to Amplitude and is included in event_properties.

* 2nd page - Critical path table, a table with an example user_id, which is passed 
to Amplitude, and a user_properties table. In the captures user_id, user_properties there 
are also examples of values and a description of the parameters

* 3rd page - Category link event diagrams, with each event_properties and optional actions 
marked (for example, technical problems may arise and then the user clicks a button, or they may not, 
the user can apply a promo code or not), but no less the diagram illustrates a holistic path for the end 
of the event loop. But keep in mind that not every user completes the cycle. For example, he can click on the 
button to pay for banking operations, just close the tab, so after making a payment, an action should be taken 
on the click_confirm_payment event, payment confirmation. The curly braces indicate state changes in user_properties
or event_properties.

After this events were generated. Info for generating events is located in "info.py".
User properties are created in the "generate_users.py" file.
Events are generated and written to the file in the "generate_data.py" file.
All functions for generating events are located in "functions_of_events.py".
The code for uploading data to Amplitude is located in "upload_to_amplitude.py".
An example of the received data is the data in the  "data.json" file.


