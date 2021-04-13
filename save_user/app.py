import json
import re
# import requests


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    # Assuming the event will have sensor payload in
    # the event fed to the lambda function. event['movement']
    # Create an entry in the database about the sensor
    # trigger.
    write_movement_to_file(event['movement'])
    user_room = get_room('user')
    beast_room = get_room('beast')

    escape_class = EscapeFromBeast(user_room, beast_room)
    if not escape_class.user_is_safe():
        print("Alert for the user to move from to another room.")


def write_movement_to_file(sensor_payload):
    with open('database.txt', 'a') as phile:
        line_to_write = sensor_payload['occupant'] + "," + sensor_payload['room'] + "," + sensor_payload["time"]
        phile.write(line_to_write)


def get_room(organism):
    # Get the last entry with user in it.
    with open('database.txt', 'r') as phile:
        lines = phile.read()
        user_room = None
        for line in reversed(lines):
            if re.match(organism, line):
                # return the mid element after splitting.
                user_room = line.split(',')[1]
                break

        return user_room


class EscapeFromBeast:
    def __init__(self, user_room, beast_room):
        self.user_room = user_room
        self.beast_room = beast_room

    def user_is_safe(self):
        # returns true if the beast room is not adjacent
        # to user room else false.
        if self.user_room is None or self.beast_room is None:
            # is either of them is None, this means
            # we dont have much information about the
            # user/beast location and thereby assuming the
            # user to be safe.
            return True

        # let i,j denote user co-ordinates
        # let a,b denote beast co-ordinates.
        i,j = self.user_room
        a,b = self.beast_room

        safe = None
        if i == a:
            if abs(j-i) == 1:
                safe = False
            else:
                safe = True
        else:
            if abs(i-a) == 1:
                safe = False
            else:
                safe = True

        return safe












